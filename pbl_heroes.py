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
purchaseCount = purchaseData['Purchase ID'].count()
print('Total number of purchases: ' + str(purchaseCount))
# * Total Revenue
print('Total revenue: $' + str(round(purchaseData['Price'].sum(),2)))

#%%

### Gender Demographics
print('Gender Demographics','\n-------------------')
# * Percentage and Count of Male Players
malePlayerCount = len(purchaseData['SN'].loc[purchaseData['Gender']=='Male'].unique())
print('Male (count): ' + str(malePlayerCount))
malePlayerPercentage = malePlayerCount / playerCount
print('Male (percentage): ' + str(round(malePlayerPercentage,4)*100) + ' %')

# * Percentage and Count of Female Players
femalePlayerCount = len(purchaseData['SN'].loc[purchaseData['Gender']=='Female'].unique())
print('Female (count): ' + str(femalePlayerCount))
femalePlayerPercentage = femalePlayerCount / playerCount
print('Female (percentage): ' + str(round(femalePlayerPercentage,4)*100) + ' %')

# * Percentage and Count of Other / Non-Disclosed
otherPlayerCount = playerCount - malePlayerCount - femalePlayerCount
print('Other / Non-Disclosed (count): ' + str(otherPlayerCount))
otherPlayerPercentage = otherPlayerCount / playerCount
print('Other / Non-Disclosed (percentage): ' + str(round(otherPlayerPercentage,4)*100) + ' %')

#%%
### Purchasing Analysis (Gender)
print('Purchasing Analysis (Gender)','\n----------------------------')
# * The below each broken by gender
#  * Purchase Count
malePurchaseCount = purchaseData['Purchase ID'].loc[purchaseData['Gender']=='Male'].count()
femalePurchaseCount = purchaseData['Purchase ID'].loc[purchaseData['Gender']=='Female'].count()
otherPurchaseCount = purchaseData['Purchase ID'].loc[(purchaseData['Gender']!='Female') & (purchaseData['Gender']!='Male')].count()
print('Purchase Count','\n    Male: ' + str(malePurchaseCount) + '\n    Female: ' + str(femalePurchaseCount) + '\n    Other / Non-Disclosed: ' + str(otherPurchaseCount))

#  * Average Purchase Price
maleAveragePurchasePrice = purchaseData['Price'].loc[purchaseData['Gender']=='Male'].mean()
femaleAveragePurchasePrice = purchaseData['Price'].loc[purchaseData['Gender']=='Female'].mean()
otherAveragePurchasePrice = purchaseData['Price'].loc[(purchaseData['Gender']!='Female') & (purchaseData['Gender']!='Male')].mean()
print('\nAverage Purchase Price','\n    Male: $' + str(round(maleAveragePurchasePrice,2)) + '\n    Female: $' + str(round(femaleAveragePurchasePrice,2)) + '0' + '\n    Other / Non-Disclosed: $' + str(round(otherAveragePurchasePrice,2)))

#  * Total Purchase Value
maleTotalPurchaseValue = purchaseData['Price'].loc[purchaseData['Gender']=='Male'].sum()
femaleTotalPurchaseValue = purchaseData['Price'].loc[purchaseData['Gender']=='Female'].sum()
otherTotalPurchaseValue = purchaseData['Price'].loc[(purchaseData['Gender']!='Female') & (purchaseData['Gender']!='Male')].sum()
print('\nTotal Purchase Value','\n    Male: $' + str(round(maleTotalPurchaseValue,2)) + '\n    Female: $' + str(round(femaleTotalPurchaseValue,2)) + '\n    Other / Non-Disclosed: $' + str(round(otherTotalPurchaseValue,2)))

#  * Average Purchase Total per Person by Gender

#%%
