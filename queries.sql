SELECT SUM(Sales) AS total_revenue
FROM cleaned_orders;

SELECT AVG(Sales) AS avg_order_value
FROM cleaned_orders;

SELECT AVG(order_total) AS avg_order_value_precise
FROM (
    SELECT `Order ID`, SUM(Sales) AS order_total
    FROM cleaned_orders
    GROUP BY `Order ID`
) AS order_totals;

-- Revenue by category
SELECT Category, SUM(Sales) AS category_revenue
FROM cleaned_orders
GROUP BY Category
ORDER BY category_revenue DESC;

-- Revenue by month
SELECT `Order Month`, SUM(Sales) AS monthly_revenue
FROM cleaned_orders
GROUP BY `Order Month`
ORDER BY `Order Month`;


