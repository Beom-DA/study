-- https://leetcode.com/problems/queries-quality-and-percentage/


SELECT query_name,
    ROUND(SUM(rating::DECIMAL / position)/COUNT(*), 2) AS quality,
    ROUND((COUNT(rating) FILTER (WHERE rating < 3) / COUNT(*)::DECIMAL), 4) * 100 AS poor_query_percentage
    FROM queries
    GROUP BY query_name;