/*SELECT *
	FROM customer AS A
	INNER JOIN sales AS B
	ON A.mem_no = B.mem_no;
*/


/*CREATE TEMPORARY TABLE customer_sales_inner_join AS
SELECT A.*, B.order_no
	FROM customer AS A
	INNER JOIN sales AS B
	ON A.mem_no = B.mem_no;
*/
/*
SELECT * FROM customer_sales_inner_join;
*/
/*PostgreSQL에서 CREATE TABLE AS 구문을 쓸 때, AS키워드가 반드시 필요하다
임시테이블은 서버 연결 종료 시 자동으로 삭제된다.*/

/* SELECT *
 FROM customer_sales_inner_join
 WHERE gender = 'man';
*/

SELECT addr, COUNT(order_no) AS 구매횟수
	FROM customer_sales_inner_join
	WHERE gender = 'man'
	GROUP BY addr
	HAVING COUNT(order_no) < 100
	ORDER BY COUNT(order_no) DESC;