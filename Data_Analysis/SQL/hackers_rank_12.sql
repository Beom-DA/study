-- https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true




WITH CTE AS(
    SELECT start_date, ROW_NUMBER() OVER() AS rn
        FROM (
            SELECT  COALESCE(LAG(end_date) OVER(), 
                CAST('2025-08-18' AS DATE)) AS prev_end_date, start_date
                FROM projects    
                ORDER BY start_date
        ) AS CTE1
        WHERE prev_end_date != start_date
),
CTE2 AS(
    SELECT end_date, ROW_NUMBER() OVER() AS rn
        FROM (
            SELECT  end_date,
                COALESCE(LEAD(start_date) OVER(), CAST('2025-08-18' AS DATE)) AS    
                next_start_date
                FROM projects  
                ORDER BY end_date
        ) AS CTE3
        WHERE next_start_date != end_date
)

SELECT start_date, end_date
    FROM CTE
    JOIN CTE2
    USING (rn)
    ORDER BY (end_date - start_date), start_date;