-- https://leetcode.com/problems/delete-duplicate-emails/description/

DELETE FROM Person p1
USING Person p2
WHERE p1.email = p2.email
  AND p1.id > p2.id;

-- DELETE.... USING .... 구문을 처음 봤다.
-- WHERE문 조건에 해당하는 행이 삭제가 되는데 Person 테이블에서 삭제된다. 