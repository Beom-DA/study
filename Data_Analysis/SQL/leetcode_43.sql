-- https://leetcode.com/problems/monthly-transactions-i/description/

WITH CTE AS(
    SELECT id, country, state, amount, TO_CHAR(trans_date, 'YYYY-MM') AS trans_date
        FROM transactions
)

SELECT
    trans_date AS month,
    country,
    COUNT(*) AS trans_count,
    COUNT(*) FILTER (WHERE state = 'approved') AS approved_count,
    COALESCE(SUM(amount), 0) AS trans_total_amount,
    COALESCE(SUM(amount) FILTER (WHERE state = 'approved'), 0) AS approved_total_amount

    FROM CTE
    GROUP BY trans_date, country;




-- 다른 사람이 만든 쿼리

SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month,
            country,
            COUNT(*) AS trans_count, 
            COUNT(state) FILTER (WHERE state = 'approved') AS approved_count, 
            SUM(amount) AS trans_total_amount,
            COALESCE(SUM(amount) FILTER (WHERE state = 'approved'), 0) AS approved_total_amount
FROM Transactions
GROUP BY "month", country;


-- 의문점 : GROUP BY 절이 먼저 실행된 뒤에 SELECT 문이 실행되는데 어떻게 SELECT 문에 있는 'month'를 groupby에 쓸 수 있는거지?
-- 답변 :
-- PostgreSQL은 GROUP BY에서 SELECT 절의 alias를 참조하는 것을 허용한다.
-- 이는 SQL 표준에서는 금지되었지만, PostgreSQL의 편의 기능으로 존재한다.