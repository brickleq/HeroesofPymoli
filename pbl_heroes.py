#%%
'''

### Player Count

* Total Number of Players

### Purchasing Analysis (Total)

* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue

### Gender Demographics

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed

### Purchasing Analysis (Gender)

* The below each broken by gender
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Average Purchase Total per Person by Gender

### Age Demographics

* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Average Purchase Total per Person by Age Group

### Top Spenders

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value

### Most Popular Items

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value

### Most Profitable Items

* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value

As final considerations:

* You must use the Pandas Library and the Jupyter Notebook.
* You must submit a link to your Jupyter Notebook with the viewable Data Frames.
* You must include a written description of three observable trends based on the data.
* See [Example Solution](HeroesOfPymoli/HeroesOfPymoli_starter.ipynb) for a reference on expected format.
'''
##%
# Dependencies
import numpy as np
import pandas as pd
#%%
purchaseData = pd.DataFrame
csvfile = 'HeroesOfPymoli/Resources/purchase_data.csv'
purchaseData = pd.read_csv(csvfile, delimiter=',', encoding="utf-8")
purchaseData.head()
#%%
### Player Count
# * Total Number of Players
playerCount = len(purchaseData['SN'].unique())
print('Player count: ' + str(playerCount))
#%%
### Purchasing Analysis (Total)
print('Purchasing Analysis','\n-------------------')
# * Number of Unique Items
uniqueItems = len(purchaseData['Item ID'].unique())
print('Number of unique items: ' + str(uniqueItems))
# * Average Purchase Price
averagePurchasePrice = purchaseData['Price'].mean()
print('Average purchase price: $' + str(round(averagePurchasePrice,2)))
# * Total Number of Purchases
totalPurchases = purchaseData['Purchase ID'].count()
print('Total number of purchases: ' + str(totalPurchases))
# * Total Revenue
print('Total revenue: $' + str(round(purchaseData['Price'].sum(),2)))

#%%

### Gender Demographics
print('Gender Demographics','\n-------------------')
# * Percentage and Count of Male Players
malePlayerCount = len(purchaseData['SN'].loc[purchaseData['Gender']=='Male'].unique())
print('Male players (count): ' + str(malePlayerCount))
malePlayerPercentage = malePlayerCount / playerCount
print('Male players (percentage): ' + str(round(malePlayerPercentage,4)*100) + '%')
#%%
# * Percentage and Count of Female Players
femalePlayerCount = len(purchaseData['SN'].loc[purchaseData['Gender']=='Female'].unique())

print('Female players (count): ' + str(femalePlayerCount,2))

# * Percentage and Count of Other / Non-Disclosed


#%%
