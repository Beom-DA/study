-- https://leetcode.com/problems/product-sales-analysis-iii/


WITH CTE AS(
    SELECT product_id, MIN(year)
        FROM sales
        GROUP BY product_id
        
)

SELECT product_id, year AS first_year, quantity, price
    FROM sales
    WHERE (product_id, year) IN (SELECT * FROM CTE)
    ORDER BY first_year;
