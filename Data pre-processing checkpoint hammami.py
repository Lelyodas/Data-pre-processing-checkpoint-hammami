import pandas as pd
from sklearn.preprocessing import LabelEncoder

file_path = r"C:\Users\LELYODAS\Desktop\DATA\exercices\Data pre-processing checkpoint hammami\STEG_BILLING_HISTORY.csv"

df = pd.read_csv(file_path)

client_0_bills = df.head(10)
print(client_0_bills)

print(type(client_0_bills))

df.info()

missing_values = df.isnull().sum()
print(missing_values)

df.fillna(df.median(), inplace=True)

numeric_summary = df.describe()
print(numeric_summary)

client_0_records_method1 = df.loc[df['id'] == 'train_Client_0']
print(client_0_records_method1)

client_0_records_method2 = df[df['id'] == 'train_Client_0']
print(client_0_records_method2)

encoder = LabelEncoder()
df['counter_type_encoded'] = encoder.fit_transform(df['counter_type'])
print(df[['counter_type', 'counter_type_encoded']].head())
df.drop(columns=['counter_statue'], inplace=True)

print(df.columns)