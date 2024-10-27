CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    WITH RankedEmployeeSalaries AS (
        SELECT e1.*,
            DENSE_RANK() OVER (ORDER BY e1.salary DESC) as drk_sal
        FROM Employee e1
    )

    SELECT res.salary 
    FROM RankedEmployeeSalaries res
    WHERE res.drk_sal = N
    GROUP BY res.salary

    );
END;
$$ LANGUAGE plpgsql;