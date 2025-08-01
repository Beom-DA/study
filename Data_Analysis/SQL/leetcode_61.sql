-- https://leetcode.com/problems/find-students-who-improved/description/


-- 데이터가 한개 짜리 지우기
WITH CTE AS(
   SELECT *
        FROM scores S
        JOIN(
            SELECT student_id, subject
                FROM scores
                GROUP BY student_id, subject
                HAVING COUNT(*) > 1
        )
        USING (student_id, subject)
),

-- 3개 이상인거 latest 랑 first 구분해서 두개만 남기기

CTE_min AS(
    SELECT student_id, subject, MIN(exam_date) AS exam_date
        FROM CTE
        GROUP BY student_id, subject
),
CTE_max AS(
    SELECT student_id, subject, MAX(exam_date) AS exam_date
        FROM CTE
        GROUP BY student_id, subject
),

CTE_min_final AS(
    SELECT student_id, subject, score AS first_score
        FROM CTE
        JOIN CTE_min
        USING (student_id, subject, exam_date)
),
CTE_max_final AS(
    SELECT student_id, subject, score AS latest_score
        FROM CTE
        JOIN CTE_max
        USING (student_id, subject, exam_date)
)

-- latest 와 first 합쳐서 결과 출력

SELECT *
    FROM CTE_min_final A
    JOIN CTE_max_final B
    USING (student_id, subject)
    WHERE first_score < latest_score
    ORDER BY student_id, subject;



-- 다른 사람의 쿼리

with t1 as (
    -- first & last score of each unit
select
    distinct student_id, s.subject,
    first_value(score) over(partition by student_id, s.subject order by exam_date) as "first_score",
    first_value(score) over(partition by student_id, s.subject order by exam_date desc) as "latest_score"
from Scores as s
)

select
    student_id, t1.subject,
    first_score, latest_score
from t1
where first_score < latest_score
order by 1, 2


-- first_value() 라는 함수가 있는지 처음 알았다.