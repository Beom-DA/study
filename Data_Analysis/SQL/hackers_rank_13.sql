-- https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true



SELECT S1.name
    FROM students S1
    JOIN friends F
    USING (id)
    JOIN students S2
    ON F.friend_id = S2.id
    JOIN packages P1
    ON P1.id = S1.id
    JOIN packages P2
    ON F.friend_id = P2.id
    WHERE P1.salary < P2.salary
    ORDER BY P2.salary;