-- https://leetcode.com/problems/find-overbooked-employees/description/


WITH CTE AS(
    SELECT employee_id, employee_name, department, SUM(duration_hours)
        FROM meetings
        JOIN employees
        USING (employee_id)
        GROUP BY employee_id, DATE_TRUNC('week', meeting_date)::DATE, employee_name, department
)

SELECT employee_id, employee_name, department, COUNT(sum) FILTER(WHERE sum > 20) AS meeting_heavy_weeks
    FROM CTE
    GROUP BY employee_id, employee_name, department
    HAVING COUNT(sum) FILTER(WHERE sum > 20) > 1
    ORDER BY meeting_heavy_weeks DESC, employee_name;