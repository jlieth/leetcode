/*
 * https://leetcode.com/problems/find-total-time-spent-by-each-employee/
 *
 * Runtime: 477 ms, faster than 76.63% of MySQL online submissions for Find Total Time Spent by Each Employee.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Find Total Time Spent by Each Employee.
 */

SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
