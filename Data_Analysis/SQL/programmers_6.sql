-- https://school.programmers.co.kr/learn/courses/30/lessons/276035



WITH CTE AS(
    SELECT id, email, first_name, last_name, category
        FROM developers D
        JOIN skillcodes S
        ON D.skill_code & S.code = S.code
)

SELECT DISTINCT id, email, first_name, last_name
    FROM CTE
    WHERE category = 'Front End'
    ORDER BY id;