# Step 1 Importing necessary libaraies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2 Create the dataframe 

df1 = pd.read_csv('C:/Users/Rahul Prashar/Downloads/Zomato-data-.csv')
print(df1.head())   # Printing first five rows from starting
print(df1.tail())   # Printing last five rows from below

# Step 3 Check for summary of dataframe

print(df1.info())

# Step 4 Check for null values all the columns

print(df1.isnull().sum())

# Step 5  Cleaning the column ratings by removing the part of denominator and slash sign

def clean(value):
     value = str(value).split('/')
     value = value[0]
     return float(value)

df1['rate'] = df1['rate'].apply(clean)  # Individual column manipulation
print(df1['rate'])                      # verifying the results

# Step 6  Exploring different data columns
print(df1['name'].unique)  # In this i am referencing the method but not calling it 
print(df1['name'].unique()) # In this i am calling the method and it is executing

sns.countplot(x=df1['name'])    # Not necessary to plot this beacuse we donot have any common values
plt.xlabel('Name of resturant')
plt.show()

sns.countplot(x=df1['online_order'])  # Also , all columns except Type of restaurant does not give meaningful insights .
plt.xlabel("Online order")
plt.show()

sns.countplot(x=df1['book_table'])
plt.xlabel('Book a Table')
plt.show()

sns.countplot(x=df1['rate'])
plt.xlabel('Ratings')
plt.show()

sns.countplot(x=df1['votes'])
plt.xlabel('votes')
plt.show()

sns.countplot(x=df1['approx_cost(for two people)'])
plt.xlabel('Approximate Cost for two people') 
plt.show()                                                
            # Countplot is used for visulising categorical data and not the numerical data.
            # The countplot is ideal choice for plotiing the listed_in type column beacuse it has categorical data

sns.countplot(x=df1['listed_in(type)'])  # Only this column  is giving meaningful insight 
plt.xlabel = 'Type of restaurant'
plt.show()

# Conclusion : Most of the resturants fall into Dining Category

# Step 6  Which category of reataurants are preffered by large number of individuals

grouped_data = df1.groupby('listed_in(type)')['votes'].sum()  # used group by to group the similar data on the basis of votes column
result = pd.DataFrame({'votes': grouped_data})

# Plotting the data                                     
plt.plot(result.index, result['votes'], c="green", marker="o")  # Plot function is used for plotting the numerical data 
plt.title("Votes according to restaurant")
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.show()       # Conclusion : Dining restaurants are preferred by large number of individuals
          
# Step 7 : Determine restaurant's name that got maximum no of votes based on dataframe given

max_votes= df1['votes'].max()
resturant_maxvotes = df1.loc[df1['votes'] == max_votes,'name']
print("Restaurant with maximum votes",resturant_maxvotes)

min_votes = df1['votes'].min()
resturant_minvotes = df1.loc[df1['votes'] == min_votes,'name']
print('Resturant wiht minimum votes',resturant_minvotes)

# Step 8  Exploring the online order column
sns.countplot(x=df1['online_order'])   # From visulaisation , it shows majoity of resturants doesnot accept Online Orders
plt.show()

# Step 9 : Exploring the rate column

plt.hist(df1['rate'],bins=5)   # Since we cannot get any insights from the above plotting by plotting it as countplot
plt.title('Ratings Distribution')  # We plotted this as histogram , since the data in rate column is continous numerical data
plt.show()                        # For plotting continous numerical data , we have to plot it using histogram

# Conclusion : Majority of the resturants received the rating in between 3.5 to 4

# Step 10 Lets explore the appproximate cost for two people column

sns.countplot(x=df1['approx_cost(for two people)'])
#plt.xlabel('Approximate Cost for two people') 
plt.show()   # Conclusion : Majority of the couples prefer restaurants with an approximate cost of 300 INR

# Step 11 Explore while online orders receive higher ratings than offline orders

plt.figure(figsize=(6,6))
sns.boxplot(x= 'online_order',y='rate', data = df1)
plt.show()

# Conclusion : Offline orders remain lower ratings in comparison to online orders which gained highest ratings

# Step  11 Undertanding the data more using Heatmap

pivot_table = df1.pivot_table(index='listed_in(type)',columns = 'online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
#plt.xlabel("Online Order")
#plt.ylabel("Listed In (Type)")
plt.show()

# Conclusion : Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders. This suggests that clients prefer to place orders in person at restaurants, but prefer online ordering at cafes.



