import time
print("""
------------------------------------------- SCHOOL DATABASE SYSTEM --------------------------------------------- 
""")
values_1 = input("Please enter your name: ")
values_2 = input("Please enter your surname: ")
values_3 = int(input("Please enter your age: "))
values_4 = input("Please enter your school name: ")
values_5 = input("Please enter school number: ")
print("Your information is saved in the database, please wait...")
time.sleep(1)
print("Save is completed...\n")

print("------------------------------Your Information & Type of Values---------------------------------")
print(f"""Your Name: {values_1.title()}
Type: {type(values_1)}

Your Surname: {values_2.title()}
Type: {type(values_2)}

Your Age: {values_3}
Type: {type(values_3)}

Your School Name: {values_4.title()}
Type: {type(values_4)}

Your School Number: {values_5.title()}
Type: {type(values_5)}""")


