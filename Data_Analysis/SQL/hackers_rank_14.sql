-- 



SELECT f1.x, f1.y
    FROM functions f1, functions f2
    WHERE (f1.x = f2.y AND f1.y = f2.x) AND f1.x <= f1.y
    ORDER BY f1.x
    
-- row_number 활용해보기