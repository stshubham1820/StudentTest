import teacher
import student
class syc:
    def __init__(self) -> None:
        usermode = input("Teacher / Student : ")
        usermode=usermode.lower()
        if usermode == "teacher":
            teacher.teac()
        elif usermode == "student":
            student.stud()
        else :
            print("Wrong Input Try Again")
    
obj = syc
obj()