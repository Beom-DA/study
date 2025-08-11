-- https://school.programmers.co.kr/learn/courses/30/lessons/131530



WITH CTE AS(
SELECT product_id, FLOOR(price/10000) * 10000 AS price_group
    FROM product
)

SELECT price_group, count(*) AS products
    FROM CTE
    GROUP BY price_group
    ORDER BY price_group;