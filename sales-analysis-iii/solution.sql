/*
 * https://leetcode.com/problems/sales-analysis-iii/
 *
 * Runtime: 947 ms, faster than 93.74% of MySQL online submissions for Sales Analysis III.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Sales Analysis III.
 */

SELECT
    product_id,
    product_name
FROM Product
LEFT JOIN Sales
USING (product_id)
GROUP BY product_id
HAVING
    MIN(sale_date) >= "2019-01-01" AND
    MAX(sale_date) <= "2019-03-31"
