-- https://leetcode.com/problems/customers-who-never-order/description/

SELECT name as customers
    FROM customers AS A
    left Join orders AS B
    ON A.id = B.customerid
    WHERE B.id is NULL;