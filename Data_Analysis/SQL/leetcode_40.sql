-- https://leetcode.com/problems/product-price-at-a-given-date/

WITH CTE AS(
    SELECT DISTINCT product_id
        FROM products
),
CTE2 AS(
    SELECT product_id, MAX(change_date) AS change_date
        FROM products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
        HAVING MAX(change_date) <= '2019-08-16'
),
CTE3 AS(
    SELECT product_id, new_price AS price
    FROM products
    WHERE (product_id,change_date) IN (SELECT product_id,change_date FROM CTE2)
)

SELECT product_id, COALESCE(price,10) AS price
    FROM CTE
    LEFT JOIN CTE3
    USING (product_id);




