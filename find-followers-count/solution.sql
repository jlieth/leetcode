/*
 * https://leetcode.com/problems/find-followers-count/
 *
 * Runtime: 441 ms, faster than 95.27% of MySQL online submissions for Find Followers Count.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Find Followers Count.
 */

SELECT
    user_id,
    COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
