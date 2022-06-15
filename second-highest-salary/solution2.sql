/*
 * https://leetcode.com/problems/second-highest-salary/
 *
 * Runtime: 189 ms, faster than 96.28% of MySQL online submissions for Second Highest Salary.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
 */

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
