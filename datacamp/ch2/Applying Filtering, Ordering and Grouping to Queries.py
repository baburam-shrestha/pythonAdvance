# Connecting to a PostgreSQL database
# In these exercises, you will be working with real databases hosted on the cloud via Amazon Web Services (AWS)!

# Let's begin by connecting to a PostgreSQL database. When connecting to a PostgreSQL database, many prefer to use the psycopg2 database driver as it supports practically all of PostgreSQL's features efficiently and is the standard dialect for PostgreSQL in SQLAlchemy.

# You might recall from Chapter 1 that we use the create_engine() function and a connection string to connect to a database. In general, connection strings have the form "dialect+driver://username:password@host:port/database"

# There are three components to the connection string in this exercise: the dialect and driver ('postgresql+psycopg2://'), followed by the username and password ('student:datacamp'), followed by the host and port ('@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/'), and finally, the database name ('census'). You will have to pass this string as an argument to create_engine() in order to connect to the database.

# Import create_engine from sqlalchemy.
# Create an engine to the census database by concatenating the following strings:
# 'postgresql+psycopg2://'
# 'student:datacamp'
# '@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'
# ':5432/census'
# Use the .table_names() method on engine to print the table names.

# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())

# Filter data selected from a Table - Simple
# Having connected to the database, it's now time to practice filtering your queries!

# As mentioned in the video, a where() clause is used to filter the data that a statement returns. For example, to select all the records from the census table where the sex is Female (or 'F') we would do the following:

# select([census]).where(census.columns.sex == 'F')

# In addition to == we can use basically any python comparison operator (such as <=, !=, etc) in the where() clause.

# Select all records from the census table by passing in census as a list to select().
# Append a where clause to stmt to return only the records with a state of 'New York'.
# Execute the statement stmt using .execute() on connection and retrieve the results using .fetchall().
# Iterate over results and print the age, sex and pop2000 columns from each record. For example, you can print out the age of result with result.age.
# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York : stmt_filtered
stmt = stmt.where(census.columns.state=='New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2000
for result in results:
    print(result.age, result.sex, result.pop2000)

# Filter data selected from a Table - Expressions
# In addition to standard Python comparators, we can also use methods such as in_() to create more powerful where() clauses. You can see a full list of expressions in the SQLAlchemy Documentation.

# Method in_(), when used on a column, allows us to include records where the value of a column is among a list of possible values. For example, where(census.columns.age.in_([20, 30, 40])) will return only records for people who are exactly 20, 30, or 40 years old.

# In this exercise, you will continue working with the census table, and select the records for people from the three most densely populated states. The list of those states has already been created for you.

# Select all records from the census table.
# Modify the argument of the where clause to use in_() to return all the records where the value in the census.columns.state column is in the states list.
# Loop over the ResultProxy connection.execute(stmt) and print the state and pop2000 columns from each record.

# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_())

# Loop over the ResultProxy and print the state and its population in 2000
for state in connection.execute(stmt):
    print(state, pop2000)


# Filter data selected from a Table - Expressions
# In addition to standard Python comparators, we can also use methods such as in_() to create more powerful
#  where() clauses. You can see a full list of expressions in the SQLAlchemy Documentation.

# Method in_(), when used on a column, allows us to include records where the value of a column is
#  among a list of possible values. For example, where(census.columns.age.in_([20, 30, 40]))
#  will return only records for people who are exactly 20, 30, or 40 years old.

# In this exercise, you will continue working with the census table, and select the records for 
# people from the three most densely populated states. The list of those states has already been 
# created for you.

# Select all records from the census table.
# Modify the argument of the where clause to use in_() to return all the records where the value in 
# the census.columns.state column is in the states list.
# Loop over the ResultProxy connection.execute(stmt) and print the state and pop2000 columns from each record.

# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)

# Filter data selected from a Table - Advanced
# You're really getting the hang of this! SQLAlchemy also allows users to use conjunctions 
# such as and_(), or_(), and not_() to build more complex filtering. For example, we can get a 
# set of records for people in New York who are 21 or 37 years old with the following code:

# select([census]).where(
#   and_(census.columns.state == 'New York',
#        or_(census.columns.age == 21,
#           census.columns.age == 37
#          )
#       )
#   )
# An equivalent SQL statement would be,for example,

# SELECT * FROM census WHERE state = 'New York' AND (age = 21 OR age = 37)

# Import and_ from the sqlalchemy module.
# Select all records from the census table.
# Append a where clause to filter all the records whose state is 'California', and whose sex is not 'M'.
# Execute stmt in the connection and iterate over the ResultProxy to print the age and sex columns from each record.
# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)

# Ordering by a single column
# To sort the result output by a field, we use the .order_by() method. By default, the .order_by() method sorts from lowest to highest on the supplied column. You just have to pass in the name of the column you want sorted to .order_by().

# In the video, for example, Jason used stmt.order_by(census.columns.state) to sort the result output by the state column.

# Select all records of the state column from the census table. To do this, pass census.columns.state as a list to select().
# Append an .order_by() to sort the result output by the state column.
# Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
# Print the first 10 rows of results.

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])

# Ordering in descending order by a single column
# You can also use .order_by() to sort from highest to lowest by wrapping a column in the desc() function. Although you haven't seen this function in action, it generalizes what you have already learned.

# Pass desc() (for "descending") inside an .order_by() with the name of the column you want to sort by. For instance, stmt.order_by(desc(table.columns.column_name)) sorts column_name in descending order.

# Import desc from the sqlalchemy module.
# Select all records of the state column from the census table.
# Append an .order_by() to sort the result output by the state column in descending order. Save the result as rev_stmt.
# Execute rev_stmt using connection.execute() and fetch all the results with .fetchall(). Save them as rev_results.
# Print the first 10 rows of rev_results.
# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results)

# Ordering by multiple columns
# We can pass multiple arguments to the .order_by() method to order by multiple columns. In fact, we can also sort in ascending or descending order for each individual column. Each column in the .order_by() method is fully sorted from left to right. This means that the first column is completely sorted, and then within each matching group of values in the first column, it's sorted by the next column in the .order_by() method. This process is repeated until all the columns in the .order_by() are sorted.

# Select all records of the state and age columns from the census table.
# Use .order_by() to sort the output of the state column in ascending order and age in descending order. (NOTE: desc is already imported).
# Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
# Print the first 20 results.

# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])
# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])

# Ordering by a single column
# To sort the result output by a field, we use the .order_by() method. By default, the .order_by() method sorts from lowest to highest on the supplied column. You just have to pass in the name of the column you want sorted to .order_by().

# In the video, for example, Jason used stmt.order_by(census.columns.state) to sort the result output by the state column.

# Select all records of the state column from the census table. To do this, pass census.columns.state as a list to select().
# Append an .order_by() to sort the result output by the state column.
# Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
# Print the first 10 rows of results.

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])

# Ordering in descending order by a single column
# You can also use .order_by() to sort from highest to lowest by wrapping a column in the desc() function. Although you haven't seen this function in action, it generalizes what you have already learned.

# Pass desc() (for "descending") inside an .order_by() with the name of the column you want to sort by. For instance, stmt.order_by(desc(table.columns.column_name)) sorts column_name in descending order.

# Import desc from the sqlalchemy module.
# Select all records of the state column from the census table.
# Append an .order_by() to sort the result output by the state column in descending order. Save the result as rev_stmt.
# Execute rev_stmt using connection.execute() and fetch all the results with .fetchall(). Save them as rev_results.
# Print the first 10 rows of rev_results.
# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results)

# Ordering by multiple columns
# We can pass multiple arguments to the .order_by() method to order by multiple columns. In fact, we can also sort in ascending or descending order for each individual column. Each column in the .order_by() method is fully sorted from left to right. This means that the first column is completely sorted, and then within each matching group of values in the first column, it's sorted by the next column in the .order_by() method. This process is repeated until all the columns in the .order_by() are sorted.

# Select all records of the state and age columns from the census table.
# Use .order_by() to sort the output of the state column in ascending order and age in descending order. (NOTE: desc is already imported).
# Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
# Print the first 20 results.

# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])
# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])

# ResultsSets and pandas DataFrames
# We can feed a ResultSet directly into a pandas DataFrame, which is the workhorse of many Data Scientists in PythonLand. Jason demonstrated this in the video. In this exercise, you'll follow exactly the same approach to convert a ResultSet into a DataFrame.

# Import pandas as pd.
# Create a DataFrame df using pd.DataFrame() on the ResultSet results.
# Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
# Print the DataFrame.

# import pandas
import pandas as np

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# From SQLAlchemy results to a plot
# We can also take advantage of pandas and Matplotlib to build figures of our data. Remember that data visualization is essential for both exploratory data analysis and communication of your data!

# Import matplotlib.pyplot as plt.
# Create a DataFrame df using pd.DataFrame() on the provided results.
# Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
# Print the DataFrame df.
# Use the plot.bar() method on df to create a bar plot of the results.
# Display the plot with plt.show().

# Import pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()