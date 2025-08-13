-- https://school.programmers.co.kr/learn/courses/30/lessons/133027



WITH CTE AS(
    SELECT * FROM first_half
    UNION ALL
    SELECT * FROM july    
)

SELECT flavor
    FROM (
        SELECT flavor, SUM(total_order) AS sum
        FROM CTE
        GROUP BY flavor
        ORDER BY sum DESC
    ) AS C
    LIMIT 3;