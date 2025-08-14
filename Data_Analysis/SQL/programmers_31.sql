-- https://school.programmers.co.kr/learn/courses/30/lessons/298519



SELECT COUNT(*) AS fish_count, MAX(length) AS max_length, fish_type
    FROM fish_info
    JOIN (
        SELECT fish_type
            FROM (
                SELECT fish_type, COALESCE(length, 10) AS length
                    FROM fish_info
            ) AS F
            GROUP BY fish_type
            HAVING AVG(length) >= 33    
    ) AS CTE
    USING (fish_type)
    GROUP BY fish_type
    ORDER BY fish_type;