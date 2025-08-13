-- https://school.programmers.co.kr/learn/courses/30/lessons/284531



WITH CTE AS(
    SELECT route, ROUND(SUM(d_between_dist),1) AS total_distance,
        ROUND(AVG(d_between_dist),2) AS average_distance
        FROM subway_distance
        GROUP BY route
        ORDER BY total_distance DESC
)

SELECT route, CONCAT(total_distance, 'km') AS total_distance, CONCAT(average_distance, 'km') AS average_distance
    FROM CTE