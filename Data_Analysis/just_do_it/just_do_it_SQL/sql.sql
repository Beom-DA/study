WITH CTE1 AS(
	select 날짜::DATE, "평균기온(℃)" AS 기온
	from temperature
	
),
CTE2 AS(
	select 날짜::DATE, "강수량(mm)" AS 강수량
		from precipitation
		
),
CTE3 AS(
	SELECT 날짜, 기온, 강수량
		FROM CTE2
		JOIN CTE1
		USING (날짜)
		WHERE 날짜 >= '2024-06-01' AND 날짜 <= '2025-05-31'
),
CTE4 AS(
	SELECT 일시::DATE AS 날짜, "평균풍속(m/s)" AS 풍속, "평균습도(%rh)" AS 습도
		FROM wind
		JOIN humidity
		USING (일시)
		WHERE 일시 >= '2024-06-01' AND 일시 <= '2025-05-31'
),
CTE5 AS(
	SELECT CTE3.날짜 AS 날짜, 기온, 강수량, 풍속, 습도
		FROM CTE3
		JOIN CTE4
		USING (날짜)
),
CTE6 AS(
	SELECT ta_ymd::text::DATE AS 날짜, card_tpbuz_nm_2 AS 물품분류, hour AS 시간, sex AS 성별, age AS 나이, day AS 요일, amt AS 금액
		FROM consumption
		WHERE ta_ymd >= 20240601 AND ta_ymd <= 20250531 
)

SELECT C1.날짜, 물품분류, 시간, 성별, 나이, 요일, 금액, 기온, 강수량, 풍속, 습도
	FROM CTE6 C1
	JOIN CTE5 C2
	USING (날짜);


	





