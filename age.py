import datetime

birth_year = int(input("What year were you born? "))

current_year = datetime.datetime.now().year
# print(current_year)
age = current_year - birth_year

print(f"You are {age} years old")

