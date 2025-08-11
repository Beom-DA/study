-- https://school.programmers.co.kr/learn/courses/30/lessons/59413


WITH RECURSIVE CTE1 AS(
    SELECT 0 AS hour_value
    
    UNION ALL
    
    SELECT hour_value + 1
        FROM CTE1
        WHERE hour_value < 23
),
CTE2 AS (
    SELECT hour, count(*) AS count
        FROM(
            SELECT EXTRACT(hour FROM datetime) AS hour
                FROM animal_outs 
            ) A
        GROUP BY hour
        ORDER BY hour
)

SELECT CTE1.hour_value AS hour, COALESCE(CTE2.count,0) AS count
    FROM CTE1
    LEFT JOIN CTE2
    ON CTE1.hour_value = CTE2.hour
    ORDER BY hour;