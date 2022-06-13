/*
 * https://leetcode.com/problems/group-sold-products-by-the-date/
 *
 * Runtime: 386 ms, faster than 85.39% of MySQL online submissions for Group Sold Products By The Date.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Group Sold Products By The Date.
 */

SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
