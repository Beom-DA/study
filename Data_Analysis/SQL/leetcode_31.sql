-- https://leetcode.com/problems/customers-who-bought-all-products/description/

WITH CTE AS(
    SELECT DISTINCT *
        FROM customer
),
CTE2 AS(
    SELECT customer_id, COUNT(customer_id) AS C
        FROM CTE
        GROUP BY customer_id
)

SELECT customer_id
    FROM CTE2
    WHERE C IN (SELECT COUNT(*) FROM product);



-- 다른 사람의 쿼리
select c.customer_id from Customer c 
join Product p on c.product_key = p.product_key
group by c.customer_id
having count(distinct c.product_key) = (select count(*) from product)