-- https://leetcode.com/problems/group-sold-products-by-the-date/


WITH CTE AS(
    SELECT DISTINCT *
        FROM activities
)

SELECT sell_date, COUNT(*) AS num_sold, STRING_AGG(product, ',' ORDER BY product)  AS products
    FROM CTE
    GROUP BY sell_date
    ORDER BY sell_date;


-- STRING_AGG(column_name, delimiter ORDER BY order)
-- 같은 행, 같은 열에 원하는 데이터를 원하는 구분자(delimiter)로 이어서 나타내는 방법