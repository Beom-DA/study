-- https://school.programmers.co.kr/learn/courses/30/lessons/299308



WITH CTE AS(
    SELECT *,
        CASE
            WHEN month BETWEEN 1 AND 3 THEN '1Q'
                ELSE
                    CASE
                        WHEN month BETWEEN 4 AND 6 THEN '2Q'
                        ELSE
                            CASE 
                                WHEN month BETWEEN 7 AND 9 THEN '3Q'
                                ELSE '4Q'
                            END
                    END
        END AS quarter
        FROM(
            SELECT id, EXTRACT(month FROM differentiation_date) AS month
                FROM ecoli_data
        ) AS E
)

SELECT quarter, count(*) AS ecoli_count
    FROM CTE
    GROUP BY quarter
    ORDER BY quarter;