/*
 * https://leetcode.com/problems/swap-salary/
 *
 * Runtime: 219 ms, faster than 80.55% of MySQL online submissions for Swap Salary.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.
 */

UPDATE Salary
SET sex = IF(sex = "m", "f", "m");
