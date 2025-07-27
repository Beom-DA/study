-- https://leetcode.com/problems/immediate-food-delivery-ii/

-- 첫 주문 정보
WITH CTE AS(
    SELECT customer_id, MIN(order_date) AS order_date
        FROM delivery
        GROUP BY customer_id
)

-- 
SELECT ROUND(COUNT(*) FILTER (WHERE order_date = customer_pref_delivery_date) / COUNT(*)::DECIMAL, 4) * 100 AS immediate_percentage
    FROM delivery
    JOIN CTE
    USING (order_date, customer_id);