-- https://leetcode.com/problems/movie-rating/

WITH avg_CTE AS(
    SELECT movie_id, title, AVG(rating)
        FROM movierating
        JOIN movies
        USING (movie_id)
        WHERE created_at BETWEEN '2020-02-01' AND '2020-02-28'
        GROUP BY movie_id, title
        ORDER BY avg DESC, title
        LIMIT 1
),
rate_CTE AS(
    SELECT user_id, name, COUNT(*)
        FROM movierating
        JOIN users
        USING (user_id)
        GROUP BY user_id, name
        ORDER BY count DESC, name 
        LIMIT 1
)

SELECT name as results FROM rate_CTE
UNION ALL
SELECT title as results FROM avg_CTE; -- 서로 다른 테이블의 값을 하나의 테이블의 하나의 열로 표현하는 방법
