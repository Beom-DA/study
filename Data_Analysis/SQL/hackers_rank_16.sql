-- https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true



WITH RECURSIVE rec AS(
    SELECT submission_date, hacker_id
        FROM submissions
        GROUP BY submission_date, hacker_id
        HAVING submission_date = MIN(submission_date)
    
    UNION ALL
    
    SELECT rec.submission_date, rec.hacker_id
        FROM rec
        WHERE red.hacker_id IN (
            SELECT hacker_id 
                FROM submissions S
                WHERE S.submissions_date = MAX(rec.submission_date) + 1
        )
)


WITH CTE_count AS(
    SELECT submission_date, COUNT(*) AS count
        FROM rec
        GROUP BY submission_date
        ORDER BY submission_date
)


SET @row_num := 0;
SET @prev_date := NULL;

SELECT submission_date,
       count,
       hacker_id,
       name
FROM (
    SELECT submission_date,
           hacker_id,
           c AS submission_count,
           @row_num := IF(@prev_date = submission_date, @row_num + 1, 1) AS rn,
           @prev_date := submission_date
    FROM (
        SELECT submission_date,
               hacker_id,
               COUNT(*) AS c
        FROM submissions
        GROUP BY submission_date, hacker_id
        ORDER BY submission_date, c DESC, hacker_id
    ) AS t
) AS CTE
JOIN hackers USING (hacker_id)
JOIN CTE_count USING (submission_date)
WHERE rn = 1
ORDER BY submission_date;