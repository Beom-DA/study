-- https://school.programmers.co.kr/learn/courses/30/lessons/284528



SELECT E.emp_no, E.emp_name,
    CASE
        WHEN score >= 96 THEN 'S'
        ELSE
            CASE
                WHEN score >= 90 THEN 'A'
                ELSE
                    CASE
                        WHEN score >= 80 THEN 'B'
                        ELSE 'C'
                    END
            END
    END AS grade,
    CASE
        WHEN score >= 96 THEN sal * 0.2
        ELSE
            CASE
                WHEN score >= 90 THEN sal * 0.15
                ELSE
                    CASE
                        WHEN score >= 80 THEN sal * 0.1
                        ELSE 0
                    END
            END
    END AS bonus
    FROM hr_employees E
    JOIN hr_grade G
    USING (emp_no)
    ORDER BY E.emp_no;