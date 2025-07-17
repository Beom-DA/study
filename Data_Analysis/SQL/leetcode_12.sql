-- https://leetcode.com/problems/trips-and-users/description/

SELECT T.request_at AS "Day", ROUND(COUNT(*) FILTER(WHERE T.status != 'completed')::DECIMAL / COUNT(*)::DECIMAL, 2) AS "Cancellation Rate"
    FROM trips T
    JOIN users U1
    ON T.client_id = U1.users_id
    JOIN users U2
    ON T.driver_id = U2.users_id
    WHERE U1.banned = 'No' AND U2.banned = 'No'
    AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY T.request_at
    ORDER BY T.request_at;

-- 이중 JOIN문을 처음 다뤄봤는데, 구글링을 하지 않아도 될 정도로 그리 어려운건 아니었다.
-- 이 문제를 통해 새로 얻은 지식은 DECIMAL 사용법, ROUND 사용법, FILTER 사용법이다.
-- 사소한 지식이지만 AS 구문을 사용할때 큰 따옴표("")를 사용하는 방법도 새로 익혔다.