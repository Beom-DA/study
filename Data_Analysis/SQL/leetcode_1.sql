-- https://leetcode.com/problems/combine-two-tables/

SELECT A.firstName, A.lastName, B.city, B.state
    FROM Person AS A
    LEFT JOIN Address AS B
    ON A.personId = B.personId;