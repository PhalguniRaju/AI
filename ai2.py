import pandas as pd
data = {"Name":["Alice","Bob","Charlie","David"],"Age":[24,27,22,32],"Department":["HR","FINANCE","IT","MARKETING"],"Salary":[50000,60000,55000,65000]}
df=pd.DataFrame(data)
print("Dataframe: ")
print(df)
print("\nNames: ")
print(df["Name"])
print("\nSalary max:",df["Salary"].max())
print("\nSalary min:",df["Salary"].min())
print(df.iloc[2:5])
print("\nSalary mean: ",df["Salary"].mean())
print("\nInfo of Data Frame\n",df.info)