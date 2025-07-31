-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/


SELECT customer_id, COUNT(*) AS count_no_trans
    FROM visits V
    LEFT JOIN transactions T
    USING (visit_id)
    WHERE transaction_id IS NULL
    GROUP BY customer_id;