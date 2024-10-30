-- Write your PostgreSQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM
(
select 
num,
lag(num) over (order by id) as prev_num,
lead(num) over (order by id) as next_num
from Logs
) as temp
WHERE num = prev_num AND num = next_num
