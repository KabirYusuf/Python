students = []
add_student = 'yes'
while add_student != 'no':
    student_name: str = str(input("Enter Student Name: "))
    subject_one_score: int = int(input("Enter subject 1 score: "))
    subject_two_score: int = int(input("Enter subject 2 score: "))
    subject_total_score = subject_one_score + subject_two_score

    students_info = {
        'name': student_name,
        'subject': [{'subject_one_score': subject_one_score},
                    {'subject_two_score': subject_two_score},
                    {'subjects_total_score': subject_total_score},
                    {'subjects_avg_score': subject_total_score / 2},
                    ]
    }
    students.append(students_info)

    add_student: str = str(input("Enter yes to add student and no to exit: "))

print(students)
print(len(students))



def student_info_output():
    for i in range(len(students)):
        print(students[i]['name'], "\t", students[i]['subject'][0]['subject_one_score'], "\t", students[i]['subject'][1]['subject_two_score'], "\t",
              students[i]['subject'][2]['subjects_total_score'], "\t",
              students[i]['subject'][3]['subjects_avg_score'])


print(student_info_output())
