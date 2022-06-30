import pandas as pd

data = {'Patient_Name': ['Fiona',
                         'Phillip',
                         'Ian',
                         'Debbie',
                         'Carl',
                         'Liam'],

        'Monthly_Premium': ['350',
                            '300',
                            '450',
                            '200',
                            '150',
                            '100'],

        'Claims_Filed': ['1',
                         '3',
                         '0',
                         '5',
                         '82',
                         '2'],

        'Cost_per_Claim': ['200',
                           '150',
                           '200',
                           '300',
                           '750',
                           '150']}

Insurance_df = pd.DataFrame(data)

Insurance_df['Too_Expensive'] = (Insurance_df['Claims_Filed'].astype(
    int)).apply(lambda val: "Yes" if val > 10 else "No")

print(Insurance_df)


def Average_Cost_Per_Claim(df):
    avg_cost = int(sum(Insurance_df['Cost_per_Claim'].astype(
        int))/len(Insurance_df['Cost_per_Claim'].astype(int)))
    print("The average cost per claim is: $", (avg_cost))


Average_Cost_Per_Claim(Insurance_df)


def Average_Number_of_Claims(df):
    avg_claims = int(sum(Insurance_df['Claims_Filed'].astype(
        int))/len(Insurance_df['Claims_Filed'].astype(int)))
    print("The average number of claims is: ", (avg_claims))


Average_Number_of_Claims(Insurance_df)
