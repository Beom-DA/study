/********** 서브 쿼리 ***********/

SELECT *
	, (SELECT gender 
		FROM customer
		WHERE A.mem_no = mem_no)
	FROM sales AS A;