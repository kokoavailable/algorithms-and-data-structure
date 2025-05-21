-- Write your PostgreSQL query statement below
-- 해당 날짜 이전 날짜중 가장 가까운 price 를 들고 오면 되고 없으면 10으로 들고오기.


WITH ranked AS (
    select
        product_id,
        new_price,
        ROW_NUMBER() OVER (
            Partition BY product_id
            ORDER BY change_date DESC
        ) AS rn
    from
        Products
    where 
        change_date <= '2019-08-16'
)
SELECT
    p.product_id,
    COALESCE(r.new_price, 10) as price
FROM (
    SELECT DISTINCT product_id FROM Products
) p
Left join ranked r 
    ON p.product_id = r.product_id
    AND r.rn = 1;