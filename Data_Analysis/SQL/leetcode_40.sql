-- https://leetcode.com/problems/product-price-at-a-given-date/

-- product_id 종류 당 하나씩 모두 저장
WITH CTE AS(
    SELECT DISTINCT product_id
        FROM products
),

-- id 당 2019-08-16(포함) 이전 날짜 중 최신 날짜
CTE2 AS(
    SELECT product_id, MAX(change_date) AS change_date
        FROM products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
        HAVING MAX(change_date) <= '2019-08-16'
),

-- 최신 날짜에 해당하는 price 값 저장
CTE3 AS(
    SELECT P.product_id, P.new_price AS price
    FROM products P
    JOIN (
        SELECT product_id,change_date FROM CTE2
    ) AS C
    ON P.product_id = C.product_id AND P.change_date = C.change_date
    --WHERE (product_id,change_date) IN (SELECT product_id,change_date FROM CTE2)
    -- WHERE IN 문 대신에 JOIN 문으로 바꿨더니 성능이 더 좋아졌다.
)

-- 결과값
SELECT product_id, COALESCE(price,10) AS price
    FROM CTE
    LEFT JOIN CTE3
    USING (product_id);