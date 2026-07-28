# THE ADVANCED PIVOT TABLE
# First, we only want to look at the money we are losing (Denied claims)
denied_claims_only = df[df['Claim_Status'] == 'Denied']
# Next, we group them by Insurance Type and do three math problems at once!
denied_summary = denied_claims_only.groupby('Insurance_Type').agg(
    Total_Dollars_Lost=('Billed_Amount_USD', 'sum'),
    Average_Bill_Size=('Billed_Amount_USD', 'mean'),
    Total_Claims_Denied=('ClaimID', 'count')).reset_index()
# Let's look at the final summary table
print("Here is your final Summary Table:")
display(denied_summary)
# EXPORT FOR POWER BI
# This packages our clean data into new CSV files and saves them to our computer
df.to_csv('Cleaned_RCM_Data_for_PowerBI.csv', index=False)
denied_summary.to_csv('RCM_Summary_Table.csv', index=False)
print("\n🎉 Pipeline Complete! Data is clean, scored, and ready for Power BI. 🎉")
