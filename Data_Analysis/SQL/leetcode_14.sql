-- https://leetcode.com/problems/game-play-analysis-iv/

SELECT ROUND((COUNT(*) FILTER(WHERE B.player_id = B.prev_id AND B.event_date = B.prev_date + 1)::DECIMAL) / COUNT(*) FILTER(WHERE B.player_id != B.prev_id), 2) AS fraction
    FROM(
        SELECT *
            , LAG(A.player_id, 1, 0) OVER() AS prev_id
            , LAG(A.event_date) OVER() AS prev_date
            FROM(
                SELECT *
                    FROM(
                        SELECT *
                            ,ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS RANK
                            FROM activity
                    ) as rn
                    WHERE rn.RANK < 3
            ) AS A
    )AS B;

-- 코드만 봐도 효율이 안나올 것 같은 그런 느낌....


-- 첫 번째 수정한 쿼리(use with문)
WITH B AS(
    SELECT *
            , LAG(A.player_id, 1, 0) OVER() AS prev_id
            , LAG(A.event_date) OVER() AS prev_date
            FROM(
                SELECT *
                    FROM(
                        SELECT *
                            ,ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS RANK
                            FROM activity
                    ) as rn
                    WHERE rn.RANK < 3
            ) AS A
)


SELECT ROUND((COUNT(*) FILTER(WHERE B.player_id = B.prev_id AND B.event_date = B.prev_date + 1)::DECIMAL) / COUNT(*) FILTER(WHERE B.player_id != B.prev_id), 2) AS fraction
    FROM B;



-- 두 번째 수정한 쿼리

WITH CTE AS(   
    SELECT *
    , LAG(player_id, 1, 0) OVER() AS prev_id
    , LAG(event_date) OVER() AS prev_date
    , ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS RANK
    FROM activity      
)


SELECT ROUND(
    (
        SELECT COUNT(*)
            FROM CTE
            WHERE CTE.RANK = 2
            AND CTE.event_date = CTE.prev_date + 1
    )::DECIMAL
    /
    (
        SELECT COUNT(*)
            FROM CTE
            WHERE CTE.RANK = 1
    )
, 2) AS fraction
-- 서브쿼리는 데이터 사용량이 많기 때문에 최대한 줄이는 방법을 선택했고
-- ROW_NUMBER()를 이용하여 코드를 더 간결하게 만들었다.