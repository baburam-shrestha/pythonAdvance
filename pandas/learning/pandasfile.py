# https://pandas.pydata.org/docs/getting_started/install.html

# importing pandas: To load the pandas package and start working with it, import the package. 
# The community agreed alias for pandas is pd, so loading pandas as pd is assumed standard practice for 
# all of the pandas documentation.
import pandas as pd

# I want to store passenger data of the Titanic. 
# For a number of passengers, I know the name (characters), age (integers) and sex (male/female) data.

#makeing dataframe
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "Baburam Shrestha",
            "asda shrestha",
        ],
        "Age": [22, 35, 58,38,24],
        "Sex": ["male", "male", "female",'male','female'],
    }
)
#printing dataframe df
print(df)
df_descibe= df.describe()
# it returns count, mean, standard deviation, min values, P25,P50,P75, max 

print(df_descibe)
# To manually store data in a table, create a DataFrame. 
# When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values
# in each list as columns of the DataFrame.

# A DataFrame is a 2-dimensional data structure that can store data of different types 
# (including characters, integers, floating point values, categorical data and more) in columns. 
# It is similar to a spreadsheet, a SQL table or the data.frame in R.

# The table has 3 columns, each of them with a column label. 
# The column labels are respectively Name, Age and Sex.

# The column Name consists of textual data with each value a string, 
# the column Age are numbers and the column Sex is textual data.

# In spreadsheet software, the table representation of our data would look very similar:
# When selecting a single column of a pandas DataFrame, the result is a pandas Series. 
# To select the column, use the column label in between square brackets [].

# If you are familiar to Python dictionaries, 
# the selection of a single column is very similar to selection of dictionary values based on the key.

# You can create a Series from scratch as well:
age=[22, 35, 58]
ages = pd.Series(age, name="Age")

# A pandas Series has no column labels, as it is just a single column of a DataFrame. 
# A Series does have row labels.
# Do something with a DataFrame or Series
# I want to know the maximum Age of the passengers
# We can do this on the DataFrame by selecting the Age column and applying max():

max_age=ages.max() # it returns maximum age among ages
print(max_age)

# As illustrated by the max() method, you can do things with a DataFrame or Series. 
# pandas provides a lot of functionalities, each of them a method you can apply to a DataFrame or Series. 
# As methods are functions, do not forget to use parentheses ().

# The describe() method provides a quick overview of the numerical data in a DataFrame. 
# As the Name and Sex columns are textual data, these are by default not taken into account by the describe() method.
# Many pandas operations return a DataFrame or a Series. 
# The describe() method is an example of a pandas operation returning a pandas Series or a pandas DataFrame.

age_describe=ages.describe() 
# it returns count, mean, standard deviation, min values, P25,P50,P75, max 
# and series name and its type
print(age_describe)

age_info = ages.info() # it returns technical details of the ages
print(age_info)

# he method info() provides technical information about a DataFrame, 
# so let’s explain the output in more detail:
    # It is indeed a DataFrame.
    # There are n entries, .
    # Each row has a row label (aka the index) with values ranging from 0 to n-1.
    # The table has m columns. Most columns have a value for each of the rows (all 891 values are non-null). 
    # Some columns do have missing values and less than 891 non-null values.
    # The columns Name, Sex, Cabin and Embarked consists of textual data (strings, aka object). 
    # The other columns are numerical data with some of them whole numbers (aka integer) 
    # and others are real numbers (aka float).
    # The kind of data (characters, integers,…) in the different columns are summarized by listing the dtypes.
    # The approximate amount of RAM used to hold the DataFrame is provided as well.

# REMEMBER
# Import the package, aka import pandas as pd
# A table of data is stored as a pandas DataFrame
# Each column in a DataFrame is a Series
# You can do things by applying a method to a DataFrame or Series

# reading csv file: titanic = pd.read_csv("titanic.csv")
#reading spreedsheet/excel file : titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

#exporting dataframe to excel file: titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

# REMEMBER
# Getting data in to pandas from many different file formats or data sources is supported by read_* functions.
# Exporting data out of pandas is provided by different to_*methods.
# The head/tail/info methods and the dtypes attribute are convenient for a first check.



#select specific columns from a DataFrame
ages = df["Age"] # it doesnot return column name
print(ages)
ages = df[["Age"]]
print(ages)

age_sex = df[["Age", "Sex"]]
print(age_sex)

# filter specific rows from a DataFrame
above_35 = df[df["Age"] > 35]
print(above_35)

male_person=df[df["Sex"]=="male"]
print(male_person)

shape_df=df.shape # it returns (Rows,Columns)
print(shape_df)

isin_df=df[df["Age"].isin([20,58])] # returns the matheched rows (A)
print(isin_df)

isin_df=df[(df["Age"]==20) | (df["Age"]==58)] # returns the matheched rows (equivalent to A)
print(isin_df)

age_no_na = df[df["Age"].notna()] # returns table for know age not for all
print(age_no_na)


# select specific rows and columns from a DataFrame

adult_names = df.loc[df["Age"] > 35, "Name"] # returns the Name  whose age is grater than 35
print(adult_names)


adult_names = df.loc[2] # returns the details of the 3rd row 
print(adult_names)

row_col=df.iloc[1:4, 0:2] # rows 1 till 4 and columns 0 to 2.
print(row_col)

# REMEMBER
# When selecting subsets of data, square brackets [] are used.
# Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.
# Select specific rows and/or columns using loc when using the row and column names.
# Select specific rows and/or columns using iloc when using the positions in the table.
# You can assign new values to a selection based on loc/iloc.
