-- https://leetcode.com/problems/classes-with-at-least-5-students/description/

WITH CTE as(
    SELECT class, COUNT(class)
        FROM courses
        GROUP BY class
        ORDER BY COUNT(class) DESC
)

SELECT CTE.class
    FROM CTE
    WHERE CTE.count > 4;