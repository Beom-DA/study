-- https://leetcode.com/problems/employee-bonus/

WITH ETC AS(
    SELECT *
        FROM employee E
        LEFT JOIN bonus B
        ON E.empId = B.empId
        WHERE b.bonus < 1000
        OR b.bonus IS NULL
)

SELECT ETC.name, ETC.bonus
    FROM ETC;