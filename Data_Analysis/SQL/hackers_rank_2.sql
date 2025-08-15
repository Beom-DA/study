-- https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true




SELECT N,
    CASE
        WHEN P IS null THEN 'Root'
        ELSE
            CASE
                WHEN N IN (SELECT P FROM bst) THEN 'Inner'
                ELSE 'Leaf'
            END
    END AS state
    FROM bst
    ORDER BY N