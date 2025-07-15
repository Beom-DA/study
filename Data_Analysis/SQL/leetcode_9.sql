-- https://leetcode.com/problems/department-top-three-salaries/description/

-- DENSE_RANK()를 사용하면 될 것 같은 느낌
SELECT R.department Department, R.employee Employee, R.s Salary
    FROM(
        SELECT D.name department, E.name employee, E.salary s
            , DENSE_RANK() OVER(PARTITION BY D.name ORDER BY E.salary DESC) RANK
            FROM employee E
            JOIN department D
            ON E.departmentid = D.id
    ) AS R
    WHERE R.RANK < 4;