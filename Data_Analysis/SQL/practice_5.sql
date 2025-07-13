-- 1. customer 테이블의 가입연도별 및 지역별 회원 수를 조회하시오
-- FROM/GROUP BY/ SELECT/ YEAR 및 COUNT 함수 활용

-- SELECT EXTRACT(YEAR FROM join_date) AS 가입연도, addr AS 지역, COUNT(mem_no)
-- 	FROM customer
-- 	GROUP BY 가입연도, 지역
-- 	ORDER BY 지역;
	

-- 2. (1) 명령어에서 성별이 남성회원 조건을 추가한 뒤, 회원 수가 50명 이상인 조건을 추가하시오
-- WHERE절 / HAVING절 활용

-- SELECT EXTRACT(YEAR FROM join_date) AS 가입연도, addr AS 지역, COUNT(mem_no)
-- 	FROM customer
-- 	WHERE gender = 'man'
-- 	GROUP BY 가입연도, 지역
-- 	HAVING COUNT(mem_no) > 50
-- 	ORDER BY 지역;

-- 3. (2) 명령어에서 회원 수를 내림차순으로 정렬하시오

-- SELECT EXTRACT(YEAR FROM join_date) AS 가입연도, addr AS 지역, COUNT(mem_no) AS 회원수
-- 	FROM customer
-- 	WHERE gender = 'man'
-- 	GROUP BY 가입연도, 지역
-- 	HAVING COUNT(mem_no) > 50
-- 	ORDER BY 회원수;


/************ 데이터 조회(SELECT) + 데이터 결합(JOIN) *************/

-- 1. sales 테이블을 기준으로 product 테이블을 LEFT JOIN 하시오
-- SELECT *
-- 	FROM sales AS A
-- 	LEFT JOIN product AS B
-- 	ON A.product_code = B.product_code;



-- 2. (1)에서 결합된 테이블을 활용하여, 브랜드별 판매수량을 구하시오
-- SELECT B.brand AS 브랜드, SUM(A.sales_qty) AS 판매수량
-- 	FROM sales AS A
-- 	LEFT JOIN product AS B
-- 	ON A.product_code = B.product_code
-- 	GROUP BY 브랜드;

-- 3. customer 및 sales 테이블을 활용하여, 회원가입만 하고 주문이력이 없는 회원 수를 구하시오
SELECT COUNT(A.mem_no) AS 회원수
	FROM customer AS A
	LEFT JOIN sales AS B
	ON A.mem_no = B.mem_no
	WHERE B.product_code is NULL
	
	
