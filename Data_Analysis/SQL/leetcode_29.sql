-- https://leetcode.com/problems/exchange-seats

WITH CTE AS(
    SELECT *,
        LAG(student) OVER(ORDER BY id),
        LEAD(student) OVER(ORDER BY id)
    FROM seat
)

SELECT id,
    CASE
        WHEN id % 2 = 1 
        AND lead IS NOT NULL THEN lead

        WHEN id % 2 = 0 THEN lag

        ELSE student
    END as student
    FROM CTE;

-- 다른 사람의 쿼리
SELECT(
  CASE WHEN id % 2 = 1 and  id = (select max(id) from Seat) THEN id
  WHEN id % 2 = 1 THEN id + 1
  WHEN id % 2 = 0 THEN id - 1
  END ) AS id, student 
FROM Seat
ORDER BY id
-- 다음 행을 지정할 수 있는 방법이 있다는걸 처음 알았고
-- AS id, student 처럼 두 개의 열을 묶어서 가져올 수 있는 것도 처음 알았다.
