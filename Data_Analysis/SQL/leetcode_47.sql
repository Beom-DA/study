-- https://leetcode.com/problems/students-and-examinations/


WITH CTE AS(
    SELECT *
        FROM students
        CROSS JOIN subjects
)

SELECT CTE.student_id, CTE.student_name, CTE.subject_name, COALESCE(COUNT(E.student_id), 0) AS attended_exams
    FROM CTE
    LEFT JOIN examinations E
    ON CTE.student_id = E.student_id and CTE.subject_name = E.subject_name
    GROUP BY CTE.student_id, CTE.student_name, CTE.subject_name
    ORDER BY CTE.student_id, CTE.subject_name;

-- CROSS JOIN
-- 두 테이블의 모든 행을 서로 조합해서 결과를 생성하는 조인
-- A 테이블의 행 수 × B 테이블의 행 수 만큼 결과가 나옴