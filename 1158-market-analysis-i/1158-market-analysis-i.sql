-- Write your PostgreSQL query statement below
-- join 데이트와 2019년에 실행한 주문의 총 수
-- 유저를 기준으로 주문을 읽어온다. 그룹바이 이후 order_date 를 기준으로 2019만 뽑아 집계한다.

SELECT
u.user_id as buyer_id,
u.join_date,
COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
ON u.user_id = o.buyer_id
AND EXTRACT(YEAR FROM o.order_date) = 2019
GROUP BY u.user_id, u.join_date