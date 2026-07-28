-- Step 1: Tell SQL which columns to pull from our table
SELECT 
    ClaimID,             -- The unique ID for each medical claim
    Insurance_Type,      -- The type of insurance (e.g., Medicare, Private)
    Billed_Amount_USD,   -- The dollar amount billed for the claim
 -- Step 2: Calculate a running total (a cumulative sum) of billed amounts
    SUM(Billed_Amount_USD) OVER (
        -- Group (or "chunk") the data by Insurance_Type so the total resets for each insurance
        PARTITION BY Insurance_Type 
-- Add up the amounts one claim at a time, ordered by ClaimID
        ORDER BY ClaimID
    ) AS Running_Total_Lost_Revenue  -- Rename this calculated result column
-- Step 3: Specify the source view we are reading from
FROM rcm_analysis_view
-- Step 4: Filter the rows so we only look at rejected/denied claims
WHERE Claim_Status = 'Denied';
