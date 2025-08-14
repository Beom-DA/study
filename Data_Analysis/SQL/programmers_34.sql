-- https://school.programmers.co.kr/learn/courses/30/lessons/132204



SELECT apnt_no, pt_name, A.pt_no, A.mcdp_cd, dr_name, apnt_ymd
    FROM appointment A
    JOIN patient
    USING (pt_no)
    JOIN doctor D
    ON A.mddr_id = D.dr_id
    WHERE CONVERT(apnt_ymd, DATE) = '2022-04-13' AND apnt_cncl_yn = 'N' AND A.mcdp_cd = 'CS'
    ORDER BY apnt_ymd;