/*
 * https://leetcode.com/problems/combine-two-tables/
 *
 * Runtime: 342 ms, faster than 85.68% of MySQL online submissions for Combine Two Tables.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
 */

SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
USING (personId);
