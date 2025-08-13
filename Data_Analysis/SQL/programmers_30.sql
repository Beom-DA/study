-- https://school.programmers.co.kr/learn/courses/30/lessons/131532



SELECT EXTRACT(year FROM sales_date) AS year, EXTRACT(month FROM sales_date) AS month, gender,
    COUNT(DISTINCT user_id) AS users
    FROM user_info
    JOIN online_sale
    USING (user_id)
    WHERE gender IS NOT null
    GROUP BY EXTRACT(year FROM sales_date), EXTRACT(month FROM sales_date), gender
    ORDER BY year, month, gender;