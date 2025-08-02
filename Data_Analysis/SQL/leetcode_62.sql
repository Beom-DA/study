-- https://leetcode.com/problems/first-letter-capitalization-ii/


-- 로직의 흐름
-- 맨 앞에 있는 str을 upper OR ' '(공백)뒤에 있는 첫번째 글자를 upper OR '-'뒤에 있는 첫번째 글자를 upper

WITH CTE AS(
    SELECT content_id, STRING_TO_ARRAY(content_text, ' ') AS S
        FROM user_content
),
CTE2 AS(
    SELECT content_id, (UPPER(LEFT(UNNEST(S), 1)) || 
        LOWER(SUBSTRING(UNNEST(S) FROM 2))) AS str
        -- INITCAP(content_text) AS converted_text
        FROM CTE
),
CTE3 AS(
    SELECT DISTINCT content_id, ARRAY_TO_STRING(ARRAY_AGG(str) OVER(PARTITION BY content_id), ' ') AS str
        FROM CTE2
),
CTE4 AS(
    SELECT content_id,
        STRING_TO_ARRAY(str, '-') AS str
        FROM CTE3
),
CTE5 AS(
    SELECT content_id,
        (UPPER(LEFT(UNNEST(str), 1)) || SUBSTRING(UNNEST(str) FROM 2)) AS str,
        DENSE_RANK() OVER(PARTITION BY content_id ORDER BY str) AS rank
        FROM CTE4
),
CTE6 AS(
    SELECT content_id, ARRAY_TO_STRING(ARRAY_AGG(str ORDER BY rank), '-') AS converted_text
        FROM CTE5
        GROUP BY content_id
        ORDER BY content_id
)

SELECT content_id, content_text AS original_text, converted_text
    FROM user_content
    JOIN CTE6
    USING (content_id);