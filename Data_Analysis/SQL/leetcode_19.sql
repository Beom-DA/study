-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

WITH CTE AS(
    SELECT customer_number, COUNT(customer_number) AS count
    FROM orders
    GROUP BY customer_number
    ORDER BY count DESC
)

SELECT customer_number
    FROM CTE
    limit 1;


-- 다른 사람이 푼 쿼리
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
-- order by에 count를 쓸 수 있는지 처음 알았다.