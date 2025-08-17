-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true




SELECT id, age, coins_needed, power
    FROM wands AS W
    JOIN wands_property AS P
    USING (code)
    JOIN (
        SELECT power, age, MIN(coins_needed) AS coins_needed
            FROM wands
            JOIN wands_property
            USING (code)
            WHERE is_evil = 0
            GROUP BY age, power    
    ) AS CTE
    USING (power, age, coins_needed)
    ORDER BY power DESC, age DESC;
