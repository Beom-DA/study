-- https://school.programmers.co.kr/learn/courses/30/lessons/301651


WITH RECURSIVE generation_tree AS(
    SELECT id, parent_id, 1 AS generation
        FROM ecoli_data
        WHERE parent_id IS NULL
    
    UNION ALL
    
    SELECT d1.id, d1.parent_id, g.generation + 1
        FROM ecoli_data d1
        JOIN generation_tree g ON d1.parent_id = g.id
),
statement AS (
    SELECT id,
        CASE
            WHEN parent_id IS NULL THEN 
                CASE
                    WHEN  id IN (SELECT parent_id FROM ecoli_data) THEN 'parent'
                    ELSE 'leaf'
                END
            ELSE
                CASE
                    WHEN id IN (SELECT parent_id FROM ecoli_data) THEN 'inner'
                    ELSE 'leaf'
                END
        END AS state
        FROM ecoli_data
)

SELECT count(*) AS count, generation
    FROM generation_tree
    JOIN statement
    USING (id)
    WHERE state = 'leaf'
    GROUP BY generation
    ORDER BY generation;