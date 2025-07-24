-- https://leetcode.com/problems/product-sales-analysis-i/description/

SELECT P.product_name, S.year, S.price
    FROM sales S
    LEFT JOIN product P
    ON S.product_id = P.product_id;


-- 다른 사람의 쿼리
SELECT product_name,
        year,
        price
FROM Sales
INNER JOIN Product
USING (product_id);

-- USING 뭐임?;;
-- USING은 ON을 대체하는 간결한 코드.
-- ON을 사용하면 똑같은 컬럼이 두개 출력되지만
-- USING을 사용하면 하나만 출력된다.