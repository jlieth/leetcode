/*
 * https://leetcode.com/problems/customers-who-never-order/
 *
 * Runtime: 423 ms, faster than 85.20% of MySQL online submissions for Customers Who Never Order.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
 */

SELECT name as Customers
FROM Customers
WHERE id NOT IN (
    SELECT DISTINCT customerId from Orders
);
