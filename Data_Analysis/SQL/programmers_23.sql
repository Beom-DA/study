-- https://school.programmers.co.kr/learn/courses/30/lessons/151139



SELECT MONTH(start_date) AS month, car_id, count(*) AS records
    FROM car_rental_company_rental_history
    JOIN(
        SELECT car_id
            FROM car_rental_company_rental_history
            WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
            GROUP BY car_id
            HAVING COUNT(car_id) > 4  
    ) AS CTE
    USING (car_id)
    WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY month, car_id
    ORDER BY month, car_id DESC