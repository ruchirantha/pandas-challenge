#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
purchase_data = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data_df = pd.read_csv(purchase_data)
purchase_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


players_df = purchase_data_df.groupby("SN")["SN"].nunique()
players_df.count()


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


#Number of unique items

items_df = purchase_data_df.groupby("Item Name")["Item Name"].nunique()
items_df.count()


# In[4]:


average_price_df = purchase_data_df["Price"].mean()
average_price_df


# In[5]:


#Total number of purchases

total_purchases_df = len(purchase_data_df)
total_purchases_df


# In[6]:


# Total Revenue

total_revenue_df = purchase_data_df["Price"].sum()
total_revenue_df


# In[7]:


# Summary

purchasing_analysis_df = pd.DataFrame({"Number of Unique Items":[items_df],"Average Purchase Price":[average_price_df],
                                     "Total Number of Purchases":[total_purchases_df],"Total Revenue":[total_revenue_df]})
purchasing_analysis_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[8]:


# Gender Count
gender_count_df = purchase_data_df.groupby("Gender")["SN"].nunique()
gender_count_df.head()


# In[9]:


# Gender Percentage
gender_percentage_df = gender_count_df/players_df.count()
gender_percentage_df.round(2)


# In[10]:


#Summary Gender demographics

gender_demographics_df = pd.DataFrame({"Gender Count": gender_count_df,"Gender Percentage":gender_percentage_df})
gender_demographics_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[11]:


#Total number of purchases by gender

gender_purchases_df = purchase_data_df.groupby("Gender")["Item Name"]
gender_purchases_df.count()


# In[12]:


# Average price of items by gender

gender_average_df = purchase_data_df.groupby("Gender")["Price"].mean()
gender_average_df


# In[13]:


#Total Purchase value by gender

gender_total_df = purchase_data_df.groupby("Gender")["Price"].sum()
gender_total_df


# In[14]:


#Avg Total Purchase per Person

normalized_gender_total_df = gender_total_df/gender_count_df
normalized_gender_total_df.round


# In[15]:


# Purchasing analysis DataFrame by gender

gender_analysis_df = pd.DataFrame({"Purchase Count":gender_purchases_df, "Average Purchase Price":gender_average_df,
                                   "Total Purchase Value":gender_total_df,"Normalized Totals":normalized_gender_total_df})
gender_analysis_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[16]:


#Establishing bins
bins = [0,10,15,20,25,30,35,40, 45]
age_ranges = ["<10", "10-14","15-19", "20-24", "25-29", "30-34", "35-39", ">=40"]


# In[17]:


#cut
pd.cut(purchase_data_df["Age"], bins, labels=age_ranges)


# In[18]:


purchase_data_df["Age Range"] = pd.cut(purchase_data_df["Age"], bins, labels= age_ranges)
purchase_data_df.head()


# In[20]:


#Percentage by age range
age_group_percentage_df = round(purchase_data_df["Age Range"].value_counts()/total_purchases_df,2)
age_group_percentage_df


# In[22]:


# Purchase count by age range

age_group_count_df = purchase_data_df.groupby("Age Range")["Item Name"]
age_group_count_df.count()


# In[23]:


# Average purchase price by age range

age_group_average_df = purchase_data_df.groupby("Age Range")["Price"].mean()
age_group_average_df.round(2)


# In[25]:


#Total purchase value by age range

age_group_total_df = purchase_data_df.groupby("Age Range")["Price"].sum()
age_group_total_df


# In[35]:


#Normalized totals by age range.

normalized_age_total_df = age_group_total_df/576
normalized_age_total_df.round(2)


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[37]:


# Purchasing analysis DataFrame by age range
age_range_df = pd.DataFrame({"Purchase Count":age_group_count_df,"Average Purchase Price":age_group_average_df,
                            "Total Purchase Value": age_group_total_df,"Normalized Totals": normalized_age_total_df})
age_range_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[39]:


#Top spenders analysis

players_purchase_count_df = purchase_data_df.groupby("SN").count()["Price"].rename("Purchase Count")
players_average_price_df = purchase_data_df.groupby("SN").mean()["Price"].rename("Average Purchase Price")
players_total_df = purchase_data_df.groupby("SN").sum()["Price"].rename("Total Purchase Value")

#DataFrame

total_user_data_df = pd.DataFrame({"Purchase Count":players_purchase_count_df,"Average Purchase Price": players_average_price_df,
                                   "Total Purchase Value": players_total_df})
total_user_data_df.head()


# In[40]:


# Top five spenders

top_five_spenders = total_user_data_df.sort_values("Total Purchase Value", ascending=False)
top_five_spenders.head()


# In[41]:


# Total items purchases analysis

items_purchase_count_df = purchase_data_df.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")
items_average_price_df = purchase_data_df.groupby(["Item ID", "Item Name"]).mean()["Price"].rename("Average Purchase Price")
items_value_total_df = purchase_data_df.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")

# DataFrame

items_purchased_df = pd.DataFrame({"Purchase Count":items_purchase_count_df,"Item Price":items_average_price_df,
                                   "Total Purchase Value":items_value_total_df,})

items_purchased_df.head()


# In[ ]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[44]:


# 5 most popular items
most_popular_items_df = items_purchased_df.sort_values("Purchase Count", ascending=False)
most_popular_items_df.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[49]:


# five the most profitable items.

most_profitable_items_df = items_purchased_df.sort_values("Total Purchase Value", ascending=False)
most_profitable_items_df.head()

