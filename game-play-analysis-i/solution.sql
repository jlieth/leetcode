/*
 * https://leetcode.com/problems/game-play-analysis-i/
 *
 * Runtime: 480 ms, faster than 86.31% of MySQL online submissions for Game Play Analysis I.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Game Play Analysis I.
 */

SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
