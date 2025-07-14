-- https://leetcode.com/problems/nth-highest-salary/description/

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT *
        FROM Employee
        
      
  );
END;
$$ LANGUAGE plpgsql;