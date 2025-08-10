-- https://school.programmers.co.kr/learn/courses/30/lessons/151141


WITH CTE AS(
    SELECT daily_fee, history_id, duration_type, discount_rate, (DATEDIFF(end_date, start_date)+1) AS 대여기간
        FROM car_rental_company_car
        LEFT JOIN car_rental_company_rental_history
        USING (car_id)
        LEFT JOIN car_rental_company_discount_plan
        USING (car_type)
        WHERE car_type = '트럭'
),
CTE2 AS(
    SELECT  *,
        CASE
            WHEN 대여기간 >= 90 THEN '90일 이상'
            WHEN 대여기간 >= 30 THEN '30일 이상'
            WHEN 대여기간 >= 7 THEN '7일 이상'
        END AS duration
        FROM CTE
),
CTE3 AS (
    SELECT daily_fee, history_id, duration_type, discount_rate, 대여기간
        FROM CTE2
        WHERE duration_type = duration
),
CTE4 AS (
    SELECT DISTINCT daily_fee, history_id, 대여기간
        FROM CTE2
        WHERE 대여기간 < 7
)

SELECT history_id, CONVERT((daily_fee * 대여기간 * (1-discount_rate/100)), UNSIGNED) AS fee
    FROM CTE3

UNION ALL

SELECT history_id, CONVERT((daily_fee * 대여기간), UNSIGNED) AS fee
    FROM CTE4
    ORDER BY fee DESC, history_id DESC;