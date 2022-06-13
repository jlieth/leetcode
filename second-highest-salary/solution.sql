/*
 * https://leetcode.com/problems/second-highest-salary/
 *
 * Runtime: 213 ms, faster than 77.34% of MySQL online submissions for Second Highest Salary.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
 */

SELECT
    IF(COUNT(salary) = 0, NULL, salary) AS SecondHighestSalary
FROM (
    SELECT DISTINCT salary
    FROM Employee t1
    ORDER BY salary DESC
    LIMIT 1
    OFFSET 1
) t2;
