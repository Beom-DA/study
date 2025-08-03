-- https://leetcode.com/problems/find-invalid-ip-addresses/


-- '.' 으로 나눈 리스트 만들기
-- 0이 아닌 숫자 앞에 0이 있으면 invalid
-- 리스트의 요소가 4개가 아니면 invalid
-- 리스트의 요소가 255보다 큰게 있으면 invalid

WITH CTE AS(
    SELECT log_id, STRING_TO_ARRAY(ip, '.') AS ip
        FROM logs        
),
CTE2 AS(
    SELECT log_id, UNNEST(STRING_TO_ARRAY(ip, '.'))::INTEGER AS ip
        FROM logs 
),
CTE3 AS(
    SELECT log_id, UNNEST(STRING_TO_ARRAY(ip, '.')) AS ip
        FROM logs
),
CTE4 AS(
    -- 리스트의 요소가 4개아 아닌 ip
    SELECT log_id
        FROM CTE
        WHERE CARDINALITY(ip) != 4

    UNION ALL
    -- 255 보다 큰 값이 있는 ip
    SELECT log_id
        FROM CTE2
        WHERE ip > 255

    UNION ALL
    -- 0이 아닌 숫자 앞에 0이 있는 ip
    SELECT log_id
        FROM CTE3
        WHERE ip ~ '^0+[1-9]+'
),
CTE5 AS(
    SELECT DISTINCT log_id
        FROM CTE4
)

SELECT ip, COUNT(*) AS invalid_count
    FROM logs
    JOIN CTE5
    USING (log_id)
    GROUP BY ip
    ORDER BY invalid_count DESC, ip DESC;