-- Write your PostgreSQL query statement below
SELECT
    manager.employee_id,
    manager.name,
    COUNT(employee.employee_id) AS reports_count,
    ROUND(AVG(employee.age)) AS average_age
FROM
    Employees AS manager
JOIN
    Employees AS employee ON manager.employee_id = employee.reports_to
GROUP BY
    manager.employee_id, manager.name
ORDER BY
    manager.employee_id;