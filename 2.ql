/**
 * @name Potential Prototype Pollution via Direct Assignment
 * @description Detects direct assignments with potentially user-controlled source objects
 * @kind problem
 * @problem.severity warning
*/

import javascript

/**
* Detect direct assignments (object[path] = userInput)
*/
from AssignExpr assignment
where
    assignment.getLhs() instanceof IndexExpr and
    assignment.getRhs() instanceof Expr
select assignment, "Potential prototype pollution via direct assignment"
 