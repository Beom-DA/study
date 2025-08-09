-- https://school.programmers.co.kr/learn/courses/30/lessons/301647


WITH CTE AS(
    SELECT e1.id AS parent_id, e1.genotype AS parent_genotype, e2.id, e2.genotype
        FROM ecoli_data e1, ecoli_data e2
        WHERE e1.id = e2.parent_id
)

SELECT id, genotype, parent_genotype
    FROM CTE
    WHERE parent_genotype & genotype = parent_genotype
    ORDER BY id