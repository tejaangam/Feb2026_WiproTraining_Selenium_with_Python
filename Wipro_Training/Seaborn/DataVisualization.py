import seaborn as sns
import matplotlib.pyplot as plt

#Basic plot(Line Plot)
#Load the sample data
data = sns.load_dataset("flights")
#line plot
sns.lineplot(x = "year", y ="passengers", data= data)
plt.title("Line Plot-Yearly Passenger Growth")
plt.show()

#Bar Plot
data = sns.load_dataset("tips")
sns.barplot(x = "day", y = "tip", data=data)
plt.title("BarPlot-Total Bill vs Tip")
plt.show()

#Scatterplot
data = sns.load_dataset("tips")
sns.scatterplot(x = "day", y = "tip", data=data)
plt.title("ScatterPlot-Total Bill vs Tip")
plt.show()

#Histo Plot
data = sns.load_dataset("tips")
sns.histplot(data["total_bill"], bins=20)
plt.title("HistPlot-Total Bill vs Tip")
plt.show()

#Box Plot
data = sns.load_dataset("tips")
sns.boxplot(x = "day", y = "tip", data=data)
plt.title("Box Plot-Total Bill vs Tip")
plt.show()

#Heat map
data = sns.load_dataset("tips")
cor1 = data.corr(numeric_only=True)
sns.heatmap(cor1, annot = True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#Pair plot
data = sns.load_dataset("iris")
sns.pairplot(data)
plt.show()

#Violin plot
data = sns.load_dataset("tips")
sns.violinplot(x = "day", y = "tip", data=data)
plt.title("Violin Plot-Bill Distribution by Day")
plt.show()

#Count Plot
data = sns.load_dataset("tips")
sns.countplot(x = "day", data=data)
plt.title("CountPlot-Number of customers per day")
plt.show()

#Reg plot
data = sns.load_dataset("tips")
sns.regplot(x = "total_bill", y = "tip", data=data)
plt.title("Regression Plot-Regression between Bill and TotalBill")
plt.show()