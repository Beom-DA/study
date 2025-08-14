-- https://school.programmers.co.kr/learn/courses/30/lessons/164671



SELECT CONCAT('/home/grep/src/', board_id, '/', file_id, file_name, file_ext) AS file_path
    FROM used_goods_file
    JOIN (
        SELECT board_id
            FROM used_goods_board
            ORDER BY views DESC
            LIMIT 1    
    ) AS CTE
    USING (board_id)
    ORDER BY file_id DESC;