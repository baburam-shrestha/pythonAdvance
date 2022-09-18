# Engines and connection strings
# Alright, it's time to create your first engine! An engine is just a common interface to a database, and the information it requires to connect to one is contained in a connection string, for example sqlite:///example.sqlite. Here, sqlite in sqlite:/// is the database driver, while example.sqlite is a SQLite file contained in the local directory.

# You can learn a lot more about connection strings in the SQLAlchemy documentation.

# Your job in this exercise is to create an engine that connects to a local SQLite file named census.sqlite. Then, print the names of the tables the engine contains using the .table_names() method. Note that when you just want to print the table names, you do not need to use engine.connect() after creating the engine.

# Import create_engine from the sqlalchemy module.
# Using the create_engine() function, create an engine for a local file named census.sqlite with sqlite as the driver. Be sure to enclose the connection string within quotation marks.
# Print the output from the .table_names() method on the engine.

# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())

# Autoloading Tables from a database
# SQLAlchemy can be used to automatically load tables from a database using something called reflection. Reflection is the process of reading the database and building the metadata based on that information. It's the opposite of creating a Table by hand and is very useful for working with existing databases.

# To perform reflection, you will first need to import and initialize a MetaData object. MetaData objects contain information about tables stored in a database. During reflection, the MetaData object will be populated with information about the reflected table automatically, so we only need to initialize it before reflecting by calling MetaData().

# You will also need to import the Table object from the SQLAlchemy package. Then, you use this Table object to read your table from the engine, autoload the columns, and populate the metadata. This can be done with a single call to Table(): using the Table object in this manner is a lot like passing arguments to a function. For example, to autoload the columns with the engine, you have to specify the keyword arguments autoload=True and autoload_with=engine to Table().

# Finally, to view information about the object you just created, you will use the repr() function. For any Python object, repr() returns a text representation of that object. For SQLAlchemy Table objects, it will return the information about that table contained in the metadata.

# In this exercise, your job is to reflect the "census" table available on your engine into a variable called census. We already pre-filled the code to create the engine that you wrote in the previous exercise.

# Import the Table and MetaData from sqlalchemy.
# Create a MetaData object: metadata
# Reflect the census table by using the Table object with the arguments:
# The name of the table as a string ('census').
# The metadata you just initialized.
# autoload=True
# The engine to autoload with - in this case, engine.
# Print the details of census using the repr() function.
# Import create_engine, MetaData, and Table

from sqlalchemy import create_engine, MetaData,Table 

# Create engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census',metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

# Viewing Table details
# Great job reflecting the census table! Now you can begin to learn more about the columns and structure of your table. It is important to get an understanding of your database by examining the column names. This can be done by using the .columns attribute and accessing the .keys() method. For example, census.columns.keys() would return a list of column names of the census table.

# Following this, we can use the metadata container to find out more details about the reflected table such as the columns and their types. For example, information about the table objects are stored in the metadata.tables dictionary, so you can get the metadata of your census table with metadata.tables['census']. This is similar to your use of the repr() function on the census table from the previous exercise.

# The code for connecting to the engine and initializing the metadata you wrote in the previous exercises is displayed for you again and for the last time. From now on and until Chapter 5, this will usually be done behind the scenes.

# Reflect the census table as you did in the previous exercise using the Table() function.
# Print a list of column names of the census table by applying the .keys() method to census.columns.
# Print the details of the census table using the metadata.tables dictionary along with the repr() function. To do this, first access the 'census' key of the metadata.tables dictionary, and place this inside the provided repr() function.

from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Reflect the census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())

# Print full metadata of census
print(repr(metadata.tables['census']))


# Selecting data from a Table: raw SQL
# As you have seen in the video, to access and manipulate the data in the database, we will first need to establish a connection to it by using the .connect() method on the engine. This is because the create_engine() function that you have used before returns an instance of an engine, but it does not actually open a connection until an action is called that would require a connection, such as a query.

# Using what we just learned about SQL and applying the .execute() method on our connection, we can leverage a raw SQL query to query all the records in our census table. The object returned by the .execute() method is a ResultProxy. On this ResultProxy, we can then use the .fetchall() method to get our results - that is, the ResultSet.

# In this exercise, you'll use a traditional SQL query. Notice that when you execute a query using raw SQL, you will query the table in the database directly. In particular, no reflection step is needed.

# In the next exercise, you'll move to SQLAlchemy and begin to understand its advantages. Go for it!

# Use the .connect() method of engine to create a connection.
# Build a SQL statement to query all the columns from census and store it in stmt. Note that your SQL statement must be a string.
# Use the .execute() and .fetchall() methods on connection and store the result in results. Remember that .execute() comes before .fetchall() and that stmt needs to be passed to .execute().
# Print results.

from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Create a connection on engine
connection = engine.connect()

# Build select statement for census table: stmt
stmt = 'select * from census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Selecting data from a Table with SQLAlchemy
# Excellent work so far! It's now time to build your first select statement using SQLAlchemy. SQLAlchemy provides a nice "Pythonic" way of interacting with databases. When you used raw SQL in the last exercise, you queried the database directly. When using SQLAlchemy, you will go through a Table object instead, and SQLAlchemy will take case of translating your query to an appropriate SQL statement for you. So rather than dealing with the differences between specific dialects of traditional SQL such as MySQL or PostgreSQL, you can leverage the Pythonic framework of SQLAlchemy to streamline your workflow and more efficiently query your data. For this reason, it is worth learning even if you may already be familiar with traditional SQL.

# In this exercise, you'll once again build a statement to query all records from the census table. This time, however, you'll make use of the select() function of the sqlalchemy module. This function requires a list of tables or columns as the only required argument: for example, select([my_table]).

# You will also fetch only a few records of the ResultProxy by using .fetchmany() with a size argument specifying the number of records to fetch.

# Table and MetaData have already been imported. The metadata is available as metadata and the connection to the database as connection.

# Import select from the sqlalchemy module.
# Reflect the census table. This code is already written for you.
# Create a query using the select() function to retrieve all the records in the census table. To do so, pass a list to select() containing a single element: census.
# Print stmt to see the actual SQL query being created. This code has been written for you.
# Fetch 10 records from the census table and store then in results. To do this:
# Use the .execute() method on connection with stmt as the argument to retrieve the ResultProxy.
# Use .fetchmany() with the appropriate size argument on connection.execute(stmt) to retrieve the ResultSet.
# Import select
from sqlalchemy import select,Table,MetaData,

# Reflect census table via engine: census
census = Table('census', MetaData, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: results
results = connection.execute(stmt).fetchmany(size=10)

# Execute the statement and print the results
print(results)

# Handling a ResultSet
# Recall the differences between a ResultProxy and a ResultSet:

# ResultProxy: The object returned by the .execute() method. It can be used in a variety of ways to get the data returned by the query.
# ResultSet: The actual data asked for in the query when using a fetch method such as .fetchall() on a ResultProxy.
# This separation between the ResultSet and ResultProxy allows us to fetch as much or as little data as we desire.

# Once we have a ResultSet, we can use Python to access all the data within it by column name and by list style indexes. For example, you can get the first row of the results by using results[0]. With that first row then assigned to a variable first_row, you can get data from the first column by either using first_row[0] or by column name such as first_row['column_name']. You'll now practice exactly this using the ResultSet you obtained from the census table in the previous exercise. It is stored in the variable results. Enjoy!

# Extract the first row of results and assign it to the variable first_row.
# Print the value of the first column in first_row.
# Print the value of the 'state' column in first_row.

# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])