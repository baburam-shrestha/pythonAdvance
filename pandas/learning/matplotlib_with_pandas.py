# create plots in pandas
# importing pandas as pd
import pandas
#importing matplotlib. pyplot as plt
import matplotlib.pyplot as plt

#The usage of the index_col and parse_dates parameters of the read_csv function to define the first column 
# as index of the resulting DataFrame and convert the dates in the column to Timestamp objects,respectively.
air_quality = pandas.read_csv("air_quality.csv", index_col=0, parse_dates=True)
heads=air_quality.head()
print(heads)

air_quality.plot() # ploting the air_quality data 
plt.show()

air_quality["station_paris"].plot()
plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.8)
plt.show()

air_quality.plot.box()
plt.show()

air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()


# REMEMBER
# The .plot.* methods are applicable on both Series and DataFrames.
# By default, each of the columns is plotted as a different element (line, boxplot,…).
# Any plot created by pandas is a Matplotlib object.

# create new columns derived from existing columns
# check the ratio of the values in Paris versus Antwerp and save the result in a new column.

air_quality["sum_of_3_station"] = (air_quality["station_london"]+air_quality["station_paris"]+ air_quality["station_antwerp"])
heads=air_quality.head()
print(heads)