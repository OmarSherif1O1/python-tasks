username= input("enter ur name: ")
print (username, 'of type', type(username))

user_age = input(" enter ur age: ")
age = int(user_age)
print(age, 'of type', type(age))

user_height = input ("enter ur height in meters: ")
height = float(user_height)
print(height, 'of type' , type(height))

is_student = input("R U A student Y/N: ")
student = (is_student in ["y","Y","yes","Yes"])
print(student, 'Type of Var student', type(student))

formatted_string= f"-hello {username} \n-age {age} \n-Height {height} \n-R U student {student}"
print(formatted_string)
print(" this is too ez ")

birthyear = f"ur birth year is {2024 - age}"
print(birthyear)

