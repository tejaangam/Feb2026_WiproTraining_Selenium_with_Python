import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]

plt.plot(x,y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Simple Plot")
#show method will display the graph
plt.show()

#simple data
subjects = ["maths", "Science", "English", "Social", "Biology"]
marks =[85, 75, 96, 84, 90]

plt.plot(subjects,marks)

plt.title("Student marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

data = {
    "Month": ["Jan","Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 150, 110, 180]
}

df = pd.DataFrame(data)
plt.plot(df["Month"], df["Sales"])

plt.title("Monthly sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()