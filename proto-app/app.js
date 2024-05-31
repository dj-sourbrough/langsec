const express = require('express');
const bodyParser = require('body-parser');
const _ = require('lodash');

const {ajv} = require("./schemaValidation");

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Temporary storage for users
let users = [];
let userIdCounter = 1; 

// Function to generate unique user IDs
function generateUserId() {
    return userIdCounter++;
}

function setObjValue(obj, path, value) {
    obj[path] = value;
}

// INDIRECT PROTYOTYPE POLLUTION
// User registration route
app.post('/register', (req, res) => {
    // const { username, password } = req.body;
    const payload = req.body;
    let newUser = {};
    // let newUser = Map();
    /*
    validate = ajv.getSchema("user");
    if (!validate(payload)) {
        console.log("invalid data")
        return res.status(400)
    }
    */

    // Auto-generate user ID
    const userId = generateUserId();
    newUser.id = userId;

    _.merge(newUser, payload);

    // Check if the user is already registered
    const existingUser = users.find(user => user.username === username);
    if (existingUser) {
        return res.status(400).send('User already registered');
    }
    // Create a new user and save to the list
    users.push({ newUser });
    res.send('User registered successfully');
    console.log(users)
});

// DIRECT PROTYOTYPE POLLUTION
// User update route by id
app.post('/update/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    const userIndex = users.findIndex(user => user.id === userId);
    setObjValue(users[userIndex], req.body.path, req.body.value);
});

// Route to get the role of a user by ID
app.get('/users/:id/role', (req, res) => {
    const userId = parseInt(req.params.id);
    const user = users.find(user => user.id === userId);

    if (!user) {
        return res.status(404).send('User not found');
    }

    res.json({ id: user.id, role: user.role });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
