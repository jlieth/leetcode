/*
 * https://leetcode.com/problems/the-latest-login-in-2020/
 *
 * Runtime: 588 ms, faster than 73.21% of MySQL online submissions for The Latest Login in 2020.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for The Latest Login in 2020.
 */

SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = "2020"
GROUP BY user_id;
