/*
 * https://leetcode.com/problems/rising-temperature/
 *
 * Runtime: 413 ms, faster than 82.53% of MySQL online submissions for Rising Temperature.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.
 */

SELECT w1.id
FROM Weather w1
LEFT JOIN Weather w2
ON w1.recordDate = ADDDATE(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;
