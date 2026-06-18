-- How does each brand's price compare to the country average? (Window Function)

SELECT
    Country,
    Brand,
    ROUND(AVG(Original_Price_USD), 2) AS Brand_Avg_Price,
    ROUND(AVG(AVG(Original_Price_USD)) OVER (PARTITION BY Country), 2) AS Country_Avg_Price,
    ROUND(AVG(Original_Price_USD) - AVG(AVG(Original_Price_USD)) OVER (PARTITION BY Country), 2) AS Diff_From_Country_Avg
FROM pricing_data
GROUP BY Country, Brand
ORDER BY Country, Diff_From_Country_Avg DESC;
