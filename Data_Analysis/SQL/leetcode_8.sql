-- https://leetcode.com/problems/department-highest-salary/description/

-- Write your PostgreSQL query statement below

SELECT D.name Department, E.name Employee, E.salary Salary
    FROM employee E
    JOIN department D
    ON E.departmentid = D.id
    WHERE (D.name, E.salary) in(
        SELECT B.name AS Department, MAX(A.salary)
            FROM employee AS A
            LEFT JOIN department AS B
            ON A.departmentID = B.id
        GROUP BY B.name
    );

-- WHERE문 안에 in 구문이 있는지 처음 알았다.