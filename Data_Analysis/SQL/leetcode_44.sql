-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/

 WITH CTE AS(
    SELECT *, SUM(weight) OVER(ORDER BY turn), LAG(person_name) OVER(ORDER BY turn)
        FROM Queue
)

SELECT person_name
    FROM CTE
    WHERE sum <= 1000
    ORDER BY turn DESC
    LIMIT 1;