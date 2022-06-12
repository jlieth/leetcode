/*
 * https://leetcode.com/problems/calculate-special-bonus/
 *
 * Runtime: 514 ms, faster than 84.81% of MySQL online submissions for Calculate Special Bonus.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Calculate Special Bonus.
 */

SELECT
    employee_id,
    IF(employee_id MOD 2 = 0 OR name LIKE "M%", 0, salary) as bonus
FROM Employees
ORDER BY employee_id;
