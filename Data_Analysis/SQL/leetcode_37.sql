-- https://leetcode.com/problems/sales-analysis-iii/

WITH CTE AS(
    SELECT DISTINCT product_id
        FROM sales
        WHERE sale_date < '2019-01-01'
        OR sale_date > '2019-03-31'
)

SELECT DISTINCT product_id, product_name
    FROM product
    JOIN sales
    USING (product_id)
    WHERE product_id NOT IN (SELECT * FROM CTE);