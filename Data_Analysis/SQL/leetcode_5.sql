-- https://leetcode.com/problems/consecutive-numbers/description/

SELECT DISTINCT A.num as ConsecutiveNums
    FROM(
        SELECT num
            ,LAG(num) OVER(ORDER BY id) as pre_num_1
            ,LAG(num,2) OVER(ORDER BY id) as pre_num_2
            FROM logs
    ) AS A
    WHERE A.num = A.pre_num_1
    AND A.pre_num_1 = A.pre_num_2;


-- LAG()함수
-- 이전 N번 째 행의 값을 조회할 수 있는 함수
-- LAG(column_name, offset, default_value) OVER ( 
--     PARTITION BY ... 
--     ORDER BY ...
-- )
-- offset의 기본값은 1