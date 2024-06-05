const express = require('express');
const bodyParser = require('body-parser');
const _ = require('lodash');
const ejs = require('ejs');

const {ajv} = require("./schemaValidation");

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.set('view engine', 'ejs')
Object.freeze(Object)

// Temporary storage for users
let users = [];
let userIdCounter = 1; 
let notes = {};

// Function to generate unique user IDs
function generateUserId() {
    return userIdCounter++;
}

function setObjValue(obj, path, value) {
    obj[path] = value;
}

// Function to set value at path in object
function set(obj, path, value) {
    const keys = path.split('.');
    let current = obj;

    for (let i = 0; i < keys.length - 1; i++) {
      if (!current[keys[i]]) {
        current[keys[i]] = {};
      }
      current = current[keys[i]];
    }

    current[keys[keys.length - 1]] = value;
}

app.get('/', (req, res) => {
    res.render('index');
})

// INDIRECT PROTYOTYPE POLLUTION
// User registration route
app.post('/register', (req, res) => {
    // const { username, password } = req.body;
    const payload = req.body;
    console.log(payload);
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
    users.push(newUser);
    res.send('User registered successfully');
});

// DIRECT PROTOTYPE POLLUTION
// User update route by id
app.post('/update/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    const userIndex = users.findIndex(user => user.id === userId);
    
    if (userIndex === -1) {
        return res.status(404).send('User not found');
    }

    setObjValue(users[userIndex], req.body.path, req.body.value);
    // Set the value at the specified path in the user object
    set(users[userIndex], req.body.path, req.body.value);

    res.send('User updated successfully');
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