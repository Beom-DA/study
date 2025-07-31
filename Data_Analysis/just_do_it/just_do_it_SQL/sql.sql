SELECT ta_ymd AS 날짜, AVG(hour) AS 시간, AVG(age) AS 나이, AVG(amt) AS 금액  
	FROM consumption
	GROUP BY ta_ymd
	LIMIT 5;