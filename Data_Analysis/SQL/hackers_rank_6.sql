-- https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true



WITH numbered AS (
    SELECT 
        lat_n,
        ROW_NUMBER() OVER(ORDER BY lat_n ASC) AS index_row,
        COUNT(*) OVER () AS total_rows
    FROM station
)   

SELECT
    ROUND(AVG(lat_n), 4) AS mediana
FROM numbered
WHERE index_row IN (
    FLOOR((total_rows + 1) / 2),
    CEIL((total_rows + 1) / 2)
);