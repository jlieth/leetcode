/*
 * https://leetcode.com/problems/article-views-i/
 *
 * Runtime: 407 ms, faster than 73.86% of MySQL online submissions for Article Views I.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Article Views I.
 */

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;
