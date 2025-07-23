-- https://leetcode.com/problems/biggest-single-number/

WITH CTE AS(
    SELECT *, COUNT(*) AS c
        FROM mynumbers
        GROUP BY num
)


    SELECT 
        CASE
            WHEN AVG(CTE.c) = 2 THEN null
            WHEN AVG(CTE.c) != 2 AND CTE.c = 1 THEN MAX(num)
        END AS num
        FROM CTE
        GROUP BY CTE.c
        ORDER BY num NULLS last
        limit 1;
    
    
-- order by 절에 nulls last를 하면 null이 맨 뒤로 가는 구문을 처음 접했다.


-- 또 다른 방법
select 
case when count(*)=1 then num
     else null
     end as num
from mynumbers
group by num
order by 1 desc nulls last
limit 1
