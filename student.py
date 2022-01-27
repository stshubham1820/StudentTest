from configparser import DuplicateSectionError
import Access
def stud():
    import mysql.connector
    try :
        mydb = mysql.connector.connect(host='localhost',user='root',password='1820',database='work')
        pointer = mydb.cursor()
        user = input("Register / Login : ")
        user = user.lower()
        def studlogin():
            username = input("Enter User Name : ")
            username = username.lower()
            select = "select * from student"
            pointer.execute(select)
            data =pointer.fetchall()
            for i in data :
                if i[0] == username :
                    passw=input("Enter Password : ")
                    if i[2] == passw :
                        print("Login Sucessful")
                        Access.stud_details("student",username)
                        break
                    else :
                        print("Password Incorrect : Try Again")
                        break            
            else :
                print("User is Not Here : Please Register")
        def studregister():
            try :
                username = input("Enter User Name : ")
                username = username.lower()
                Name = input("Enter Your Name : ")
                Passw = input("Enter Password : ")
                Email = input("Enter Email Address : ")
                Dob = input("Enter Date Of Birth : ")
                Father_Name = input("Enter Father Name : ")
                Mother_Name = input("Enter Mother Name : ")
                DAdm = input("Date Of Admission : ")
                tup = (username,Name,Passw,Email,Dob,Father_Name,Mother_Name,DAdm)
                user = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)"
                pointer.execute(user,tup)
                mydb.commit()
                print("Registeration Sucessful")
                mydb.close()
            except DuplicateSectionError as err:
                print("Already Registered Please Login")
            except Exception as Err :
                print("Registeration Unsucessful Due to : ",Err)
        if user == "login":
            studlogin()
        elif user == "register":
            studregister()
        else :
            print("Wrong Input")
    except :
        print("Not Connected")
