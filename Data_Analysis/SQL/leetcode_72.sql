-- https://leetcode.com/problems/find-students-with-study-spiral-pattern/


-- 수업이 6개보다 작은 학생들은 제거
WITH CTE AS(
    SELECT *,
        LAG(session_date) OVER() AS prev_session_date
        FROM study_sessions
        JOIN (
            SELECT student_id
                FROM study_sessions
                GROUP BY student_id
                HAVING COUNT(*) > 5
        )
        USING (student_id)
        JOIN students
        USING (student_id)    
),

-- 강의를 2일 이상 스킵한 경우 제거
CTE1 AS(
    SELECT *
        FROM CTE
        WHERE student_id NOT IN (
            SELECT student_id
                FROM CTE
                WHERE session_date - prev_session_date > 2
        )    
),

-- 한 사이클에 3과목 이상인지 확인
CTE2 AS(
    SELECT student_id, subject, session_date, hours_studied
        FROM CTE1
        JOIN (
            SELECT student_id
                FROM (
                    SELECT student_id, COUNT(*)
                        FROM (
                        SELECT student_id, subject
                            FROM CTE1
                            GROUP BY student_id, subject  
                        )
                        GROUP BY student_id
                )
                WHERE count > 2        
        )
        USING (student_id)    
),

-- 2사이클을 만족하는지 확인
CTE3 AS(
    SELECT *
        FROM CTE2
        WHERE student_id NOT IN(
            SELECT student_id
                FROM CTE1
                GROUP BY student_id, subject
                HAVING COUNT(*) < 2        
        )    
),

-- cylce length
CTE4 AS(
    SELECT student_id, COUNT(*)
        FROM (
            SELECT student_id, COUNT(*)
                FROM CTE3
                GROUP BY student_id, subject        
        )
        GROUP BY student_id    
),
CTE5 AS(
    SELECT student_id, SUM(hours_studied)
        FROM CTE3
        GROUP BY student_id     
)

SELECT DISTINCT student_id, student_name, major, count AS cycle_length, sum AS total_study_hours
    FROM CTE3
    JOIN CTE4
    USING (student_id)
    JOIN CTE5
    USING (student_id)
    JOIN students
    USING (student_id)
    ORDER BY cycle_length DESC, total_study_hours DESC;
       
    



