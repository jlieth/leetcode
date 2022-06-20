/*
 * https://leetcode.com/problems/bank-account-summary-ii/
 *
 * Runtime: 566 ms, faster than 90.02% of MySQL online submissions for Bank Account Summary II.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Bank Account Summary II.
 */

SELECT
    name,
    SUM(amount) AS balance
FROM Users
LEFT JOIN Transactions
USING (account)
GROUP BY account
HAVING balance >= 10000;
