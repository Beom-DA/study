-- https://leetcode.com/problems/find-covid-recovery-patients/


WITH CTE1 AS (
    SELECT *
        FROM covid_tests
        WHERE (patient_id,test_date) IN (SELECT patient_id, MIN(test_date)
                                FROM covid_tests
                                WHERE result = 'Positive'
                                GROUP BY patient_id)
        AND result = 'Positive'
),
CTE2 AS(
    SELECT *
        FROM covid_tests
        WHERE result = 'Negative'  
),
CTE3 AS(
    SELECT c1.patient_id AS patient_id, c1.test_date AS d1, c1.result AS p, c2.patient_id AS p2, c2.test_date AS d2, c2.result AS n
        FROM CTE1 c1
        JOIN LATERAL(
            SELECT *
                FROM CTE2 c2
                WHERE c1.patient_id = c2.patient_id
                AND c1.test_date < c2.test_date
                limit 1
        ) c2 ON TRUE     
        
)

SELECT patient_id, patient_name, age, d2 - d1 AS recovery_time 
    FROM CTE3
    JOIN patients
    USING (patient_id)
    ORDER BY recovery_time, patient_name;
    

