SELECT 
    TO_CHAR(trans_date, 'YYYY-MM') AS month, -- 연월 추출
    country, 
    COUNT(*) AS trans_count, -- 전체 거래 수
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count, -- 승인된 거래 수
    SUM(amount) AS trans_total_amount, -- 전체 거래 금액
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount -- 승인된 거래 금액
FROM 
    Transactions
GROUP BY 
    TO_CHAR(trans_date, 'YYYY-MM'), country -- 월별 및 국가별 그룹화
ORDER BY 
    month, country; -- 결과 정렬