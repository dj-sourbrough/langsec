const Ajv = require("ajv");
const schema_user = require("./schemas/schema_user.json")

const ajv = exports.ajv = new Ajv();
ajv.addSchema(schema_user, "user")