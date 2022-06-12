/*
 * https://leetcode.com/problems/recyclable-and-low-fat-products/
 *
 * Runtime: 438 ms, faster than 89.64% of MySQL online submissions for Recyclable and Low Fat Products.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Recyclable and Low Fat Products.
 */

SELECT product_id
FROM Products
WHERE
    low_fats = "Y" AND
    recyclable = "Y"
;
