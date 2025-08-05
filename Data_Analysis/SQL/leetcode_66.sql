-- https://leetcode.com/problems/find-product-recommendation-pairs/


WITH filtered_product AS (
  SELECT product_id
  FROM productpurchases
  GROUP BY product_id
  HAVING COUNT(DISTINCT user_id) > 2
),
CTE AS (
  SELECT DISTINCT user_id, product_id
  FROM productpurchases
  WHERE product_id IN (SELECT product_id FROM filtered_product)
),

CTE1 AS(
    SELECT p1.product_id AS product1_id, p2.product_id AS product2_id,
        p1.category AS product1_category, p2.category AS product2_category
        FROM productinfo p1, productinfo p2
        WHERE p1.product_id < p2.product_id    
),
CTE2 AS(
    SELECT p1.user_id, p1.product_id AS product1_id, p2.product_id AS product2_id
        FROM CTE p1, CTE p2
        WHERE p1.user_id = p2.user_id
        AND p1.product_id < p2.product_id    
)

SELECT product1_id, product2_id, product1_category, product2_category, COUNT(*) AS customer_count
    FROM CTE1
    JOIN CTE2
    USING (product1_id, product2_id)
    GROUP BY product1_id, product2_id, product1_category, product2_category
    HAVING COUNT(*) > 2
    ORDER BY customer_count DESC, product1_id, product2_id;