// advanced_queries.ql

/**
 * This query identifies unused variables in the codebase.
 * @name Unused Variables
 * @kind problem
 * @problem.severity warning
 * @id python/unused-variables
 */

import python

from Variable v
where not v.getAnAssignment().isUsed()
select v, "This variable is declared but never used."

/**
 * This query detects functions with high cyclomatic complexity.
 * @name High Cyclomatic Complexity
 * @kind problem
 * @problem.severity warning
 * @id python/high-cyclomatic-complexity
 */

import python

from Function f
where f.getBody().(Statement).exists(s | 
      s instanceof IfStatement or 
      s instanceof ForStatement or 
      s instanceof WhileStatement) // Counting decision points
select f, "This function has high cyclomatic complexity."

/**
 * This query checks for potential SQL injection vulnerabilities.
 * @name SQL Injection Vulnerabilities
 * @kind problem
 * @problem.severity error
 * @id python/sql-injection
 */

import python

from Call c
where c.getTarget().hasName("execute") and 
      (c.getArgument(0).(StringLiteral).getValue().indexOf("SELECT") >= 0 or
       c.getArgument(0).(StringLiteral).getValue().indexOf("INSERT") >= 0 or
       c.getArgument(0).(StringLiteral).getValue().indexOf("UPDATE") >= 0)
select c, "Potential SQL injection vulnerability detected."
