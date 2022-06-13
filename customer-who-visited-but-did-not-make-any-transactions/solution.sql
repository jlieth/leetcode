/*
 * https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
 *
 * Runtime: 976 ms, faster than 95.38% of MySQL online submissions for Customer Who Visited but Did Not Make Any Transactions.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customer Who Visited but Did Not Make Any Transactions.
 */

SELECT
    customer_id,
    COUNT(*) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (
    SELECT DISTINCT visit_id FROM Transactions
)
GROUP BY customer_id;
