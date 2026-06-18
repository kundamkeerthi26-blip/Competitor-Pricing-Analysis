-- Rank Brands by Average Price

SELECT Brand,
       ROUND(AVG(Original_Price_USD),2) AS Avg_Price_USD
FROM pricing_data
GROUP BY Brand
ORDER BY Avg_Price_USD DESC;