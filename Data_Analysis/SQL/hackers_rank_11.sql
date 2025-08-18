-- https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true

SELECT hacker_id, name, SUM(max_score) AS total_score
    FROM (
        SELECT hacker_id, name, MAX(score) AS max_score
            FROM submissions
            JOIN hackers
            USING (hacker_id)
            GROUP BY hacker_id, name, challenge_id    
    ) AS CTE
    GROUP BY hacker_id, name
    HAVING SUM(max_score) > 0
    ORDER BY total_score DESC, hacker_id;