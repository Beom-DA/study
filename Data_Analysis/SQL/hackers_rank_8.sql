-- https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true



SELECT CTE.hacker_id, name
    FROM (
        SELECT S.hacker_id AS hacker_id, COUNT(challenge_id) AS count
            FROM submissions AS S
            JOIN challenges AS C
            USING (challenge_id)
            JOIN difficulty AS D
            USING (difficulty_level)
            WHERE S.score = D.score
            GROUP BY S.hacker_id    
    ) AS CTE
    JOIN hackers
    USING (hacker_id)
    WHERE count > 1
    ORDER BY count DESC, CTE.hacker_id;



-- 다른사람의 쿼리
    select
    h.hacker_id, h.name
from 
    hackers h
join
    submissions s on h.hacker_id = s.hacker_id
join
    challenges c on s.challenge_id = c.challenge_id
join
    difficulty d on c.difficulty_level = d.difficulty_level
where 
    s.score = d.score
group by
    h.hacker_id, h.name
having
    count(*) > 1
order by
    count (*) desc, hacker_id asc;