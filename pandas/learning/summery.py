# Titanic data
# This tutorial uses the Titanic data set, stored as CSV. The data consists of the following data columns:
#     PassengerId: Id of every passenger.
#     Survived: Indication whether passenger survived. 0 for yes and 1 for no.
#     Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
#     Name: Name of passenger.
#     Sex: Gender of passenger.
#     Age: Age of passenger in years.
#     SibSp: Number of siblings or spouses aboard.
#     Parch: Number of parents or children aboard.
#     Ticket: Ticket number of passenger.
#     Fare: Indicating the fare.
#     Cabin: Cabin number of passenger.
#     Embarked: Port of embarkation.
from statistics import mean
import pandas as pd
titanic = pd.read_csv("titanic.csv")
heads=titanic.head()
print(heads)

# Aggregating statistics
# What is the average age of the Titanic passengers?
mean_age=titanic["Age"].mean()
print(mean_age)

# What is the median age and ticket fare price of the Titanic passengers?
medain_age_fare=titanic[["Age", "Fare"]].median()
print(medain_age_fare)

# describe of titanic about Age and Fare
age_fare=titanic[["Age", "Fare"]].describe()
print(age_fare)

# Instead of the predefined statistics, 
# specific combinations of aggregating statistics for given columns can be defined using the DataFrame.agg() method:

aggregate=titanic.agg(
    {
        "Age": ["min", "max", "median", "skew", "mean"],
        "Fare": ["min", "max", "median", "skew", "mean"],
    }
)
print(aggregate)

# What is the average age for male versus female Titanic passengers?
average_age=titanic[["Sex", "Age"]].groupby("Sex").mean()
print(average_age)
# or
avg_age=titanic.groupby("Sex")["Age"].mean()
print(avg_age)

# Count number of records by category
# What is the number of passengers in each of the cabin classes?
number=titanic["Pclass"].value_counts()
print(number)
# or
number=titanic.groupby("Pclass")["Pclass"].count()
print(number)

# REMEMBER
# Aggregation statistics can be calculated on entire columns or rows.
# groupby provides the power of the split-apply-combine pattern.
# value_counts is a convenient shortcut to count the number of entries in each category of a variable.