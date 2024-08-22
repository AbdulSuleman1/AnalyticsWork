import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
file = pd.read_csv("qc_public-sector_nga.csv")
my_file = pd.DataFrame(file)
my_file.loc[0,"Country ISO3"] = "Country Code"
my_file.loc[0,"Year"] = "year"
my_file.loc[0,"Indicator Code"] = "Indicator Code"
my_file.loc[0,"Value"] = "Indicator value"

dat = pd.DataFrame(my_file)
dat1 = dat.iloc[:,[1,-1]]
print(dat1)
dat1.drop(index =[0], inplace=True)
show = dat1.head(3)
sortedvalue = show.sort_values(["Year","Value"],ascending= False)
print(sortedvalue)
show1 = pd.DataFrame(sortedvalue)
print(show1)
# print(show1.corr())
# # histogram
plt.hist(x=show1['Year'],y=show1['Value'],bins= np.arange(0,1100,46))
# show1["Value"].hist(bins= 5,alpha=0.5,label='Year')
# show1["Year"].hist(bins= 5,alpha=0.5,label='Year')
# plt.hist(x=show1['Year'],y=show1['Value'])
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.legend()

# #piechart
# pie=plt.pie(show1["Year"])
# print(pie)
 #linegraph
# plt.plot(show1["Year"],show1["Value"])
# plt.xlabel("Year")
# plt.ylabel("Value")


# #sn.histplot(x = "Year",y="Value", data=show1  )
# #scatterplot
# # plt.scatter(x= show1 ["Year"], y= show1 ["Value"], s =5, c= "r" )
# # plt.xlabel("Year")
# # plt.ylabel("Value")
# #plt.grid()

plt.show()

#show = plt.plot("year","Indicator value")
#print(show.head(31))



