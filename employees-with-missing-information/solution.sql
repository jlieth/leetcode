/*
 * https://leetcode.com/problems/employees-with-missing-information/
 *
 * Runtime: 599 ms, faster than 37.47% of MySQL online submissions for Employees With Missing Information.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees With Missing Information.
 */

-- select employees without salary info
SELECT e.employee_id
FROM Employees e
LEFT JOIN Salaries s
USING (employee_id)
WHERE s.salary IS NULL

UNION

-- select salary info without corresponding employee
SELECT s.employee_id
FROM Salaries s
LEFT JOIN Employees e
USING (employee_id)
WHERE e.name IS NULL

ORDER BY employee_id;
