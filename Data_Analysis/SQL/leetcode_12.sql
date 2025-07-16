-- https://leetcode.com/problems/rising-temperature/description/
-- LAG()를 사용하면 될 것 같은 느낌

SELECT D.id
    FROM(
        SELECT *
            , LAG(recordDate) OVER() y_date
            , LAG(temperature) OVER() y_temp
            FROM (SELECT * FROM weather ORDER BY recordDate)
            ORDER BY recordDate
    ) AS D
    WHERE D.y_temp IS NOT NULL 
    AND D.recordDate - D.y_date = 1 -- Date자료형끼리 연산을 하면 INTEGER자료형이 반환된다.
    AND D.temperature > D.y_temp;