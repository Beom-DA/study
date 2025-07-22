-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends

WITH CTE AS(
    SELECT requester_id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
)

SELECT requester_id AS id, COUNT(*) AS num
    FROM CTE
    GROUP BY requester_id
    ORDER BY num DESC
    limit 1;