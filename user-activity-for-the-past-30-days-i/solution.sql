/*
 * https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
 *
 * Runtime: 374 ms, faster than 96.12% of MySQL online submissions for User Activity for the Past 30 Days I.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for User Activity for the Past 30 Days I.
 */

SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN "2019-06-28" AND "2019-07-27"
GROUP BY activity_date;
