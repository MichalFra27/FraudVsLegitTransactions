import pandas as pd

data = pd.read_csv("balanced_dataset_50_50.csv")
print(data.info())
print(data.isnull().sum())

# delete colums of data that will not help
data = data.drop(columns=['nameOrig', 'nameDest'])
print(data.info())

newData = {type:['transfer', 'cash_in', 'cash_out', 'payment']}
df = pd.DataFrame(newData)
df_encoded = pd.get_dummies(df, dtype=int)
print(df_encoded)







# implement one hot encoding