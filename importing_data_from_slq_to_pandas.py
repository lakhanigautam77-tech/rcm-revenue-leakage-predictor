# Import pandas, a library used to organize and work with data in tables (DataFrames)
import pandas as pd   
# Import create_engine, a tool that acts as a bridge to connect Python to the database
from sqlalchemy import create_engine
# Create a connection engine that tells Python where your database is and how to log in
engine = create_engine('mysql+pymysql://root:Gautam%400802@localhost/rcm_data')
# Store your SQL command in a variable (this tells the database to select all data from the view)
sql_query = "SELECT * FROM rcm_analysis_view;"
# Run the SQL query through the database connection and load the resulting table into 'df'
df = pd.read_sql(sql_query, engine)
# Display the first 5 rows of your new DataFrame so you can quickly preview the data
df.head()
