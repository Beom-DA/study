-- https://leetcode.com/problems/human-traffic-of-stadium/

WITH CTE as(
        SELECT *
            , ROW_NUMBER() OVER(ORDER BY id) AS R1
            , id - ROW_NUMBER() OVER(ORDER BY id) AS R2
            FROM stadium
            WHERE people >= 100
),

CTE2 as(
    SELECT CTE.R2, COUNT(CTE.R2)
        FROM CTE
        GROUP BY CTE.R2
)

SELECT CTE.id, CTE.visit_date, CTE.people
    FROM CTE
    LEFT JOIN stadium
    ON CTE.id = stadium.id
    LEFT JOIN CTE2
    ON CTE.R2 = CTE2.R2
    WHERE count > 2;


-- 다른 사람의 쿼리
with visit_cte as (
    select id, visit_date, people,
    row_number() over () as row_num,
    id - row_number() over () as diff
    from Stadium
    where people >= 100
)
select id, visit_date, people from visit_cte where diff in(
    select diff from visit_cte
    group by diff
    having count(*) >= 3
);

-- in을 활용해서 문제를 풀어보는 습관을 들여봐야겠다.
-- 불필요한 join이 없다.