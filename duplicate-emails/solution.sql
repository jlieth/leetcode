/*
 * https://leetcode.com/problems/duplicate-emails/
 *
 * Runtime: 312 ms, faster than 88.24% of MySQL online submissions for Duplicate Emails.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
 */

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
