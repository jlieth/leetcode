/*
 * https://leetcode.com/problems/sales-person/
 *
 * Runtime: 1062 ms, faster than 85.51% of MySQL online submissions for Sales Person.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Sales Person.
 */

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    WHERE com_id = (SELECT com_id FROM Company WHERE name = "RED")
);
