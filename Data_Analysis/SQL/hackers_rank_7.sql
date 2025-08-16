-- https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true



SELECT 
    CASE
        WHEN marks BETWEEN 70 AND 100 THEN name
        ELSE NULL
    END AS name,
    CASE
        WHEN marks BETWEEN 0 AND 9 THEN 1
        ELSE
            CASE
                WHEN marks BETWEEN 10 AND 19 THEN 2
                ELSE
                    CASE
                        WHEN marks BETWEEN 20 AND 29 THEN 3
                        ELSE
                            CASE
                                WHEN marks BETWEEN 30 AND 39 THEN 4
                                ELSE
                                    CASE
                                        WHEN marks BETWEEN 40 AND 49 THEN 5
                                        ELSE
                                            CASE
                                                WHEN marks BETWEEN 50 AND 59 THEN 6
                                                ELSE
                                                    CASE
                                                        WHEN marks BETWEEN 60 AND 69 THEN 7
                                                        ELSE
                                                            CASE
                                                                WHEN marks BETWEEN 70 AND 79 THEN 8
                                                                ELSE
                                                                    CASE
                                                                        WHEN marks BETWEEN 80 AND 89 THEN 9
                                                                        ELSE 10      
                                                                    END
                                                            END
                                                    END                
                                            END
                                    END
                            END
                    END
            END
    END AS grade,
    marks
    FROM students
    ORDER BY grade DESC, name, grade DESC, marks;