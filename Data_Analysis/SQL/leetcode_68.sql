-- https://leetcode.com/problems/find-consistently-improving-employees/


WITH CTE1 AS( -- review가 2개 이하인 employee_id에 대해 review 전부 삭제 
    SELECT employee_id
        FROM performance_reviews
        GROUP BY employee_id
        HAVING COUNT(*) > 2
),
CTE2 AS(
    SELECT employee_id, review_date, rating,
        ROW_NUMBER() OVER(PARTITION BY employee_id ORDER BY review_date DESC)
        FROM performance_reviews
        JOIN CTE1
        USING (employee_id) 
),
CTE3 AS(
    SELECT employee_id,
        LAG(employee_id) OVER() AS prev_employee_id,
        LAG(rating) OVER() AS prev_rating,
        rating,
        row_number,
        LAG(rating) OVER() - rating AS difference
        FROM CTE2
        WHERE row_number < 4
),
CTE4 AS(
    SELECT DISTINCT employee_id
        FROM CTE3
        WHERE employee_id = prev_employee_id
        AND prev_rating <= rating     
)

SELECT employee_id, name, SUM(difference) FILTER (WHERE employee_id = prev_employee_id) AS improvement_score
    FROM CTE3
    JOIN employees
    USING (employee_id)
    WHERE employee_id NOT IN (SELECT * FROM CTE4)
    GROUP BY employee_id, name
    ORDER BY improvement_score DESC, name;