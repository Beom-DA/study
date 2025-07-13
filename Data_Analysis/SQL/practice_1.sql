/********* INNER JOIN *********/
/* 밴다이어그램 A∩B */

/*
SELECT *
	FROM customer AS A
	INNER
	JOIN sales AS B
	on A.mem_no = B.mem_no;
*/

/* SELECT *
	FROM customer AS A
	INNER
	JOIN sales AS B
	ON A.mem_no = B.mem_no
	WHERE A.mem_no = '1000970';
*/

/********** LEFT JOIN ***********/
/* 밴다이어그램 A-B + (A∩B). B-A에 해당하는 부분은 null로 표시 */
/* SELECT *
	FROM customer AS A
	LEFT
	JOIN sales AS B
	ON A.mem_no = B.mem_no;
*/


/********** RIGHT JOIN ***********/
/* 밴다이어그램 B-A + (A∩B). A-B에 해당하는 부분은 null로 표시 */

/*SELECT *
	FROM customer as A
	RIGHT JOIN sales as B
	ON A.mem_no = B.mem_no
	WHERE A.mem_no IS NULL; /*비회원으로 주문*/
*/


