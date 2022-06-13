/*
 * https://leetcode.com/problems/tree-node/
 *
 * Runtime: 398 ms, faster than 78.04% of MySQL online submissions for Tree Node.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Tree Node.
 */

SELECT DISTINCT
    node.id,
    CASE
        WHEN node.p_id IS NULL THEN "Root"
        WHEN child.id IS NULL THEN "Leaf"
        ELSE "Inner"
    END AS type
FROM Tree node
LEFT JOIN Tree child
ON node.id = child.p_id
ORDER BY node.id;
