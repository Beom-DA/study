-- https://leetcode.com/problems/dna-pattern-recognition/


WITH CTE AS(
    SELECT sample_id,
        COUNT(dna_sequence) FILTER (WHERE dna_sequence LIKE 'ATG%') AS has_start,
        COUNT(dna_sequence) FILTER (WHERE dna_sequence LIKE '%TAA' 
                                    OR dna_sequence LIKE '%TAG' 
                                    OR dna_sequence LIKE '%TGA') AS has_stop,
        COUNT(dna_sequence) FILTER (WHERE dna_sequence LIKE '%ATAT%' 
                                    OR dna_sequence LIKE '%ATAT' 
                                    OR dna_sequence LIKE 'ATAT%') AS has_atat,
        COUNT(dna_sequence) FILTER (WHERE dna_sequence LIKE '%GGG%' 
                                    OR dna_sequence LIKE '%GGG' 
                                    OR dna_sequence LIKE 'GGG%') AS has_ggg
        FROM samples
        GROUP BY sample_id
        ORDER BY sample_id    
)

SELECT *
    FROM samples
    JOIN CTE
    USING (sample_id);