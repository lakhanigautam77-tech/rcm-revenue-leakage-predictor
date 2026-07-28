# this  fills it with the word 'Unknown' where the insurance type is missing to avoid any further errors.
df['Insurance_Type'] = df['Insurance_Type'].fillna('Unknown')
# This custom rule reads every single row one by one. 
# If the bill is expensive AND the coverage changed, it gets a Critical Risk Score!
df['Denial_Risk_Score'] = df.apply(
    lambda row: '95% (Critical Risk)' if (row['Claim_Value_Category'] == 'High Value' and row['Coverage_Changed_BW_Billing'] == 'Yes') else 'Low Risk', 
    axis=1)
# Let's look at the first 10 rows to see our new Risk Score column!
df.head(10)
