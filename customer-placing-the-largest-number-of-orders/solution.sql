/*
 * https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
 *
 * Runtime: 389 ms, faster than 92.89% of MySQL online submissions for Customer Placing the Largest Number of Orders.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customer Placing the Largest Number of Orders.
 */

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

-- follow-up where more than one customer can have the largest number of order:
SELECT customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(*) = (
    SELECT COUNT(*) AS num_orders
    FROM Orders
    GROUP BY customer_number
    ORDER BY num_orders DESC
    LIMIT 1
);
