-- Switch to our target database where the billing data is stored
USE rcm_data; 
-- Create a "SQL View" (a saved virtual table) named 'rcm_analysis_view'
-- This creates a clean, pre-filtered lens so Python or Tableau can read RCM metrics without rewriting SQL queries
CREATE VIEW rcm_analysis_view AS
SELECT 
    ClaimID,
    Patient_ID,
    Billed_Amount_USD,
    Insurance_Type,
    Coverage_Changed_BW_Billing,
	Claim_Status,
    Denial_Reason,
    -- Business Logic: Flag claims greater than $2,000 so the RCM team can prioritize high-revenue recovery
    -- Start the conditional rule
CASE -- Check if the billed amount is strictly greater than $2,000
    WHEN Billed_Amount_USD > 2000 THEN 'High Value'
    -- For any amount $2,000 or less, assign 'Standard'
    ELSE 'Standard'-- End the logic block and name the new column
END AS Claim_Value_Category

-- Source table where raw CSV billing records were imported
FROM rcm_data_table;
select* from rcm_analysis_view;
