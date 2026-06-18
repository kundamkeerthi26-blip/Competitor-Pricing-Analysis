CREATE DATABASE competitor_pricing;
USE  competitor_pricing;

CREATE DATABASE competitor_pricing;
USE competitor_pricing;

CREATE TABLE Pricing_Data (
    Row_ID INT,
    Country VARCHAR(50),
    Currency VARCHAR(20),
    Brand VARCHAR(100),
    Brand_Type VARCHAR(50),
    Category VARCHAR(100),
    Segment VARCHAR(100),
    Season VARCHAR(100),
    Original_Price DECIMAL(10,2),
    Discount_Percent INT,
    Discounted_Price DECIMAL(10,2),
    Stock_Status VARCHAR(50),
    Online_Available VARCHAR(10),
    In_Store_Available VARCHAR(10),
    Data_Source VARCHAR(100),
    Collection_Date DATE,
    Original_Price_USD DECIMAL(10,2),
    Discounted_Price_USD DECIMAL(10,2)
);


SELECT * FROM pricing_data
LIMIT 10;


