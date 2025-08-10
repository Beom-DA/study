-- https://school.programmers.co.kr/learn/courses/30/lessons/276034


SELECT DISTINCT id, email, first_name, last_name 
    FROM developers
    LEFT JOIN skillcodes
    ON skill_code & code = code
    WHERE name = 'c#' OR name = 'Python'
    ORDER BY id;