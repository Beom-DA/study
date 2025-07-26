-- https://leetcode.com/problems/market-analysis-i/

WITH CTE AS(
    SELECT *
        FROM orders
        LEFT JOIN users
        ON users.user_id = orders.buyer_id
        LEFT JOIN items
        USING (item_id)
),
CTE2 AS(
   SELECT buyer_id AS user_id, 
        CASE
            WHEN (COUNT(*) FILTER(WHERE EXTRACT(YEAR FROM order_date)::INT = 2019)) = 0 THEN 0
            ELSE (COUNT(*) FILTER(WHERE EXTRACT(YEAR FROM order_date)::INT = 2019))
        END AS orders_in_2019
        FROM CTE
        GROUP BY buyer_id
)

SELECT user_id AS buyer_id, join_date, COALESCE(orders_in_2019,0) AS orders_in_2019
    FROM users
    LEFT JOIN CTE2
    USING (user_id);

-- COALESCE(column_name, 0) 을 처음 다뤄봤다.
-- 'column_name'에 해당하는 값이 null일 경우 0을 반환하는 함수
-- 발음은 '코얼레스크' 라고 한다.