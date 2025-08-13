-- https://school.programmers.co.kr/learn/courses/30/lessons/131124



WITH CTE AS(
    SELECT member_id, COUNT(*) AS count
        FROM rest_review R
        GROUP BY member_id
        ORDER BY count DESC
        LIMIT 1
)

SELECT member_name, review_text, DATE_FORMAT(review_date, '%Y-%m-%d') AS review_date
    FROM member_profile
    JOIN CTE
    USING (member_id)
    JOIN rest_review
    USING (member_id)
    ORDER BY review_date, review_text;