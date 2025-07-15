-- https://leetcode.com/problems/nth-highest-salary/description/

/********** 첫 번째 방법 (sub_query)**********/
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT A.salary AS getNthHighestSalary
        FROM(
            SELECT E.salary
                , DENSE_RANK() OVER (ORDER BY E.salary DESC) AS 순위
                FROM Employee AS E
        ) AS A
        WHERE A.순위 = N
        LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;


/********** 두 번째 방법 (IF문)**********/
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $
BEGIN
IF N < 1 THEN 
    RETURN QUERY(SELECT NULL::INT AS salary); -- NULL::INT는 NULL값의 자료형을 INT로 바꾸는 코드. salary의 반환형은 int기 때문에 그냥 NULL을 입력하면 오류가 발생한다.
ELSE                                          -- SELECT문은 FROM절이 꼭 있어야하는건 아니다. 특정 값을 반환하려 할때 FROM절 없이 SELECT문 사용 가능
  RETURN QUERY (
    SELECT DISTINCT Employee.salary
      from Employee
      ORDER BY salary DESC
      LIMIT 1
      OFFSET N-1 -- 앞에서 N-1개를 건너뛰고, N번째 항목부터 결과를 반환한다.(LIMIT 1이 걸려있으므로 1개만 반환)
  );
 END IF;
END;
$ LANGUAGE plpgsql;