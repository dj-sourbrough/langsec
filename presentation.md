# Prototype

- Prototype pollution is a vulnerability specific to the JavaScript ecosystem discovered by a security research Arteau in 2018
- Due to how object-inheritance is implemented and the fact that JavaScript is dynamically typed, improper assignment of key-value pairs to objects can be polute all objects in a JavaScript application
- With "__proto__" as a key, and another key-value pair as the assigned value

# Goals

- Our goals are to implement a simple web application with these vulnerabilities present.
- This is done in order to showcase these exploits,
- test and discuss different monitoring tools to discover these pollutions
- implement different mitigation strategies

# Mitigations

- Avoiding direct assignment of key value pairs of user controlled output
- Internally this can be done by using a JavaScript Map instead of Object as these do not inherit from the prototype-chain
- Setting prototype to null
- Indirect vulnerabilities:
    - Updating from known vulnerabilities
    - How to guard against unknown?:
        - Object.freeze(Object.prototype)
            - Downstream objects cannot redefine standard methods
        - Schema Validation of Input
            - Format not always known
            - developer cost

# Insights

- With a prototype pollution injection sink, projects using html-sanitizers can be have these security measures nullified by polluting allowedTags properties, leading to a further host of xss exploits
- Seen that some project maintainers are unaware of how their projects can be utilized as an execution gadget in order to trigger remote code execution.
- ejs, with 14000 dependent packages, was unchanged for over a year after issues had been raised on their github page relating to their vulnerability
