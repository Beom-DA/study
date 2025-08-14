-- https://school.programmers.co.kr/learn/courses/30/lessons/157340



SELECT DISTINCT car_id,
    CASE
        WHEN car_id IN (
            SELECT car_id
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                WHERE '2022-10-16' BETWEEN start_date AND end_date        
        ) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
    FROM car_rental_company_rental_history
    ORDER BY car_id DESC;