/*
 * https://leetcode.com/problems/fix-names-in-a-table/
 *
 * Runtime: 703 ms, faster than 43.41% of MySQL online submissions for Fix Names in a Table.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Fix Names in a Table.
 */

SELECT
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) as name
FROM Users
ORDER BY user_id;
