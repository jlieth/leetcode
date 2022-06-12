/*
 * https://leetcode.com/problems/delete-duplicate-emails/
 *
 * Runtime: 859 ms, faster than 54.17% of MySQL online submissions for Delete Duplicate Emails.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
 */

DELETE p1
FROM
    Person p1,
    Person p2
WHERE
    p2.id < p1.id AND
    p2.email = p1.email
;
