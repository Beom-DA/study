-- https://school.programmers.co.kr/learn/courses/30/lessons/131534



SELECT  
    YEAR(SALES_DATE) AS year_SALES_DATE,
    MONTH(SALES_DATE) AS month_SALES_DATE,
    COUNT(DISTINCT u.user_id) AS purchased_users,
    ROUND(
        COUNT(DISTINCT u.user_id) * 1.0 / (SELECT COUNT(*) FROM USER_INFO WHERE joined LIKE '2021%'),
        1
    ) AS purchased_ratio
FROM user_info u
JOIN online_sale USING (user_id)
WHERE EXTRACT(YEAR FROM joined) = 2021
GROUP BY YEAR(sales_date), MONTH(sales_date)
ORDER BY year_SALES_DATE, month_SALES_DATE;