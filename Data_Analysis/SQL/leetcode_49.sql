-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/


WITH CTE AS(
    SELECT product_id, SUM(unit)
        FROM orders
        WHERE EXTRACT (YEAR FROM order_date) = 2020
        AND   EXTRACT (MONTH FROM order_date) = 02
        GROUP BY product_id
)

SELECT product_name, sum AS unit
    FROM products
    JOIN CTE
    USING (product_id)
    WHERE sum >= 100;