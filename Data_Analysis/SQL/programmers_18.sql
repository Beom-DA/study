-- https://school.programmers.co.kr/learn/courses/30/lessons/299305



SELECT id, IFNULL(CTE.count, 0) AS child_count
    FROM ecoli_data
    LEFT JOIN (
        SELECT parent_id AS id, COUNT(*) AS count
            FROM ecoli_data
            WHERE parent_id IN (SELECT id FROM ecoli_data)
            GROUP BY parent_id 
    ) AS CTE
    USING (id)