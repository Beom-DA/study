-- https://leetcode.com/problems/game-play-analysis-i/
-- 내가 짠 쿼리
SELECT A.player_id, A.event_date AS first_login
    FROM(
        SELECT player_id, event_date
            ,LAG(player_id) OVER() AS pre_id
            FROM (
                SELECT * FROM activity ORDER BY player_id, event_date
            )
    ) AS A
    WHERE A.pre_id IS NULL
    OR A.player_id != A.pre_id;

-- 참고 쿼리(ㅋㅋㅋ...)
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;