/************** 연습 문제 **************/
-- 1. customer 테이블을 활용하여, 가입일자가 2019년이며 생일이 4~6월생인 회원 수를 조회하시오
-- SELECT COUNT(mem_no) AS 회원수
-- 	FROM customer
-- 	WHERE EXTRACT(YEAR FROM join_date) = 2019
-- 	AND EXTRACT(MONTH FROM birthday) BETWEEN 4 and 6;
	
-- 2. sales 및 product테이블을 활용하여, 1회 주문시 평균 구매금액을 구하시오(비회원 9999999 제외)
-- SELECT COUNT(A.order_no) AS 전체주문수, SUM(B.price) AS 전체구매금액, SUM(B.price) / COUNT(A.order_no) AS 평균구매금액 
-- 	FROM sales AS A
-- 	LEFT JOIN product AS B
-- 	ON A.product_code = B.product_code
--  WHERE A.mem_no <> '9999999';

-- 3. sales 테이블을 활용하여, 구매수량이 높은 상위 10명을 조회하시오(비회원 제외) --> 모르겠음
-- 내가 한 방법
-- SELECT B.mem_no AS 회원번호, SUM(A.sales_qty) AS 구매_수량
-- 	FROM sales AS A
-- 	LEFT JOIN customer AS B
-- 	ON A.mem_no = B.mem_no
-- 	WHERE B.mem_no is NOT NULL
-- 	GROUP BY 회원번호
-- 	ORDER BY 구매_수량 DESC
-- 	LIMIT 10;

-- 다른 방법
SELECT mem_no
	, SUM(sales_qty) AS 구매수량
	, ROW_NUMBER() OVER (ORDER BY SUM(sales_qty) DESC) AS 고유한_순위_반환
	, RANK() 	   OVER (ORDER BY SUM(sales_qty) DESC) AS 동일한_순위_반환
	, DENSE_RANK() OVER (ORDER BY SUM(sales_qty) DESC) AS 동일한_순위_반환_하나의등수
	FROM sales
	WHERE mem_no <> '9999999'
	GROUP BY mem_no
	limit 10;


/************** VIEW 및 Function ************/
-- 1. view를 활용하여, sales 테이블을 기준으로 customer 및 product 테이블을 LEFT JOIN 결합한 가상 테이블을 생성하시오
-- 열은 sales 테이블의 모든 열 + customer 테이블의 gender + product 테이블의 brand
-- CREATE VIEW sales_cus_pro_table AS
-- SELECT A.*
-- 	, B.gender, C.brand
-- 	FROM sales AS A
-- 	LEFT JOIN customer AS B
-- 	ON A.mem_no = B.mem_no
-- 	LEFT JOIN product AS C
-- 	ON A.product_code = C.product_code;

-- SELECT *
-- 	FROM sales_cus_pro_table;

-- 2.  Function을 활용하여 customer의 몇월부터 몇월까지의 생일인 회원을 조회하는 작업을 저장하시오
-- CREATE FUNCTION find_customer(IN input_A INTEGER, input_B INTEGER)
-- RETURNS SETOF customer
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- 	RETURN QUERY
-- 	SELECT *
-- 		FROM customer
-- 		WHERE EXTRACT(MONTH FROM birthday) BETWEEN input_A and input_B;
-- END;
-- $$;

-- SELECT *
-- 	FROM find_customer(4, 6);

-- DROP FUNCTION find_customer;


/************** 데이터 마트 *****************/
-- 1. sales 및 product 테이블을 활용하여, sales 테이블을 기준으로 product 테이블을 LEFT JOIN 결합한 테이블을 생성하시오
-- 열은 sales 테이블의 모든 열 + product 테이블의 category, type + sales_qty * price 구매금액
-- CREATE TABLE data_mart AS
-- SELECT A.*, B.category, B.type, A.sales_qty * B.price AS 구매금액
-- 	FROM sales AS A
-- 	LEFT JOIN product AS B
-- 	ON A.product_code = B.product_code;

-- SELECT *
-- 	FROM data_mart;

-- 2. (1)에서 생성한 데이터 마트를 활용하여, category 및 type별 구매금액 합계를 구하시오
-- SELECT category, type, SUM(구매금액) AS 총_구매금액
-- 	FROM data_mart
-- 	GROUP BY category, type
-- 	ORDER BY category;
	

