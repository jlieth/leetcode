/*
 * https://leetcode.com/problems/patients-with-a-condition/
 *
 * Runtime: 313 ms, faster than 71.95% of MySQL online submissions for Patients With a Condition.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Patients With a Condition.
 */

SELECT *
FROM Patients
WHERE conditions RLIKE '\\bDIAB1';
