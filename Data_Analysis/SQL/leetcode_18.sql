-- https://leetcode.com/problems/investments-in-2016/

-- 내가 푼 쿼리
WITH CTE AS(
    SELECT lat, lon, COUNT(*) AS location_count
    FROM insurance
    GROUP BY lat, lon
),
CTE_2 AS(
    SELECT tiv_2015, COUNT(tiv_2015) AS tiv_count
    FROM insurance
    GROUP BY tiv_2015
)

SELECT ROUND(SUM(tiv_2016)::DECIMAL,2) AS tiv_2016
    FROM insurance AS I
    LEFT JOIN CTE
    ON I.lat = CTE.lat AND I.lon = CTE.lon
    LEFT JOIN CTE_2
    ON I.tiv_2015 = CTE_2.tiv_2015
    WHERE location_count < 2
    AND tiv_count > 1;



-- 다른 사람이 푼 쿼리
-- Write your PostgreSQL query statement below
SELECT ROUND(SUM(tiv_2016)::NUMERIC,2) AS tiv_2016 
    FROM Insurance 
    WHERE (tiv_2015) IN (
        SELECT tiv_2015 
            FROM Insurance 
            GROUP BY tiv_2015 
            HAVING COUNT(*) > 1
    ) 
    AND (lat, lon) IN (
        SELECT lat, lon 
        FROM Insurance 
        GROUP BY lat,lon 
        HAVING count(*) = 1
    )