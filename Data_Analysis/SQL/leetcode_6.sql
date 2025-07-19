-- https://leetcode.com/problems/duplicate-emails/description/


SELECT A.email
    FROM(
        SELECT email, COUNT(email)
            FROM person
            GROUP by email
            HAVING COUNT(email) > 1
    ) AS A;