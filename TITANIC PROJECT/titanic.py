import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load titanic dataset
url="Titanic.csv"
df=pd.read_csv(url)

#Inspect data
print(df.info())
print(df.describe())

#handle missing values
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Age"].mode()[0])

#remove duplicates
df=df.drop_duplicates()

#filter Data: Passengers in first class

first_class=df[df["Pclass"]==1]
print("First Class Passengers: \n",first_class.head())

#display barchart: Survival rate by class
# survival_by_class=df.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind="bar", color="green")
# plt.title("Survival Rate by class")
# plt.ylabel("Survival Rate")
# plt.show()

#histogram :Age distribution
# sns.histplot(df["Age"], kde=True, bins=20, color="purple")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

#Scatter plot: Age vs Fare
plt.scatter(df["Age"],df["Fare"],alpha=0.5,color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()