##%
# Dependencies
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
maleAveragePurchaseTotal = maleTotalPurchaseValue / malePlayerCount
femaleAveragePurchaseTotal = femaleTotalPurchaseValue / femalePlayerCount
otherAveragePurchaseTotal = otherTotalPurchaseValue / otherPlayerCount
print('\nAverage Purchase Total per Person by Gender','\n    Male: $' + str(round(maleAveragePurchaseTotal,2)) + '\n    Female: $' + str(round(femaleAveragePurchaseTotal,2)) + '\n    Other / Non-Disclosed: $' + str(round(otherAveragePurchaseTotal,2)))

#%%
### Age Demographics
# * The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
print('Age Demographics','\n----------------\n')
#  * Purchase Count
print('Purchase Count')
print('     < 10: ' + str(purchaseData['Purchase ID'].loc[purchaseData['Age']<10].count()))
print('    10-14: ' + str((purchaseData['Purchase ID'].loc[(purchaseData['Age']>9) & (purchaseData['Age']<15)].count())))
print('    15-19: ' + str((purchaseData['Purchase ID'].loc[(purchaseData['Age']>14) & (purchaseData['Age']<20)].count())))
print('    20-24: ' + str((purchaseData['Purchase ID'].loc[(purchaseData['Age']>19) & (purchaseData['Age']<25)].count())))
print('    25-29: ' + str((purchaseData['Purchase ID'].loc[(purchaseData['Age']>24) & (purchaseData['Age']<30)].count())))
print('    30-34: ' + str((purchaseData['Purchase ID'].loc[(purchaseData['Age']>29) & (purchaseData['Age']<35)].count())))
print('    35-39: ' + str((purchaseData['Purchase ID'].loc[(purchaseData['Age']>34) & (purchaseData['Age']<40)].count())))
print('    40-44: ' + str((purchaseData['Purchase ID'].loc[(purchaseData['Age']>39) & (purchaseData['Age']<45)].count())))
print('     > 44: '  + str(purchaseData['Purchase ID'].loc[purchaseData['Age']>44].count()))
#%%
#  * Average Purchase Price
print('\nAverage Purchase Price')
avgPrice = purchaseData['Price'].loc[purchaseData['Age']<10].mean()
print('     < 10: $' + str(round(avgPrice,2)))
avgPrice = purchaseData['Price'].loc[(purchaseData['Age']>9) & (purchaseData['Age']<15)].mean()
print('    10-14: $' + str(round(avgPrice,2)))
avgPrice = purchaseData['Price'].loc[(purchaseData['Age']>14) & (purchaseData['Age']<20)].mean()
print('    15-19: $' + str(round(avgPrice,2)))
avgPrice = purchaseData['Price'].loc[(purchaseData['Age']>19) & (purchaseData['Age']<25)].mean()
print('    20-24: $' + str(round(avgPrice,2)))
avgPrice = purchaseData['Price'].loc[(purchaseData['Age']>24) & (purchaseData['Age']<30)].mean()
print('    25-29: $' + str(round(avgPrice,2)) + '0')
avgPrice = purchaseData['Price'].loc[(purchaseData['Age']>29) & (purchaseData['Age']<35)].mean()
print('    30-34: $' + str(round(avgPrice,2)))
avgPrice = purchaseData['Price'].loc[(purchaseData['Age']>34) & (purchaseData['Age']<40)].mean()
print('    35-39: $' + str(round(avgPrice,2)) + '0')
avgPrice = purchaseData['Price'].loc[(purchaseData['Age']>39) & (purchaseData['Age']<45)].mean()
print('    40-44: $' + str(round(avgPrice,2)))
avgPrice = purchaseData['Price'].loc[purchaseData['Age']>44].mean()
print('     > 44: $' + str(round(avgPrice,2)) + '0')

#%%
#  * Total Purchase Value
print('\nTotal Purchase Value')
sumPrice = purchaseData['Price'].loc[purchaseData['Age']<10].sum()
print('     < 10: $' + str(round(sumPrice,2)))
sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>9) & (purchaseData['Age']<15)].sum()
print('    10-14: $' + str(round(sumPrice,2)))
sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>14) & (purchaseData['Age']<20)].sum()
print('    15-19: $' + str(round(sumPrice,2)))
sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>19) & (purchaseData['Age']<25)].sum()
print('    20-24: $' + str(round(sumPrice,2)))
sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>24) & (purchaseData['Age']<30)].sum()
print('    25-29: $' + str(round(sumPrice,2)) + '0')
sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>29) & (purchaseData['Age']<35)].sum()
print('    30-34: $' + str(round(sumPrice,2)) + '0')
sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>34) & (purchaseData['Age']<40)].sum()
print('    35-39: $' + str(round(sumPrice,2)))
sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>39) & (purchaseData['Age']<45)].sum()
print('    40-44: $' + str(round(sumPrice,2)))
sumPrice = purchaseData['Price'].loc[purchaseData['Age']>44].sum()
print('     > 44: $' + str(round(sumPrice,2)) + '0')

#%%
#  * Average Purchase Total per Person by Age Group
print('\nAverage Purchase Total per Person by Age Group')
sumPrice = purchaseData['Price'].loc[purchaseData['Age']<10].sum()
playerCountAge = len(purchaseData['SN'].loc[purchaseData['Age']<10].unique())
avgPrice = sumPrice / playerCountAge
print('     < 10: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>9) & (purchaseData['Age']<15)].sum()
playerCountAge = len(purchaseData['SN'].loc[purchaseData['Age']<10].unique())
avgPrice = sumPrice / playerCountAge
print('    10-14: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>14) & (purchaseData['Age']<20)].sum()
playerCountAge = len(purchaseData['SN'].loc[(purchaseData['Age']>14) & (purchaseData['Age']<20)].unique())
avgPrice = sumPrice / playerCountAge
print('    15-19: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>19) & (purchaseData['Age']<25)].sum()
playerCountAge = len(purchaseData['SN'].loc[(purchaseData['Age']>19) & (purchaseData['Age']<25)].unique())
avgPrice = sumPrice / playerCountAge
print('    20-24: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>24) & (purchaseData['Age']<30)].sum()
playerCountAge = len(purchaseData['SN'].loc[(purchaseData['Age']>24) & (purchaseData['Age']<30)].unique())
avgPrice = sumPrice / playerCountAge
print('    25-29: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>29) & (purchaseData['Age']<35)].sum()
playerCountAge = len(purchaseData['SN'].loc[(purchaseData['Age']>29) & (purchaseData['Age']<35)].unique())
avgPrice = sumPrice / playerCountAge
print('    30-34: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>34) & (purchaseData['Age']<40)].sum()
playerCountAge = len(purchaseData['SN'].loc[(purchaseData['Age']>34) & (purchaseData['Age']<40)].unique())
avgPrice = sumPrice / playerCountAge
print('    35-39: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[(purchaseData['Age']>39) & (purchaseData['Age']<45)].sum()
playerCountAge = len(purchaseData['SN'].loc[(purchaseData['Age']>39) & (purchaseData['Age']<45)].unique())
avgPrice = sumPrice / playerCountAge
print('    40-44: $' + str(round(avgPrice,2)))

sumPrice = purchaseData['Price'].loc[purchaseData['Age']>44].sum()
playerCountAge = len(purchaseData['SN'].loc[purchaseData['Age']>44].unique())
avgPrice = sumPrice / playerCountAge
print('     > 44: $' + str(round(avgPrice,2)) + '0')

#%%
### Top Spenders

# * Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
#   * SN
#   * Purchase Count
#   * Average Purchase Price
#   * Total Purchase Value

purchaseCount = purchaseData.groupby(['SN']).count()['Price'].rename('Purchase Count')
purchaseCount.head()
purchaseValue = purchaseData.groupby(['SN']).sum()['Price'].rename('Total Purchase Value')
purchaseValue.head()
averagePurchase = purchaseData.groupby(['SN']).mean()['Price'].rename('Average Purchase Price')
averagePurchase.head()

topSpenders = pd.DataFrame({'Purchase Count':purchaseCount,
'Total Purchase Value': purchaseValue,
'Average Purchase Price': averagePurchase})
topSpenders.sort_values(['Total Purchase Value'], ascending=False).head()

#%%
### Most Popular Items

# * Identify the 5 most popular items by purchase count, then list (in a table):
#   * Item ID
#   * Item Name
#   * Purchase Count
#   * Item Price
#   * Total Purchase Value

popularItemsCount = purchaseData.groupby(['Item Name']).count()['Item ID'].rename('Purchase Count')
popularItemsPrice = purchaseData.groupby(['Item Name']).count()['Price'].rename('Item Price')
popularItemsValue = purchaseData.groupby(['Item Name']).sum()['Price'].rename('Total Purchase Value')
mostPopularItems = pd.DataFrame({'Purchase Count': popularItemsCount,
'Item Price': popularItemsPrice,
'Total Purchase Value': popularItemsValue})
mostPopularItems.sort_values(['Purchase Count'], ascending=False).head()


#%%
### Most Profitable Items

# * Identify the 5 most profitable items by total purchase value, then list (in a table):
#   * Item ID
#   * Item Name
#   * Purchase Count
#   * Item Price
#   * Total Purchase Value
mostProfitableItems = pd.DataFrame({'Purchase Count': popularItemsCount,
'Item Price': popularItemsPrice,
'Total Purchase Value': popularItemsValue})
mostProfitableItems.sort_values(['Total Purchase Value'], ascending=False).head()