-- Write your PostgreSQL query statement below
select e.name as Employee
from Employee e
join Employee m
on e.managerId = m.id
Where e.salary > m.salary