UserName= input("enter ur name: ")
print (UserName, 'of type', type(UserName))

UserAge = input(" enter ur age: ")
Age = int(UserAge)
print(Age, 'of type', type(Age))

UserHeight = input ("enter ur height in meters: ")
Height = float(UserHeight)
print(Height, 'of type' , type(Height))

Rustudent = input("R U A student Y/N: ")
student = bool(Rustudent =="y")
print(student, 'Type of Var student', type(student))

_format= f"-hello {UserName} \n-age {Age} \n-Height {Height} \n-R U student {student}"
print(_format)
print(" this is too ez ")

