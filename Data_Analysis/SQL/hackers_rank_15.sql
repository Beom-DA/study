-- https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true



SET cte_max_recursion_depth = 1000;

WITH RECURSIVE CTE AS(
    SELECT 2 AS init
    UNION ALL
    SELECT init + 1
        FROM CTE
        WHERE init < 1000
)

SELECT GROUP_CONCAT(init separator '&')
    FROM CTE C1
    WHERE NOT EXISTS(
        SELECT 1
            FROM CTE C2
            WHERE C1.init > C2.init
            AND C1.init % C2.init = 0
    )