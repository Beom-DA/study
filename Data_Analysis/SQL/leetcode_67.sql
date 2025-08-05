-- https://leetcode.com/problems/seasonal-sales-analysis/description/



WITH CTE AS(
    SELECT *,
        CASE
            WHEN EXTRACT (month FROM sale_date) BETWEEN 3 AND 5 THEN 'Spring'
            WHEN EXTRACT (month FROM sale_date) BETWEEN 6 AND 8 THEN 'Summer'
            WHEN EXTRACT (month FROM sale_date) BETWEEN 9 AND 11 THEN 'Fall'
            ELSE 'Winter'
        END AS season,
        quantity * price AS total_price
        FROM sales
        JOIN products
        USING (product_id)
)

SELECT  DISTINCT ON (season) season, category, SUM(quantity) AS total_quantity, SUM(total_price) AS total_revenue
    FROM CTE
    GROUP BY season, category
    ORDER BY season, total_quantity DESC, total_revenue DESC