-- https://leetcode.com/problems/project-employees-i

SELECT project_id, ROUND(AVG(experience_years)::DECIMAL,2) AS average_years
    FROM project P
    JOIN employee E
    USING (employee_id)
    GROUP BY project_id;