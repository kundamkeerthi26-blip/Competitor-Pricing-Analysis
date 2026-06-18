-- Most Overpriced Market for StyleCo

SELECT Country,
       ROUND(
           AVG(CASE
                   WHEN Brand = 'Styleco'
                   THEN Original_Price_USD
               END)
           -
           AVG(CASE
                   WHEN Brand != 'Styleco'
                   THEN Original_Price_USD
               END)
       , 2) AS Price_Gap
FROM pricing_data
GROUP BY Country
ORDER BY Price_Gap DESC;