student_dict = {
    "student": ["Harry", "Ron", "Hermione"],
    "score": [70, 55, 96]
}

import pandas

student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)

# Loop through a data frame
# for (key, value) in student_dataframe.items():
    # print(value)

# Loop through row in a data frame
for (index, row) in student_dataframe.iterrows():
    # print(row.student)
    if row.student == "Harry":
        print(row.score)

smart_students = {row.student: row.score for (index, row) in student_dataframe.iterrows() if row.score >= 70}
print(smart_students)