import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sales.csv")
#print(df)

df['Revenue']=df['Quantity']*df['Rate']
print(" Data with revenue: ")
#print(df)

total_revenue = df['Revenue'].sum()
print(f"\nTotal Revenue from all prducts: {total_revenue}\n")

print("Sorting all products by revenue ")
products = df.sort_values(by='Revenue', ascending=False) # sorts all the products by revenue in decending order
print(products[['Product','Revenue']]) # in descending form prints product and revenue
print("\n")

print("The Top product that got the highest revenue is: ")
top_product=products.iloc[0]
print("Product: ",top_product['Product'])
print("Revenue: ", top_product['Revenue'])


each_unit_revenue=df.groupby('Unit')['Revenue'].sum() # this groups the df by the unit type eg: kg, pice, packet and does the sum of revenue in each group
unit_revenue=each_unit_revenue.sort_values( ascending=False) # this makes the above series data in descending form 
print("\nRevenue per unit type:")
print(unit_revenue) # prints the unit and the total revenue

each_type_revenue=df.groupby('Type')['Revenue'].sum().sort_values(ascending=False)
print("\n Revenues Per type:")
print(each_type_revenue) # here we can group item by type and see on only one column i.e. revenue only and we can play only with it
#We grouped by 'Type', We summed the 'Revenue' column, so each_type_revenue.name == 'Revenue'
# i.e the name of this each_type_revenue series is revenue



# but here in .agg(), we group item by type same as above but we can see different columns we want in the same function and we can play with any columns we want in the same function
type_summary = df.groupby('Type').agg(
    Total_Quantity = ('Quantity', 'sum'),
    Average_Rate = ('Rate','sum'),
    Total_Revenue = ('Revenue','sum')       
    )
type_summary=type_summary.sort_values(by='Total_Revenue', ascending = False)
print("\nSales Summary by Type:")
print(type_summary)


# Top 10 products by revenue
plt.figure(figsize=(10,6)) # inside this frame of matplotlib sns barplot s drawn
sns.barplot(x='Revenue', y='Product', data=products.head(10), palette='Set1')
plt.title("Top 10 products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()

# Revenue by Type (pie chart)
plt.figure(figsize=(6,6))
each_type_revenue.plot(kind='pie', autopct='%.2f%%') # each_type_revenue is a pandas series so when we use .plot(kind='pie), we dont need to worry about labels(veggies,granins,fruits) in the pie chart, it adds this itself 
    #plt.pie(each_type_revenue.values, labels=each_type_revenue.index, autopct='%.2f%%') 
    # we can aslo do this, here we have to specify labels ourselves
plt.ylabel("") # we needed this because while doing .plot, we get revenue as the ylabel itself, what it does is: labels=each_type_revenue.index and ylabel=series name which is revenue in our case
# to remove this problem of ylabel we can directly use plt.pie() also
plt.title("Revenue share by each type")
plt.show()