/*********** 3개 이상 테이블 결합 ************/

SELECT *
	FROM sales AS A
	LEFT JOIN customer AS B
	ON A.mem_no = B.mem_no
	LEFT JOIN product AS C
	on A.product_code = C.product_code;
	