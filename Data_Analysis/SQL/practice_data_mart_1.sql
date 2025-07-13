/*********** 데이터 마트  ***********/
-- 데이터 마트란 추출한 데이터를 가공하는 과정 및 결과를 뜻함

-- SELECT A.mem_no, A.gender, A.birthday, A.addr, A.join_date
-- 	, SUM(B.sales_qty * C.price) AS 구매금액
-- 	, COUNT(B.order_no) 		 AS 구매횟수
-- 	, SUM(B.sales_qty)			 AS 구매수량
	
-- 	FROM customer AS A
-- 	LEFT JOIN sales AS B
-- 	ON A.mem_no = B.mem_no
-- 	LEFT JOIN product AS C
-- 	ON B.product_code = C.product_code
-- 	GROUP BY A.mem_no, A.gender, A.birthday, A.addr, A.join_date;



/********** 회원 구매정보 임시테이블 *********/
-- CREATE TEMPORARY TABLE customer_pur_info AS
-- SELECT A.mem_no, A.gender, A.birthday, A.addr, A.join_date
-- 	, SUM(B.sales_qty * C.price) AS 구매금액
-- 	, COUNT(B.order_no) 		 AS 구매횟수
-- 	, SUM(B.sales_qty)			 AS 구매수량
	
-- 	FROM customer AS A
-- 	LEFT JOIN sales AS B
-- 	ON A.mem_no = B.mem_no
-- 	LEFT JOIN product AS C
-- 	ON B.product_code = C.product_code
-- 	GROUP BY A.mem_no, A.gender, A.birthday, A.addr, A.join_date;


-- SELECT *
-- 	FROM customer_pur_info;

/************* 회원 연령대 추가 **************/
-- CREATE TEMPORARY TABLE customer_age_range AS
-- SELECT *
-- 	, 2025 - EXTRACT(YEAR FROM birthday) + 1 AS 나이
-- 	FROM customer;

/*********** 생년월일 -> 나이 -> 연령대 *******/
SELECT *
	,CASE WHEN 나이 < 10 THEN '10대 미만'
		  WHEN 나이 < 20 THEN '10대'
		  WHEN 나이 < 30 THEN '20대'
		  WHEN 나이 < 40 THEN '30대'
		  WHEN 나이 < 50 THEN '40대'
		  ELSE '50대 이상' END AS 연령대
	FROM customer_age_range;
