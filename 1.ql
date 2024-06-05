/**
 * @name Potential Prototype Pollution via _.merge or Direct Assignment
 * @description Detects calls to _.merge or direct assignments with potentially user-controlled source objects
 * @kind problem
 * @problem.severity warning
*/

import javascript

/**
* Detect calls to _.merge
*/
from CallExpr call
where
  call.getCallee().(PropAccess).getBase().(VarAccess).getName() = "_" and
  call.getCallee().(PropAccess).getPropertyName() = "merge"
select call, "Potential prototype pollution via _.merge with user-controlled source"
