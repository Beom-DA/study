--https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/


WITH CTE AS(
    SELECT *
        FROM trips
        JOIN drivers
        USING (driver_id)
),
driver AS(
    SELECT DISTINCT driver_id
        FROM trips t1
        JOIN (
            SELECT DISTINCT driver_id
                FROM trips t2
                WHERE EXTRACT(MONTH FROM trip_date) < 7
        )
        USING (driver_id)
        WHERE EXTRACT(MONTH FROM trip_date) > 6
),
calculated AS(
    SELECT driver_id, driver_name,
        ROUND(AVG(distance_km / fuel_consumed) FILTER(WHERE EXTRACT(MONTH FROM trip_date) < 7), 2) AS first_half_avg,
        ROUND(AVG(distance_km / fuel_consumed) FILTER(WHERE EXTRACT(MONTH FROM trip_date) > 6), 2) AS second_half_avg,
        ROUND(AVG(distance_km / fuel_consumed) FILTER(WHERE EXTRACT(MONTH FROM trip_date) > 6) -
        AVG(distance_km / fuel_consumed) FILTER(WHERE EXTRACT(MONTH FROM trip_date) < 7), 2) AS efficiency_improvement
        FROM CTE
        JOIN driver
        USING (driver_id)
        GROUP BY driver_id, driver_name
        ORDER BY efficiency_improvement DESC, driver_name
)

SELECT *
    FROM calculated
    WHERE efficiency_improvement > 0;