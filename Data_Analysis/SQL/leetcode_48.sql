-- https://leetcode.com/problems/restaurant-growth/


WITH CTE AS(
    SELECT visited_on , SUM(amount) AS amount,
        LAG(visited_on, 6) OVER(ORDER BY visited_on) AS LAG
        FROM customer
        GROUP BY visited_on
        ORDER BY visited_on
),
CTE2 AS(
    SELECT visited_on,
        SUM(amount) OVER(ORDER BY visited_on  ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS total_amount
        FROM CTE
        GROUP BY visited_on, amount
)

SELECT visited_on, total_amount AS amount, ROUND(total_amount / 7.0, 2) AS average_amount
    FROM CTE2
    JOIN CTE
    USING (visited_on)
    WHERE lag IS NOT NULL


-- SUM 함수의 OVER() 인자에 이전 몇 행까지의 데이터를 더한다 라는 문법을 알게 됐다.
