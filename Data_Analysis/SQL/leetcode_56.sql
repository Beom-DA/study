-- https://leetcode.com/problems/patients-with-a-condition/description/

-- leetcode_55.sql을 참고해서 풀어보려 했지만 내 지식 범위 내의 문제가 아닌 것 같다.
-- 다른 사람의 쿼리 참고

select *
from patients 
where conditions like '% DIAB1%' or conditions like 'DIAB1%';

-- '%'은 임의의 문자 0개 이상을 의미한다.





-- 참고!
-- \m 은 단어의 시작을 의미한다.
-- ex) WHERE conditions ~ '\mDIAB1'