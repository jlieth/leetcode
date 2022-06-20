/*
 * https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
 *
 * Runtime: 353 ms, faster than 76.97% of MySQL online submissions for Actors and Directors Who Cooperated At Least Three Times.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Actors and Directors Who Cooperated At Least Three Times.
 */

SELECT
    actor_id,
    director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
