-- https://school.programmers.co.kr/learn/courses/30/lessons/276036


WITH CTE AS (
    SELECT id, email,
        GROUP_CONCAT(name) AS name,
        GROUP_CONCAT(category) AS category
        FROM developers
        JOIN skillcodes
        ON (developers.skill_code & skillcodes.code) > 0
        GROUP BY id, email
        ORDER BY id
),
CTE2 AS (
    SELECT 
        CASE
            WHEN name LIKE '%Python%' AND category LIKE '%Front End%' THEN 'A'
                ELSE
                    CASE
                        WHEN name LIKE '%C#%' THEN 'B'
                        ELSE
                            CASE
                                WHEN category LIKE '%Front END%' THEN 'C'
                                ELSE 'D'
                            END
                    END
        END AS grade,
        id, email
        FROM CTE
)

SELECT grade, id, email
    FROM CTE2
    WHERE grade != 'D'
    ORDER BY grade, id;



-- 이진수들 다루는 문제를 처음 풀어봤다
-- (developers.skill_code & skillcodes.code) > 0
-- integer를 굳이 binary code로 바꾸지 않아도 '&'와'|'를 사용하면 알아서 binary 연산을 해준다.