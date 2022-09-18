# Creating tables with SQLAlchemy
# Previously, you used the Table object to reflect a table from an existing database, but what if you wanted to create a new table? You'd still use the Table object; however, you'd need to replace the autoload and autoload_with parameters with Column objects.

# The Column object takes a name, a SQLAlchemy type with an optional format, and optional keyword arguments for different constraints.

# When defining the table, recall how in the video Jason passed in 255 as the maximum length of a String by using Column('name', String(255)). Checking out the slides from the video may help: you can download them by clicking on 'Slides' next to the IPython Shell.

# After defining the table, you can create the table in the database by using the .create_all() method on metadata and supplying the engine as the only parameter. Go for it!

# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
# Build a new table called data with columns 'name' (String(255)), 'count' (Integer()), 'amount'(Float()), and 'valid' (Boolean()) columns. The second argument of Table() needs to be metadata, which has already been initialized.
# Create the table in the database by passing engine to metadata.create_all().

# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import delete, select
import pandas as pd
from sqlalchemy import insert, select
from sqlalchemy import Table, Column, String, Integer, Float, Boolean
from sqlalchemy import Table, Column, String, Integer, Float, Boolean
# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
             )

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))

# Constraints and data defaults
# You're now going to practice creating a table with some constraints! Often, you'll need to make sure that a column is unique, nullable, a positive value, or related to a column in another table. This is where constraints come in.

# As Jason showed you in the video, in addition to constraints, you can also set a default value for the column if no data is passed to it via the default keyword on the column.


# Table, Column, String, Integer, Float, Boolean are already imported from sqlalchemy.
# Build a new table called data with a unique name (String), count (Integer) defaulted to 1, amount (Float), and valid (Boolean) defaulted to False.
# Hit 'Submit Answer' to create the table in the database and to print the table details for data.

# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
             )

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))

# Inserting a single row
# There are several ways to perform an insert with SQLAlchemy; however, we are going to focus on the one that follows the same pattern as the select statement.

# It uses an insert statement where you specify the table as an argument, and supply the data you wish to insert into the value via the .values() method as keyword arguments. For example, if my_table contains columns my_col_1 and my_col_2, then insert(my_table).values(my_col_1=5, my_col_2="Example") will create a row in my_table with the value in my_col_1 equal to 5 and value in my_col_2 equal to "Example".

# Notice the difference in syntax: when appending a where statement to an existing statement, we include the name of the table as well as the name of the column, for example new_stmt = old_stmt.where(my_tbl.columns.my_col == 15). This is necessary because the existing statement might involve several tables.

# On the other hand, you can only insert a record into a single table, so you do not need to include the name of the table when using values() to insert, e.g. stmt = insert(my_table).values(my_col = 10).

# Here, the name of the table is data. You can run repr(data) in the console to examine the structure of the table.

# Import insert and select from the sqlalchemy module.
# Build an insert statement insert_stmt for the data table to set name to 'Anna', count to 1, amount to 1000.00, and valid to True.
# Execute insert_stmt with the connection and store the results.
# Print the .rowcount attribute of results to see how many records were inserted.
# Build a select statement to query data for the record with the name of 'Anna'.
# Hit 'Run Solution' to print the results of executing the select statement.

# Import insert and select from sqlalchemy

# Build an insert statement to insert a record into the data table: insert_stmt
insert_stmt = insert(data).values(
    name='Anna', count=1, amount=1000.00, valid=True)

# Execute the insert statement via the connection: results
results = connection.execute(insert_stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert: select_stmt
select_stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(connection.execute(select_stmt).first())

# Inserting multiple records at once
# It's time to practice inserting multiple records at once!

# As Jason showed you in the video, when inserting multiple records at once, you do not use the .values() method. Instead, you'll want to first build a list of dictionaries that represents the data you want to insert, with keys being the names of the columns. in the .execute() method, you can pair this list of dictionaries with an insert statement, which will insert all the records in your list of dictionaries.

# Build a list of dictionaries called values_list with two dictionaries. In the first dictionary set name to 'Anna', count to 1, amount to 1000.00, and valid to True. In the second dictionary of the list, set name to 'Taylor', count to 1, amount to 750.00, and valid to False.
# Build an insert statement for the data table for a multiple insert, save it as stmt.
# Execute stmt with the values_list via connection and store the results. Make sure values_list is the second argument to .execute().
# Print the rowcount of the results.

# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': 'Taylor', 'count': 1, 'amount': 750.00, 'valid': False},
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)

# Loading a CSV into a table
# You've done a great job so far at inserting data into tables! You're now going to learn how to load the contents of a CSV file into a table.

# One way to do that would be to read a CSV file line by line, create a dictionary from each line, and then use insert(), like you did in the previous exercise.

# But there is a faster way using pandas. You can read a CSV file into a DataFrame using the read_csv() function (this function should be familiar to you, but you can run help(pd.read_csv) in the console to refresh your memory!). Then, you can call the .to_sql() method on the DataFrame to load it into a SQL table in a database. The columns of the DataFrame should match the columns of the SQL table.

# .to_sql() has many parameters, but in this exercise we will use the following:

# name is the name of the SQL table (as a string).
# con is the connection to the database that you will use to upload the data.
# if_exists specifies how to behave if the table already exists in the database; possible values are "fail", "replace", and "append".
# index (True or False) specifies whether to write the DataFrame's index as a column.
# In this exercise, you will upload the data contained in the census.csv file into an existing table "census". The connection to the database has already been created for you.

# Use pd.read_csv() to load the "census.csv" file into a DataFrame. Set the header parameter to None since the file doesn't have a header row.
# Rename the columns of census_df to "state", "sex", age, "pop2000", and "pop2008" to match the columns of the "census" table in the database.

# import pandas

# read census.csv into a DataFrame : census_df
census_df = pd.read_csv("census.csv", header=None)

# rename the columns of the census DataFrame
census_df.columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']

# Updating individual records
# The update statement is very similar to an insert statement. For example, you can update all wages in the employees table as follows:

# stmt = update(employees).values(wage=100.00)
# The update statement also typically uses a where clause to help us determine what data to update. For example, to only update the record for the employee with ID 15, you would append the previous statement as follows:

# stmt = stmt.where(employees.id == 15)
# You'll be using the FIPS state code here, which is appropriated by the U.S. government to identify U.S. states and certain other associated areas.

# For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), name (Column), and fips_state (Column).

# Build a statement to select all columns from the state_fact table where the value in the name column is 'New York'. Call it select_stmt.
# Fetch all the results and assign them to results.
# Print the results and the fips_state column of the first row of the results.
# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Execute select_stmt and fetch the results
results = connection.execute(select_stmt).fetchall()

# Print the results of executing the select_stmt
print(results)

# Print the FIPS code for the first row of the result
print(results[0]['fips_state'])

# Updating multiple records
# As Jason discussed in the video, by using a where clause that selects more records, you can update multiple records at once. Unlike inserting, updating multiple records works exactly the same way as updating a single record (as long as you are updating them with the same value). It's time now to practice this!

# For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), notes (Column), and census_region_name (Column).

# Build an update statement to update the notes column in the state_fact table to 'The Wild West'. Save it as stmt.
# Use a where clause to filter for records that have 'West' in the census_region_name column of the state_fact table.
# Execute stmt_west via the connection and save the output as results.
# Hit 'Run Solution' to print rowcount of the results.

# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records: stmt_west
stmt_west = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement: results
results = connection.execute(stmt_west)

# Print rowcount
print(results.rowcount)

# Correlated updates
# You can also update records with data from a select statement. This is called a correlated update. It works by defining a select statement that returns the value you want to update the record with and assigning that select statement as the value in update.

# You'll be using a flat_census in this exercise as the target of your correlated update. The flat_census table is a summarized copy of your census table, and contains, in particular, the fips_state columns.

# Build a statement to select the name column from state_fact. Save the statement as fips_stmt.
# Append a where clause to fips_stmt that matches fips_state from the state_fact table with fips_code in the flat_census table.
# Build an update statement to set the state_name in flat_census to fips_stmt. Save the statement as update_stmt.
# Hit 'Submit Answer' to execute update_stmt, store the results and print the rowcount of results.
# Build a statement to select name from state_fact: fips_stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to match the fips_state to flat_census fips_code: fips_stmt
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt_where: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)

# Deleting all the records from a table
# Often, you'll need to empty a table of all of its records so you can reload the data. You can do this with a delete statement with just the table as an argument. For example, in the video, Jason deleted the table extra_employees by executing as follows:

# delete_stmt = delete(extra_employees)
# result_proxy = connection.execute(delete_stmt)
# Do be careful, though, as deleting cannot be undone!

# Import delete and select from sqlalchemy.
# Build a delete statement to remove all the data from the census table. Save it as delete_stmt.
# Execute delete_stmt via the connection and save the results.
# Import delete, select

# Build a statement to empty the census table: stmt
delete_stmt = delete(census)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table : select_stmt
select_stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(select_stmt).fetchall())

# Deleting specific records
# By using a where() clause, you can target the delete statement to remove only certain records. For example, Jason deleted all rows from the employees table that had id 3 with the following delete statement:

# delete(employees).where(employees.columns.id == 3)
# Here you'll delete ALL rows which have 'M' in the sex column and 36 in the age column. We have included code at the start which computes the total number of these rows. It is important to make sure that this is the number of rows that you actually delete.

# Build a delete statement to remove data from the census table. Save it as delete_stmt.
# Append a where clause to delete_stmt that contains an and_ to filter for rows which have 'M' in the sex column AND 36 in the age column.
# Execute the delete statement.
# Build a statement to count records using the sex column for Men ('M') age 36: count_stmt
count_stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = connection.execute(count_stmt).scalar()

# Build a statement to delete records from the census table: delete_stmt
delete_stmt = delete(census)

# Append a where clause to target Men ('M') age 36: delete_stmt
delete_stmt = delete_stmt.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)

# Deleting a table completely
# You're now going to practice dropping individual tables from a database with the .drop() method, as well as all tables in a database with the .drop_all() method!

# As Spider-Man's Uncle Ben (as well as Jason, in the video!) said: With great power, comes great responsibility. Do be careful when deleting tables, as it's not simple or fast to restore large databases! Remember, you can check to see if a table exists on an engine with the .exists(engine) method.

# This is the final exercise in this chapter: After this, you'll be ready to apply everything you've learned to a case study in the final chapter of this course!

# Drop the state_fact table by applying the method .drop() to it and passing it the argument engine (in fact, engine will be the sole argument for every function/method in this exercise!)
# Check to see if state_fact exists via print. Use the .exists() method with engine as the argument.
# Drop all the tables via the metadata using the .drop_all() method.
# Use a print statement to check if the census table exists.

# Drop the state_fact table
state_fact.drop(engine)


# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))
