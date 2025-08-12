-- https://school.programmers.co.kr/learn/courses/30/lessons/293261



SELECT F.id, CTE.fish_name, CTE.length
    FROM fish_info F
    JOIN (
        SELECT fish_type, fish_name, MAX(length) AS length
            FROM fish_info
            JOIN fish_name_info
            USING (fish_type)
            GROUP BY fish_type, fish_name
    ) AS CTE
    USING (fish_type, length)
    ORDER BY id;