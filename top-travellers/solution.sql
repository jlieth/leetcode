/*
 * https://leetcode.com/problems/top-travellers/
 *
 * Runtime: 615 ms, faster than 94.97% of MySQL online submissions for Top Travellers.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Top Travellers.
 */

SELECT
    name,
    IFNULL(SUM(distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY 2 DESC, 1 ASC;
