**Zomato Dataset Analysis**
This project involves analyzing the Zomato restaurant dataset to derive insights regarding various restaurant attributes, customer ratings, and preferences. The analysis includes exploring multiple aspects of restaurant data, such as ratings, online ordering options, and approximate costs, as well as visualizing trends and patterns.

**Steps Involved:**
Data Importing and Inspection:
The dataset is loaded from a CSV file, and basic information about the data is printed to examine the first and last few rows, along with a summary of the data columns.

**Handling Missing Data:**
The script checks for missing values in each column and prepares the dataset for further analysis.

**Data Cleaning:**
The ratings column is cleaned by removing denominators and the slash sign to standardize the values.

**Exploratory Data Analysis (EDA):**

Various columns are explored to understand the distribution of values.
Visualizations like countplots are used to visualize categorical data such as restaurant names, online orders, table bookings, and ratings.
Insights about the type of restaurant, online ordering habits, and ratings distribution are drawn from visualizations.

**Votes Analysis:**

The dataset is grouped by restaurant types to analyze the total votes and preferences based on votes.

**Analysis of Online Ordering:**

Insights into which restaurants accept online orders and how this impacts customer ratings are explored.
A boxplot visualizes the rating distribution based on whether online ordering is available.

**Cost Analysis:**

The dataset is analyzed for approximate cost data to determine how pricing correlates with customer preferences, with the conclusion that many restaurants fall into the affordable price range for two people.

**Heatmap Visualization:**

A heatmap is generated to show the relationship between restaurant types and the availability of online ordering, revealing trends like cafes primarily offering online ordering while dining restaurants prefer offline orders.
