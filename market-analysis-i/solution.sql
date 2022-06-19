/*
 * https://leetcode.com/problems/market-analysis-i/
 *
 * Runtime: 942 ms, faster than 94.65% of MySQL online submissions for Market Analysis I.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Market Analysis I.
 */

SELECT
    user_id AS buyer_id,
    join_date,
    SUM(IF(YEAR(order_date) = 2019, 1, 0)) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
ON user_id = buyer_id
GROUP BY user_id;
