-- https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true



SELECT DISTINCT F1.x, F1.y
    FROM (
        SELECT *, ROW_NUMBER() OVER() AS rn
            FROM functions        
    ) AS F1,
    (
        SELECT *, ROW_NUMBER() OVER() AS rn
            FROM functions    
    ) AS F2
    WHERE F1.rn != F2.rn AND
    (F1.x = F2.y AND F1.y = F2.x) AND F1.x <= F1.y
    ORDER BY F1.x