-- https://school.programmers.co.kr/learn/courses/30/lessons/299310


WITH CTE AS(
SELECT EXTRACT(YEAR FROM DIFFERENTIATION_DATE) AS 연도, size_of_colony, id
    FROM ecoli_data
),
CTE2 AS(
    SELECT 연도, MAX(size_of_colony) AS MAX
        FROM CTE
        GROUP BY 연도
)
SELECT 연도 AS year, MAX-size_of_colony AS year_dev, id
    FROM CTE
    LEFT JOIN CTE2
    USING (연도)
    ORDER BY year, year_dev