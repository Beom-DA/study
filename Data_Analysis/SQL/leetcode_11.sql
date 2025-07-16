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



-- 다른 사람이 한 QUERY
SELECT current_day.id
FROM Weather AS current_day
WHERE EXISTS (
    SELECT 1
    FROM Weather AS yesterday
    WHERE current_day.temperature > yesterday.temperature
    AND current_day.recordDate = yesterday.recordDate + 1
);

-- EXISTS는 조건문에 해당하는 행이 하나라도 있으면 True를 반환하고 하나도 없으면 False를 반환한다.
-- WHERE EXISTS 바깥에서 그에 해당하는 행에 대한 데이터를 추출한다.