-- Goal: Securely import raw medical billing CSV data into a SQL database and made claim_id as primary key to avoid further duplicacy 
-- Step 1: Select the correct database schema
use rcm_data;
-- Step 2: Create the table structure (Schema) for the billing data
CREATE TABLE IF NOT EXISTS rcm_data_table ( -- ""IF NOT"" Safely creates the table only if it doesn't already exist to prevent overwriting.
    claim_id VARCHAR(50) PRIMARY KEY,        -- it can only hold maximum upto 50 characters	as well as made it a primary key
    patient_id VARCHAR(50),          -- it can only hold maximum upto 50 characters
    billed_amount_usd DECIMAL(10, 2),   -- stores the money up to 8 digits long, keeping exactly 2 digits for the cents.
    insurance_type VARCHAR(100),        -- it can only hold maximum upto 100 characters
    coverage_changed_bw_billing VARCHAR(10),  -- it can only hold maximum upto 10 characters        
    claim_status VARCHAR(50)                  -- it can only hold maximum upto 50 characters
);
--  Pour the data from the safe folder into our new table
-- Tell MySQL to read data fro the secure private folder as sql does not allow importing from another folders
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/rcm_billing_data_final.csv' 
-- Specify the destination database table where you want to insert all this data
INTO TABLE rcm_data_table 
-- Tell MySQL that a comma separates each column into the file 
FIELDS TERMINATED BY ','
-- Handle text fields that are wrapped in double quotes (e.g., "John Doe")
ENCLOSED BY '"' 
-- Using \r\n to handle the invisible Windows Enter key (tells MySQL a new line means a new row)
LINES TERMINATED BY '\r\n' 
-- Skip the very first row of the CSV file so you don't accidentally insert column titles as actual data
IGNORE 1 ROWS;
--  The Final Check: Show to prove it loaded perfectly!
SELECT * FROM rcm_data_table;
