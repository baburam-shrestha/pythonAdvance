# Setup the engine and metadata
# In this exercise, your job is to create an engine to the database that will be used in this chapter. Then, you need to initialize its metadata.

# Recall how you did this in Chapter 1 by leveraging create_engine() and MetaData().


# Import create_engine and MetaData from sqlalchemy.
# Create an engine to the chapter 5 database by using 'sqlite:///chapter5.sqlite' as the connection string.
# Create a MetaData object as metadata.

# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()

# Create the table to the database
# Having setup the engine and initialized the metadata, you will now define the census table object and then create it in the database using the metadata and engine from the previous exercise. To create it in the database, you will have to use the .create_all() method on the metadata with engine as the argument.

# It may help to refer back to the Chapter 4 exercise in which you learned how to create a table.

# Import Table, Column, String, and Integer from sqlalchemy.
# Define a census table with the following columns:
# 'state' - String - length of 30
# 'sex' - String - length of 1
# 'age' - Integer
# 'pop2000' - Integer
# 'pop2008' - Integer
# Create the table in the database using the metadata and engine.

# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column, String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)

# Reading the data from the CSV
# Leverage the Python CSV module from the standard library and load the data into a list of dictionaries.

# It may help to refer back to the Chapter 4 exercise in which you did something similar.

# Create an empty list called values_list.
# Iterate over the rows of csv_reader with a for loop, creating a dictionary called data for each row and append it to values_list.
# Within the for loop, row will be a list whose entries are 'state' , 'sex', 'age', 'pop2000' and 'pop2008' (in that order).

# Create an empty list: values_list
values_list=[]

# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state':row[0], 'sex':row[1],'age':row[2],'pop2000':row[3],'pop2008':row[4]}

    #Append that dictionary to the values list
    values_list.append(data)

# Load data from a list into the Table
# Using the multiple insert pattern, in this exercise, you will load the data from values_list into the table.

# Import insert from sqlalchemy.
# Build an insert statement for the census table.
# Execute the statement stmt along with values_list. You will need to pass them both as arguments to connection.execute().
# Print the rowcount attribute of results.
# Build an insert statement : stmt
stmt = insert(census)

# Use values_list to insert data: results   
results = connection.execute(stmt,values_list)

# Print rowcount
print(results.rowcount)

# Determine the average age by population
# As Jason discussed in the video, to calculate a weighted average, we first find the total sum of weights multiplied by the values we're averaging, then divide by the sum of all the weights.

# For example, if we wanted to find a weighted average of data = [10, 30, 50] weighted by weights = [2,4,6], we would compute 
 
# , or sum(weights * data) / sum(weights).

# In this exercise, however, you will make use of func.sum() together with select to select the weighted average of a column from a table. You will still work with the census data, and you will compute the average of age weighted by state population in the year 2000, and then group this weighted average by sex.

# Import select and func from sqlalchemy.
# Write a statement to select the average of age (age) weighted by population in 2000 (pop2000) from census.

# Import select and func
from sqlalchemy import select, func

# Select sex and average age weighted by 2000 population
stmt = select([(func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)).label('average_age'),
               census.columns.sex
			  ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and fetch all the results
results = connection.execute(stmt).fetchall()

# print the sex and average age column for each result
for result in results :
    print (result.sex,result.average_age)

# Determine the percentage of population by gender and state
# In this exercise, you will write a query to determine the percentage of the population in 2000 that comprised of women. You will group this query by state.

# Import case, cast and Float from sqlalchemy.
# Define a statement to select state and the percentage of women in 2000.
# Inside func.sum(), use case() to select women (using the sex column) from pop2000. Remember to specify else_=0 if the sex is not 'F'.
# To get the percentage, divide the number of women in the year 2000 by the overall population in 2000. Cast the divisor - census.columns.pop2000 - to Float before multiplying by 100.
# Group the query by state.
# Execute the query and store it as results.
# Print state and percent_female for each record. This has been done for you, so hit 'Submit Answer' to see the result.

# import case, cast and Float from sqlalchemy
from sqlalchemy import case,cast,Float
# Build a query to calculate the percentage of women in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)

# Determine the difference by state from the 2000 and 2008 censuses
# In this final exercise, you will write a query to calculate the states that changed the most in population. You will limit your query to display only the top 10 states.

# Build a statement to:
# Select state.
# Calculate the difference in population between 2008 (pop2008) and 2000 (pop2000).
# Group the query by census.columns.state using the .group_by() method on stmt.
# Order by 'pop_change' in descending order using the .order_by() method with the desc() function on 'pop_change'.
# Limit the query to the top 10 states using the .limit() method.
# Execute the query and store it as results.
# Print the state and the population change for each result. This has been done for you, so hit 'Submit Answer' to see the result!

# Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,
     (census.columns.pop2008-census.columns.pop2000).label('pop_change')
])

# Group by State
stmt = stmt.group_by(census.columns.state)

# Order by Population Change
stmt = stmt.order_by(desc('pop_change'))

# Limit to top 10
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))