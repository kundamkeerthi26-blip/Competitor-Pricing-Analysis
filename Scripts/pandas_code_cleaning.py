# COMPETITOR PRICING ANALYSIS — Data Cleaning

# STEP 1: Load Data
import pandas as pd

print("Loading data...")

df = pd.read_excel(
    "../Data/Competitor_Pricing_Dataset (uncleaned).xlsx",
    sheet_name="Raw Data",
    header=2
)

print("Data loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# STEP 2: Inspect Data
print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nNull Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

# STEP 3: Clean Data
print("\nCleaning Data...")

df.drop_duplicates(inplace=True)
print("Duplicates removed!")

text_columns = [
    "Country", "Currency", "Brand", "Brand_Type",
    "Category", "Segment", "Season", "Stock_Status",
    "Online_Available", "In_Store_Available", "Data_Source"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

print("Extra spaces removed!")

for col in text_columns:
    df[col] = df[col].str.title()

print("Text standardized!")

# Fix Country Names
country_mapping = {
    "Us": "USA",
    "Uk": "UK",
    "Uae": "UAE"
}

df["Country"] = df["Country"].replace(country_mapping)

print("Country names fixed!")
print("Unique countries:", df["Country"].unique())

# Fix Currency Codes
currency_mapping = {
    "Usd": "USD",
    "Gbp": "GBP",
    "Eur": "EUR",
    "Aed": "AED",
    "Inr": "INR",
    "Aud": "AUD"
}

df["Currency"] = df["Currency"].replace(currency_mapping)

print("Currency codes fixed!")
print("Unique currencies:", df["Currency"].unique())

print("\nCleaning Done!")
print("Rows after cleaning:", df.shape[0])

# STEP 4: Convert Currencies to USD
print("\nConverting prices to USD...")

exchange_rates = {
    "USD": 1.00,
    "GBP": 1.27,
    "EUR": 1.08,
    "AED": 0.27,
    "INR": 0.012,
    "AUD": 0.65
}

df["Original_Price_USD"] = (
    df["Original_Price"] * df["Currency"].map(exchange_rates)
).round(2)

df["Discounted_Price_USD"] = (
    df["Discounted_Price"] * df["Currency"].map(exchange_rates)
).round(2)

print("Prices converted to USD!")

print(
    df[
        [
            "Country",
            "Currency",
            "Original_Price",
            "Original_Price_USD"
        ]
    ].head(5)
)

# Verify conversion
null_check = df[
    [
        "Original_Price_USD",
        "Discounted_Price_USD"
    ]
].isnull().sum()

print("\nNull check after conversion:")
print(null_check)

# STEP 5: Fix Column Names & Export
print("\nExporting clean data...")

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.columns = df.columns.str.strip()

df = df.rename(
    columns={
        "Discount_%": "Discount_Percent"
    }
)

print("\nFinal Data Summary:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print(
    "Unique Brands:",
    df["Brand"].nunique(),
    "→",
    df["Brand"].unique()
)

print(
    "Unique Countries:",
    df["Country"].nunique(),
    "→",
    df["Country"].unique()
)

print(
    "Unique Categories:",
    df["Category"].nunique()
)

print(
    "Unique Currencies:",
    df["Currency"].unique()
)

# Export CSV
df.to_csv(
    "../Output/clean_pricing_data.csv",
    index=False
)

print("\nFile exported successfully!")
print("Location: Output/clean_pricing_data.csv")
print("Final Rows:", df.shape[0])
print("Final Columns:", df.shape[1])

print("\n✅ Python Cleaning Complete — Ready for MySQL!")