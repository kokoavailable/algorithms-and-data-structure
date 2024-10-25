# Write your MySQL query statement below
SELECT 
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 ELSE 0 END) /
        COUNT(*), 2
    ) AS "Cancellation Rate"
FROM 
    Trips t
JOIN 
    Users u_client ON t.client_id = u_client.users_id AND u_client.banned = 'No'
JOIN 
    Users u_driver ON t.driver_id = u_driver.users_id AND u_driver.banned = 'No'
WHERE 
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    t.request_at;