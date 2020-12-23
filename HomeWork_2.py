import time
print("------------------------------------- User Identification Program --------------------------------------")
user_list = []
user_name = input("Please enter your first name: ").title()
user_last_name = input("Please enter your last name: ").title()
user_age = int(input("Please enter your age: "))
user_year_birth = int(input("Please enter your year of birth: "))

print("Your information is being saved...\n")
time.sleep(1)
user_list.extend([user_name,user_last_name,user_age,user_year_birth])

information = ["First Name","Last Name","Age","Year of Birth"]
print("------------- User İnformation -----------------")
for inf,user in zip(information,user_list):
    print(inf,":",user)
print("------------------------------------------------")

if (user_list[2] < 18 or user_list[3] > 2002):
    print("You can't go out because it's too dangerous...")
else:
    print("You can go out to the street...")
    print("but still be careful.. ;)")