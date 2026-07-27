#We are bringing in a tool called 'csv' that helps Python create and save Excel-like files.
import csv 
#We are bringing in a tool called 'random' that helps Python pick random numbers and choices.
import random
#We are setting a rule that we want to create exactly 10,000 rows of data.
total_rows = 10000
#We are asking the computer to create and open a new file named 'rcm_billing_data.csv' in writing mode ('w').
with open('rcm_billing_data_final.csv', mode='w', newline='') as file:
# We are setting up a 'writer' tool that will actually write the text into our new file.
    writer = csv.writer(file)
# We are writing the very first row, which are the column headings for our spreadsheet.
    writer.writerow(['ClaimID', 'Patient_ID', 'Billed_Amount_USD', 'Insurance_Type', 'Coverage_Changed_BW_Billing', 'Claim_Status', 'Denial_Reason'])
# We are starting a loop that will repeat 10,000 times to create our data row by row.
    for i in range(1, total_rows + 1):
# We are creating a unique claim ID like 'CLM00001' by padding the loop number with zeros.
        ClaimID = f"CLM{i:05}"      
# We are creating a random 4-digit patient ID number, like 'PAT5678'.
        Patient_ID = f"PAT{random.randint(1000, 9999)}" 
# We are picking a random hospital bill amount between $150 and $3500, keeping only 2 decimal places.
        Billed_Amount_USD = round(random.uniform(150.0, 3500.0), 2) 
        
# We are picking one random insurance company from this big list.
        Insurance_Type = random.choice(['Medicaid', 'Medicare', 'Medicare Advantage', 'Commercial', 'Private', 'Blue Cross Blue Shield', 'UnitedHealthcare', 'Aetna', 'Cigna', 'Humana', 'Kaiser Permanente', 'Health Net', 'Molina Healthcare', 'Centene', 'Wellcare', 'Anthem', 'Oscar Health', 'Ambetter', 'CareSource', 'UMR', 'Meritain Health', 'GEHA', 'TRICARE', 'VA', 'CHAMPVA', 'Workers Compensation', 'Auto Insurance', 'Self Funded', 'COBRA', 'Uninsured']) 
        
# We are deciding if coverage changed: 15% chance it says 'Yes', 85% chance it says 'No'.
        Coverage_Changed_BW_Billing = random.choices(['Yes', 'No'], weights=[15, 85])[0] 
        
# Now we start our rules. First rule: Did the coverage change to 'Yes'?
        if Coverage_Changed_BW_Billing == 'Yes':
            
# If yes, there is a huge 90% chance the claim is 'Denied' and only 10% chance it is 'Paid'.
            Claim_Status = random.choices(['Paid', 'Denied'], weights=[10, 90])[0] 
            
# If the coverage did NOT change (meaning it is 'No')...
        else:
# ...there is a 95% chance the claim is 'Paid' safely, and only a tiny 5% chance it is 'Denied'.
            Claim_Status = random.choices(['Paid', 'Denied'], weights=[95, 5])[0]  
# Next rule: We need to give a reason. Was the claim successfully 'Paid'?
        if Claim_Status == 'Paid':
# If it was paid, we write 'N/A' because there is no reason for a denial.
            Denial_Reason = 'N/A'
# We are checking: Was it 'Denied' AND was it because coverage changed ('Yes')?
        elif Claim_Status == 'Denied' and Coverage_Changed_BW_Billing == 'Yes':
# If yes, we pick a real-life coverage problem, like the policy expiring.
            Denial_Reason = random.choices(
                ['Coverage Terminated', 'Patient Not Eligible', 'COB Issue - Need Primary Insurance'], 
                weights=[40, 40, 20])[0]
# For all other situations (meaning it was denied for a normal mistake, not a coverage change)...
        else:
# ...we pick a standard hospital billing mistake, like a duplicate claim or a missing code.
            Denial_Reason = random.choices(
                ['Duplicate Claim', 'Missing/Invalid CPT Code', 'Prior Authorization Missing', 'Timely Filing Expired'], 
                weights=[30, 30, 25, 15])[0]
# Finally, we take all the pieces we just created and write them as one complete row in our file.
        writer.writerow([ClaimID, Patient_ID, Billed_Amount_USD, Insurance_Type, Coverage_Changed_BW_Billing, Claim_Status, Denial_Reason])
# After the loop finishes 10,000 times, we print a message to the screen so we know it worked.
print("Success! Created 10,000 rows of RCM billing data with realistic denial reasons.")
