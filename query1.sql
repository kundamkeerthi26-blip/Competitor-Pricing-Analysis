-- What is the average price of each brand and how does StyleCo compare?

SELECT Brand,
    ROUND(AVG(Original_Price_USD), 2) AS Avg_Price_USD
FROM pricing_data
GROUP BY Brand
ORDER BY Avg_Price_USD DESC;