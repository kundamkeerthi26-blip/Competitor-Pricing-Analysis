# Competitor Pricing Analysis

## Project Overview
End-to-end competitor pricing analysis for StyleCo, a mid-market 
fashion brand competing against 9 global brands across 7 countries.
Built using Python (Pandas), MySQL, and Power BI.

## Tools Used
- Python (Pandas) — Data cleaning and currency conversion
- MySQL — Business SQL analysis (12 queries)
- Power BI — Interactive 3-page dashboard

## Dataset
- 2,100 rows synthetic dataset
- 10 brands, 7 countries, 10 product categories
- 3 seasons (SS2024, FW2024, SS2025)
- Data sources: Partner Data, Mystery Shopping, Website Scrape
- Note: Dataset is synthetically generated to simulate 
  real-world competitor pricing scenarios

## Key Findings
1. StyleCo ranks 5th in average price at $142.55 vs market avg $135.35
2. India is StyleCo's most overpriced market at $158 avg
3. Pull&Bear is the cheapest competitor across most markets
4. Handbags have the highest avg price ($357) across all brands
5. H&M is the most aggressive discounter at 13.05%
6. StyleCo discounts least aggressively at 10.95%
7. UAE offers the highest discounts at 13.12%

## Business Recommendations

### Recommendation 1 — Reduce prices in India
StyleCo charges the highest average price in India at $158
vs market average. Recommend a 10-12% price reduction on
Jackets and Handbags to match COS and Zara pricing in
that market.

### Recommendation 2 — Increase discount aggressiveness
StyleCo has the lowest discount rate (10.95%) vs market avg
(11.84%). Increasing seasonal discounts to 13-14% during
Fall/Winter matching H&M strategy could improve sell-through
rate and reduce out-of-stock risk.

### Recommendation 3 — Reposition T-Shirts and Accessories
StyleCo's T-Shirts ($39) and Accessories ($46) are the lowest
priced categories. These are high-volume price-sensitive
categories. Recommend pricing 5-8% below market average
to drive volume and improve market share.

## SQL Queries Covered
1. Average price by brand
2. Cheapest competitor by country
3. StyleCo vs market average by country
4. Highest average price category
5. Most aggressive discounting brand
6. Highest average price country
7. Country offering most discounts
8. StyleCo category overpricing analysis
9. Seasonal price analysis
10. Out-of-stock analysis by brand
11. Brand price vs country average (Window Function)
12. Most overpriced market for StyleCo

## Power BI Dashboard Pages
- Page 1 — Brand Overview
- Page 2 — Country Analysis  
- Page 3 — Pricing Insights

## Project Structure
Styleco-Competitor-Pricing-Analysis/
│
├── Data Cleaning/
│   └── Output/
│       └── clean_pricing_data.csv
│
├── Python/
│   └── cleaning_script.py
│
├── SQL/
│   ├── setup_query.sql
│   ├── query1.sql through query12.sql
│
├── Power BI/
│   └── competitor_pricing_analysis.pbix
│
└── README.md