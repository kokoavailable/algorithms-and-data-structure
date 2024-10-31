WITH Sales AS (
    SELECT 
        u.product_id,
        u.units,
        p.price
    FROM 
        UnitsSold u
    JOIN 
        Prices p 
    ON 
        u.product_id = p.product_id 
        AND u.purchase_date BETWEEN p.start_date AND p.end_date
),
Revenue AS (
    SELECT
        product_id,
        SUM(price * units) AS total_revenue,
        SUM(units) AS total_units
    FROM
        Sales
    GROUP BY
        product_id
)
SELECT 
    p.product_id,
    COALESCE(ROUND(total_revenue::numeric / NULLIF(total_units, 0), 2), 0) AS average_price
FROM 
    (SELECT DISTINCT product_id FROM Prices) p
LEFT JOIN 
    Revenue r ON p.product_id = r.product_id;
