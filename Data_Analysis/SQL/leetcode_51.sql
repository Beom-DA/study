-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

SELECT unique_id, name
    FROM employees
    LEFT JOIN employeeuni
    USING (id);