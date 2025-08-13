-- https://school.programmers.co.kr/learn/courses/30/lessons/62284



SELECT DISTINCT cart_id
    FROM cart_products 
    WHERE cart_id IN (
        SELECT cart_id
            FROM cart_products
            WHERE name = 'Yogurt'    
    )
    AND name = 'Milk'
    ORDER BY cart_id;


-- 다른 사람의 쿼리(신박한 방법)
SELECT CART_ID 
    FROM CART_PRODUCTS 
    GROUP BY CART_ID 
    HAVING MAX(NAME = 'Milk') AND MAX(NAME = 'Yogurt');