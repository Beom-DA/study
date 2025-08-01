-- https://leetcode.com/problems/average-selling-price/


SELECT P.product_id,
    COALESCE(ROUND(SUM(price * units) / SUM(units)::DECIMAL, 2), 0) AS average_price
    FROM prices P
    LEFT JOIN unitssold U
    ON P.product_id = U.product_id AND U.purchase_date BETWEEN P.start_date AND P.end_date
    GROUP BY P.product_id;