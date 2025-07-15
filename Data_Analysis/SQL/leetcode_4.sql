-- https://leetcode.com/problems/rank-scores/description/

-- decimal 타입
-- 고정 소수점(Fixed-point) 숫자 타입
-- 소수점 이하 자리수까지 정확하게 저장 가능
-- 반올림/오차 없이 계산이 필요할때 사용

SELECT A.score, A.rank
    FROM(
        SELECT *
            , DENSE_RANK() OVER(ORDER BY score DESC) as rank
            FROM scores
    ) AS A;