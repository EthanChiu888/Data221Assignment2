import pandas as panda
student_table = panda.read_csv("student.csv")

# Define grading function
def grade_band(grade):
    if grade <= 9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:
        return "High"
# Create new column
student_table["grade_band"] = student_table["grade"].apply(grade_band)

# Grouped summary table
summary_table = student_table.groupby("grade_band").agg(
    num_students=("grade", "count"),
    avg_absences=("absences", "mean"),
    pct_internet=("internet", "mean")
)

# Converts internet mean to percentage
summary_table["pct_internet"] = summary_table["pct_internet"] * 100
# Saves the table as student_bands.csv
summary_table.to_csv("student_bands.csv")




