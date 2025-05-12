-- Write your PostgreSQL query statement below
select
    email as Email
from
    Person
GROUP BY email
Having count(*) > 1