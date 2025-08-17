-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true



SELECT CTE1.hacker_id, CTE1.name, CTE1.c
    FROM (
        SELECT DISTINCT hacker_id, name, COUNT(*) OVER(PARTITION BY hacker_id) AS c
            FROM hackers H
            JOIN challenges C
            USING (hacker_id)
    ) AS CTE1
    JOIN (
        SELECT c
            FROM (
                SELECT DISTINCT hacker_id, name, 
                COUNT(*) OVER(PARTITION BY hacker_id) AS c
                    FROM hackers H
                    JOIN challenges C
                    USING (hacker_id)   
            ) AS CTE
            GROUP BY c
            HAVING COUNT(c) = 1  
    ) AS CTE2
    USING (c)
    
UNION

SELECT A.hacker_id, A.name, A.c
    FROM (
    SELECT DISTINCT hacker_id, name, 
        COUNT(*) OVER(PARTITION BY hacker_id) AS c
            FROM hackers H
            JOIN challenges C
            USING (hacker_id) 
    ) AS A
    JOIN (
        SELECT DISTINCT COUNT(*) OVER(PARTITION BY hacker_id) AS c
            FROM hackers H
            JOIN challenges C
            USING (hacker_id) 
            ORDER BY c DESC
            LIMIT 1    
    ) AS B
    USING (c)
    ORDER BY 3 DESC, 1;
 