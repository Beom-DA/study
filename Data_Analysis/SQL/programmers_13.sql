-- https://school.programmers.co.kr/learn/courses/30/lessons/301650


WITH RECURSIVE CTE AS(
    SELECT id, parent_id, 1 AS generation
        FROM ecoli_data
        WHERE parent_id IS NULL
    
    UNION ALL
    
    SELECT E.id AS id, E.parent_id AS parent_id, CTE.generation + 1 AS generation
        FROM CTE
        JOIN ecoli_data E
        ON CTE.id = E.parent_id
)

SELECT id
    FROM CTE
    WHERE generation = 3
    ORDER BY id;