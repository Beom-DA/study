-- SELECT A.*, A.SALES_QTY * B.PRICE AS 결제금액
-- 	FROM sales AS A
-- 	LEFT JOIN product AS B
-- 	ON A.product_code = B.product_code;

/*********** VIEW 생성 *************/
-- CREATE TABLE sales_product AS
-- SELECT A.*, A.SALES_QTY * B.PRICE AS 결제금액
-- 	FROM sales AS A
-- 	LEFT JOIN product AS B
-- 	ON A.product_code = B.product_code;

/************ VIEW 실행 *************/
-- SELECT *
-- 	FROM sales_product;

/************ VIEW 수정 **************/
-- PostgreSQL에서 한번 만들어진 VIEW는 수정이 불가능하다.
-- 수정을 하고 싶다면 아예 새로운 이름의 VIEW를 만들어야한다.

/************ VIEW 삭제 *************/
-- DROP TABLE sales_product;
-- MYSQL은 DROP VIEW를 사용하지만 PostgreSQL은 DROP TABLE을 사용한다.

/************ VIEW 특징 **************/
-- 중복되는 열이 저장되지 않는다.


/************ FUNCTION  ***********/
-- FUNCTION과 PROCEDURE 중 FUNCTION이 실무에 더 적합한 도구다.

-- CREATE FUNCTION cst_gen_addr_in(IN input_A VARCHAR(20), input_B VARCHAR(20))
-- RETURNS SETOF customer
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- 	RETURN QUERY
-- 	SELECT *
-- 		FROM customer
-- 		WHERE gender = input_A
-- 		AND addr = input_B;
-- END;
-- $$;


/************ FUNCTION 실행 *************/
SELECT *
	FROM cst_gen_addr_in('man','Seoul');
