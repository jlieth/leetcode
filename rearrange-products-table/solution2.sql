/*
 * https://leetcode.com/problems/rearrange-products-table/
 *
 * Runtime: 476 ms, faster than 79.12% of MySQL online submissions for Rearrange Products Table.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rearrange Products Table.
 */

SELECT
    p.product_id,
    x.*
FROM Products p
CROSS JOIN LATERAL (
    SELECT "store1", store1 WHERE store1 IS NOT NULL
	UNION ALL SELECT "store2", store2 WHERE store2 IS NOT NULL
	UNION ALL SELECT "store3", store3 WHERE store3 IS NOT NULL
) AS x(store, price);
