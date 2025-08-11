-- https://school.programmers.co.kr/learn/courses/30/lessons/131537


SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, user_id, sales_amount
    FROM online_sale
    WHERE EXTRACT(month FROM sales_date) = 3
    
UNION ALL

SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, NULL AS user_id , sales_amount
    FROM offline_sale
    WHERE EXTRACT(month FROM sales_date) = 3
    ORDER BY sales_date, product_id, user_id;