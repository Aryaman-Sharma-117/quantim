import pandas as pd
import glob

files = glob.glob('data/*.csv')

df_list = []

for file in files:
    df = pd.read_csv(file)

    df["product"] = df["product"].str.lower()
    df = df[df['product'] == 'pink morsel']

    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
    df["quantity"] = pd.to_numeric(df["quantity"])
    df['sales'] = df['quantity'] * df['price']

    df = df[['sales', 'date', 'region']]

    df.columns = ["Sales", "Date", "Region"]

    df_list.append(df)

final_df = pd.concat(df_list)

final_df.to_csv("output.csv", index=False)