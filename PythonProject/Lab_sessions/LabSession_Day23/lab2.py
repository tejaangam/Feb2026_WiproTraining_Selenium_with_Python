# =====================================
# CREATE student_performance.csv FILE
# =====================================

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "StudentID": [1,2,3,4,5,6,7,8,9,10,11,12],
    "Gender": ["Male","Female","Male","Female","Male","Female",
               "Male","Female","Male","Female","Male","Female"],
    "Math": [78,65,45,32,88,54,23,76,90,40,55,67],
    "Science": [72,70,50,30,85,60,25,80,92,42,58,69],
    "English": [75,68,48,35,90,57,20,74,88,38,60,72],
    "Attendance": [90,85,70,60,95,80,50,88,97,65,75,82]
}

df = pd.DataFrame(data)

file_path = "/Database/LabSession_Day23/student_performance.csv"
df.to_csv(file_path, index=False)

print("File created at:", file_path)

# STEP 1: FEATURE ENGINEERING


# Create Average_Marks
df["Average_Marks"] = (df["Math"] + df["Science"] + df["English"]) / 3

# Create Result column
df["Result"] = df["Average_Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\nUpdated Data:")
print(df.head())

# STEP 2: ANALYSIS


# Average score per subject
avg_subject_scores = df[["Math","Science","English"]].mean()
print("\nAverage Score Per Subject:")
print(avg_subject_scores)

# Correlation between Attendance and Average Marks
correlation = df["Attendance"].corr(df["Average_Marks"])
print("\nCorrelation between Attendance and Performance:", correlation)

# Performance by Gender
gender_performance = df.groupby("Gender")["Average_Marks"].mean()
print("\nAverage Performance by Gender:")
print(gender_performance)

# Pass vs Fail count
result_counts = df["Result"].value_counts()
print("\nPass vs Fail:")
print(result_counts)


# STEP 3: VISUALIZATIONS

# Bar Chart → Average subject scores
plt.figure()
avg_subject_scores.plot(kind="bar")
plt.title("Average Subject Scores")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()

# Scatter Plot → Attendance vs Average Marks
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

# Pie Chart → Pass vs Fail
plt.figure()
result_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail Distribution")
plt.ylabel("")
plt.show()