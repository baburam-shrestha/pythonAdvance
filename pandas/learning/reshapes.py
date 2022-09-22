from cmath import pi
import pandas as pd

titanic = pd.read_csv("titanic.csv")
print(titanic.head())

air_quality = pd.read_csv("air_quality.csv")
print(air_quality.head())

# Sort table rows
# I want to sort the Titanic data according to the age of the passengers.
print(titanic.sort_values(by="Age").head())

print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head())

no2=air_quality[air_quality["parameter"] == "no2"]
print(no2)

no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)


# Pivot table

# I want the mean concentrations for and  in each of the stations in table form.

pivot=air_quality.pivot_table( values="values", index="location", columns="parameter", aggfunc="mean")
print(pivot)

pivot_tbl=air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
)
print(pivot_tbl)


# REMEMBER
# Sorting by one or more columns is supported by sort_values.
# The pivot function is purely restructuring of the data, pivot_table supports aggregations.
# The reverse of pivot (long to wide format) is melt (wide to long format).