import time
import random

print("""
------------------------------------- Simple Student Management System ------------------------------------------
""")

student_inf = ("Mustafa","Sarımeşinli")
right_of_entry = 3

while True:

    input_name = input("Please enter your name: ").title()
    input_surname = input("Please enter your surname: ").title()
    print("Plese wait 1 second...Checking your information... \n")
    time.sleep(1)


    if (student_inf[0] != input_name and student_inf[1] == input_surname):
        print("Invalid Name.. Please enter your name correctly...")
        right_of_entry -= 1
        print("your remaining trial right:",right_of_entry,"\n")

    elif (student_inf[0] == input_name and student_inf[1] != input_surname):
        print("Invalid Surname.. Please enter your surname correctly...")
        right_of_entry -= 1
        print("your remaining trial right:", right_of_entry,"\n")

    elif (student_inf[0] != input_name and student_inf[1] != input_surname):
        print("Invalid Name and Surname.. Please enter your name and surname correctly...")
        right_of_entry -= 1
        print("your remaining trial right:", right_of_entry,"\n")

    else:
        print("""
                 01╗       01╗  0101010╗  01╗        01010╗    01010╗   101╗   101╗  0101010╗
                 01║  01╗  01║  01╔════╝  01║       01╔══01╗  01╔══01╗  0101╗ 0101║  01╔════╝
                 ╚01╗0101╗01╔╝  01010╗    01║       01║  ╚═╝  01║  01║  01╔0101╔01║  01010╗
                  0101╔═0101║   01╔══╝    01║       01║  01╗  01║  01║  01║╚01╔╝01║  01╔══╝
                  ╚01╔╝ ╚01╔╝   0101010╗  0101010╗  ╚01010╔╝  ╚01010╔╝  01║ ╚═╝ 01║  0101010╗
                   ╚═╝   ╚═╝    ╚══════╝  ╚══════╝   ╚════╝    ╚════╝   ╚═╝     ╚═╝  ╚══════╝    
                """)
        print("Please wait 1 second... You are redirected to the menu....\n")
        time.sleep(1)

        lessons_list = list()
        while True:
            if (len(lessons_list) <= 4):
                all_lessons = input("Please enter 5 course names: ").title()
                lessons_list.append(all_lessons)

            else:
                print("Thanks...Recording your courses...")
                print("Please wait 1 second....")
                time.sleep(1)
                print("Courses have been saved...")
                break

        print("---------------------------------- Lessons the Student Took -------------------------------------------")

        student_lessons = []
        print("~~~~ Courses Registered in the System ~~~~\n")
        for lessons in lessons_list:
            print("\t\t", lessons, "\n")
        while True:

            input_student_lessons = input("Please Enter the Courses You Have Taken(Press Q to exit): ").title()

            if input_student_lessons in lessons_list:
                print("Adding Course....")
                time.sleep(1)
                student_lessons.append(input_student_lessons)
                print("Course Added...\n")

            elif (input_student_lessons == "q" or input_student_lessons == "Q"):
                if (3 <= len(student_lessons) <= 5):
                    print("You are redirected to the menu ...\n")
                    break
                else:
                    print("You failled in class....\n")
                    break
            else:
                print("There is no such course...\n")

        print("~~~~ Lessons You Took ~~~~")
        for i in student_lessons:
            print(i)

        print("------------------------------------ now it's exam time ------------------------------------\n")
        print("The system will choose the course you will take the exam.")
        print("Please wait...")
        time.sleep(1)
        rnd_exam = random.choice(student_lessons)
        print("The course you will take the exam is {}.\n".format(rnd_exam))
        print("Test Time....")
        time.sleep(1)
        print("exams are over...")
        print("""
                                             01010╗   01╗  01╗
                                            01╔══01╗  01║ 01╔╝
                                            01║  01║  01010═╝
                                            01║  01║  01╔═01╗
                                            ╚01010╔╝  01║ ╚01╗ 
                                             ╚════╝   ╚═╝  ╚═╝ 
        """)

        print("---------------------------------- Now grade calculation ----------------------------------\n")
        midterm_grade = int(input("Please enter your midterm grade: "))
        final_grade = int(input("Please enter your final grade: "))
        project_grade = int(input("Please enteer your project grade: "))

        grade = [midterm_grade,final_grade,project_grade]
        exam = ["midterm","final","project"]
        exam_dict = dict(zip(exam,grade))

        mean_grade = exam_dict.get("midterm") * 0.3 + exam_dict.get("final") * 0.5 + exam_dict.get("project") * 0.2
        print("note you received :   {}".format(mean_grade))
        print("So....")
        time.sleep(1)

        if (mean_grade >= 90):
            letter_grade = "AA"
            print("Congratulations... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        elif (mean_grade >= 85):
            letter_grade = "BA"
            print("Congratulations... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        elif (mean_grade >= 80):
            letter_grade = "BB"
            print("Congratulations... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        elif (mean_grade >= 75):
            letter_grade = "CB"
            print("It's not bad... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        elif (mean_grade >= 70):
            letter_grade = "CC"
            print("It's not bad... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        elif (mean_grade >= 65):
            letter_grade = "DC"
            print("It's not bad... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        elif (mean_grade >= 60):
            letter_grade = "DD"
            print("You have to work harder... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        elif (mean_grade >= 50):
            letter_grade = "FD"
            print("you have to work harder... You got an {} in {} lesson.".format(letter_grade,rnd_exam))
            break
        else:
            letter_grade = "FF"
            print("You failed {} class because you got {}...".format(rnd_exam,letter_grade))
            break

    if (right_of_entry == 0):
        print("you do not have the right to enter....")
        print("Please try again later....")
        time.sleep(1)
        print("""
                                010101╗  01╗   01╗  010101╗  01╗   01╗
                                01╔══01╗ ╚01╗ 01╔╝  01╔══01╗ ╚01╗ 01╔╝
                                010101╦╝  ╚0101╔╝   010101╦╝  ╚0101╔╝
                                01╔══01╗   ╚01╔╝    01╔══01╗   ╚01╔╝
                                010101╦╝    01║     010101╦╝    01║
                                ╚═════╝     ╚═╝     ╚═════╝     ╚═╝
        """)
        break

















