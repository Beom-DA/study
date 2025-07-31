-- https://leetcode.com/problems/group-sold-products-by-the-date/


WITH CTE AS(
    SELECT DISTINCT *
        FROM activities
)

SELECT sell_date, COUNT(*) AS num_sold, STRING_AGG(product, ',' ORDER BY product)  AS products
    FROM CTE
    GROUP BY sell_date
    ORDER BY sell_date;