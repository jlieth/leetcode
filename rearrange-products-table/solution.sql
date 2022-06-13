/*
 * https://leetcode.com/problems/rearrange-products-table/
 *
 * Runtime: 736 ms, faster than 15.01% of MySQL online submissions for Rearrange Products Table.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rearrange Products Table.
 */

SELECT
    product_id,
    "store1" as store,
    store1 as price
FROM Products
WHERE store1 IS NOT NULL

UNION

SELECT
    product_id,
    "store2" as store,
    store2 as price
FROM Products
WHERE store2 IS NOT NULL

UNION

SELECT
    product_id,
    "store3" as store,
    store3 as price
FROM Products
WHERE store3 IS NOT NULL;
