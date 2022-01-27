class India():
    def info(self):
        print("Your Country Code is : +91")
        print("Your Country Capital is Delhi")
        print("Your National Sport is Hockey")
class Australia():
    def info(self):
        print("Your Country Code is : +83")
        print("Your Country Capital is Melborn")
        print("Your National Sport is Cricket")
def fun(name,age,country):
    print("Your Name is : ",name)
    print("Your Age is : ",age)
    country.info()
name = input("Enter Name : ")
age = int(input("Enter Age : "))
count = (input("Enter Country : ")).capitalize()
if count=="India":
    fun(name,age,India())
elif count=="Australia":
    fun(name,age,Australia())
else :
    print("Database Failer")

