# California House Price Prediction
![](https://storage.googleapis.com/kaggle-datasets-images/4358371/7486357/d9a83b9309472bbd4ace0100001f7b70/dataset-cover.jpg?t=2024-01-26-14-12-49)

## Project Overview:
The California House Price Prediction project aims to forecast the prices of house in California by leveraging a dataset containing essential house features. The data contains information from the 1990 California census. So although it may not help you with predicting current housing prices. With a total of 56,244 rows and 10 columns, this project seeks to identify the key variables that have the most significant impact on house prices in California of 1990.

## Data Dictionary:

| Variable         | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| Longitude        | geographic coordinate                                                 |
| Latitude         | geographic coordinate                                                 |
| housingMedianAge | Median age of houses in a block                                       |
| totalRooms       | Total number of rooms within a block                                  |
| totalBedrooms    | Total number of bedrooms within a block                               |
| population       | Total number of people residing within a block                        |
| households       | Total number of households for a block                                |
| medianIncome     | Median income for households within a block (in 10000 US$)            |
| medianHouseValue | Median house value for households within a block (in US$) --> TARGET  |
| oceanProximity   | distance from the ocean                                               |

## Key Findings:

Through comprehensive exploratory data analysis and machine learning implementation, several critical insights were discovered:

**Feature Engineering Impact**: The most significant finding was the need to normalize block-level aggregations by household count. Raw totals for rooms, bedrooms, and population were misleading due to varying block sizes. Converting these to per-household ratios revealed meaningful patterns and substantially improved model performance.

**Geographic and Economic Drivers**: The analysis confirmed that median income is the strongest predictor of house values (R² = 0.6 correlation), followed by ocean proximity. Properties near the ocean command significantly higher prices compared to inland locations, with the distinction being more binary (coastal vs. inland) rather than granular proximity levels.

**Model Performance**: The Random Forest Regressor emerged as the optimal model, achieving:
- **R² Score**: 0.754 (75.4% variance explained)
- **Mean Absolute Error**: 17.1% of average house value
- **Root Mean Squared Error**: 25.1% of average house value

## Impact:

This project provides valuable insights for multiple stakeholders in the real estate market:
- **Real Estate Professionals**: Can leverage the model for property valuation and market analysis
- **Homebuyers**: Gain understanding of key factors affecting property values in California
- **Urban Planners**: Identify geographic and economic patterns in housing markets
- **Investors**: Make data-driven decisions about property investments

The model successfully demonstrates the power of machine learning in real estate analytics while highlighting the importance of thoughtful data preprocessing and domain expertise in building effective predictive models.