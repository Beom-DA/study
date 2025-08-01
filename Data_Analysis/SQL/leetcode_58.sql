-- https://leetcode.com/problems/count-salary-categories/

WITH CTE AS(
    SELECT * FROM (VALUES ('High Salary'), ('Average Salary'), ('Low Salary')) AS t(category)
),
CTE2 AS(
    SELECT *,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income > 50000 THEN 'High Salary'
            ELSE 'Average Salary' 
        END AS category
        FROM accounts    
)

SELECT category, COUNT(CTE2.category) AS accounts_count
    FROM CTE
    LEFT JOIN CTE2
    USING (category)
    GROUP BY category;