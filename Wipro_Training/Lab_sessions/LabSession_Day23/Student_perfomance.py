import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# 1. CONNECT TO MYSQL DATABASE
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tejaangam@1516",
    database="student_db"
)

# 2. LOAD DATA USING PANDAS
query = "SELECT * FROM student_performance"
df = pd.read_sql(query, connection)

print("Data Loaded from MySQL:")
print(df.head())


# 3. FEATURE ENGINEERING
# Create Average_Marks
df["Average_Marks"] = df[["Math","Science","English"]].mean(axis=1)

# Create Result column
df["Result"] = df["Average_Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nUpdated Data:")
print(df.head())

# 4. ANALYSIS
# 1. Average score per subject
avg_subject_scores = df[["Math","Science","English"]].mean()
print("\nAverage Score Per Subject:")
print(avg_subject_scores)

# 2. Correlation between Attendance and Performance
correlation = df["Attendance"].corr(df["Average_Marks"])
print("\nCorrelation between Attendance & Performance:", correlation)

# 3. Performance by Gender
gender_performance = df.groupby("Gender")["Average_Marks"].mean()
print("\nPerformance by Gender:")
print(gender_performance)

# 4. Pass vs Fail count
result_counts = df["Result"].value_counts()
print("\nPass vs Fail:")
print(result_counts)

# 5. VISUALIZATIONS
# Bar chart → Average subject scores
plt.figure()
avg_subject_scores.plot(kind="bar")
plt.title("Average Subject Scores")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()

# Scatter plot → Attendance vs Average Marks
plt.figure()
plt.scatter(df["Attendance"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()

# Boxplot → Marks distribution by Gender
plt.figure()
df.boxplot(column="Average_Marks", by="Gender")
plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.show()

# Pie chart → Pass vs Fail
plt.figure()
result_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail Distribution")
plt.ylabel("")
plt.show()

connection.close()