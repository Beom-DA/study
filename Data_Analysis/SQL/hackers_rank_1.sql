-- https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true



SELECT CONCAT(name, '(' , LEFT(occupation,1), ')') AS output
    FROM occupations
    ORDER BY output;

SELECT CONCAT('There are a total of ', count, ' ', LOWER(occupation), 's.') AS output
    FROM (
        SELECT occupation, COUNT(*) AS count
            FROM occupations
            GROUP BY occupation
    ) AS CTE
    ORDER BY count, output;