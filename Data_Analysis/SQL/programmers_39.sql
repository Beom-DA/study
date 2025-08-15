-- https://school.programmers.co.kr/learn/courses/30/lessons/131117



SELECT product_id, product_name, SUM(amount) * price AS total_sales
    FROM food_order
    JOIN food_product
    USING (product_id)
    WHERE DATE_FORMAT(produce_date, '%Y-%m') = '2022-05'
    GROUP BY product_id, product_name
    ORDER BY total_sales DESC, product_id;