-- https://school.programmers.co.kr/learn/courses/30/lessons/301649


WITH CTE1 AS(
    SELECT id,
        ROW_NUMBER() OVER(ORDER BY size_of_colony DESC) as rn
        FROM ecoli_data
),  
CTE2 AS(
SELECT COUNT(*) AS count
        FROM ecoli_data
),
CTE3 AS(
SELECT *
    FROM CTE1, CTE2
)

SELECT id,
    CASE
        WHEN rn <= 0.25 * count THEN 'CRITICAL'
        WHEN rn > 0.25 * count AND rn <= 0.5 * count THEN 'HIGH'
        WHEN rn > 0.5 * count AND rn <= 0.75 * count THEN 'MEDIUM'
        WHEN rn > 0.75 * count THEN 'LOW'
    END AS colony_name
    FROM CTE3
    ORDER BY id;