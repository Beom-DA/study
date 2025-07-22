-- https://leetcode.com/problems/sales-person/
-- WHRER IN 문을 사용한 방법
SELECT name
    FROM salesperson
    WHERE sales_id NOT IN
        (
            SELECT sales_id
                FROM orders
                WHERE com_id IN
                (
                    SELECT com_id
                        FROM company
                        WHERE name = 'RED'
                )
        );

-- CTE와 JOIN문을 사용한 방법
WITH CTE AS(
    SELECT sales_id
        FROM orders O
        LEFT JOIN company C
        ON O.com_id = C.com_id
        WHERE C.name = 'RED'
)

SELECT S.name
    FROM salesperson S
    LEFT JOIN CTE
    ON S.sales_id = CTE.sales_id
    WHERE CTE.sales_id IS NULL;