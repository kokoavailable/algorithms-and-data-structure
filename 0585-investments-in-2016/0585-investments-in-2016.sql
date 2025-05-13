-- Write your PostgreSQL query statement below
-- 같은 tiv 2015 가 2개 이상
-- lat, lon이 같이 중복된 것 없을 것. (전체 칼럼에 대해)
-- 해당 조건에 맞는 row 들의 tiv를 전부 sum
-- 두 조건이 동시에 필터링 돼야할 듯..

SELECT ROUND(SUM(i.tiv_2016)::numeric, 2) AS tiv_2016
FROM Insurance i
JOIN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
) dup
ON i.tiv_2015 = dup.tiv_2015
JOIN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
) ul
ON i.lat = ul.lat AND i.lon = ul.lon;
