-- https://school.programmers.co.kr/learn/courses/30/lessons/131118



SELECT rest_id, rest_name, food_type, favorites, address, ROUND(AVG(review_score),2) AS score
    FROM rest_info
    JOIN rest_review
    USING (rest_id)
    WHERE address LIKE '서울%'
    GROUP BY rest_id, rest_name, food_type, favorites, address
    ORDER BY score DESC, favorites DESC;