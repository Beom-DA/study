-- https://school.programmers.co.kr/learn/courses/30/lessons/77487



SELECT id, name, host_id
    FROM places
    JOIN (
        SELECT host_id
            FROM places
            GROUP BY host_id
            HAVING COUNT(host_id) > 1    
    ) AS CTE
    USING (host_id)
    ORDER BY id;