-- https://leetcode.com/problems/confirmation-rate/


WITH CTE AS(
    SELECT user_id, COALESCE(COUNT(action) FILTER (WHERE action = 'confirmed'), 0) AS confirmed, COUNT(*) AS total
        FROM confirmations
        GROUP BY user_id
)

SELECT user_id, COALESCE(ROUND(confirmed / total::DECIMAL, 2), 0) AS confirmation_rate
    FROM signups
    LEFT JOIN CTE
    USING (user_id);