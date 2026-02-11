import pandas as panda

# Load the dataset into a DataFrame
student_table = panda.read_csv("student.csv")

# Filter students step by step
filtered_student_table = student_table[student_table["studytime"] >= 3]
filtered_student_table = filtered_student_table[filtered_student_table["internet"] == 1]
filtered_student_table = filtered_student_table[filtered_student_table["absences"] <= 5]

# Save the filtered data to a new CSV file
filtered_student_table.to_csv("high_engagement.csv", index=False)

# Find the number of filtered students and their respective grade average
number_of_filtered_students = len(filtered_student_table)
average_grade_for_filtered_students = filtered_student_table["grade"].mean()

print(f"\nThe average grade is: {average_grade_for_filtered_students:.2f}")
print(f"Number of students: {number_of_filtered_students}")