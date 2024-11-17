WITH FirstOrders AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM
        Delivery
    GROUP BY
        customer_id
),
FirstOrderDetails AS (
    SELECT
        f.customer_id,
        d.delivery_id,
        d.order_date,
        d.customer_pref_delivery_date
    FROM
        FirstOrders f
    JOIN
        Delivery d
    ON
        f.customer_id = d.customer_id AND f.first_order_date = d.order_date
),
ImmediateOrders AS (
    SELECT
        COUNT(*) AS immediate_count
    FROM
        FirstOrderDetails
    WHERE
        order_date = customer_pref_delivery_date
),
TotalCustomers AS (
    SELECT
        COUNT(DISTINCT customer_id) AS total_count
    FROM
        Delivery
)
SELECT
    ROUND((i.immediate_count * 100.0) / t.total_count, 2) AS immediate_percentage
FROM
    ImmediateOrders i,
    TotalCustomers t;