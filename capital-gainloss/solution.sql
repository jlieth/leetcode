/*
 * https://leetcode.com/problems/capital-gainloss/
 *
 * Runtime: 414 ms, faster than 96.51% of MySQL online submissions for Capital Gain/Loss.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Capital Gain/Loss.
 */

SELECT
    stock_name,
    SUM(
        CASE
            WHEN operation = "Buy" THEN -1 * price
            ELSE price
        END
    ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
