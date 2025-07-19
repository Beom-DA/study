-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

WITH CTE as(
    SELECT managerId
        FROM employee
        GROUP BY managerId
        HAVING COUNT(*) > 4
)

SELECT E.name
    FROM employee E
    JOIN CTE
    ON E.id = CTE.managerId;