# Teacher Access : After Login 1 Can ADD a Student 2 Can View All Student details 3 Can Edit student details
from configparser import DuplicateSectionError
import Access
def teac():
    import mysql.connector
    try :
        mydb = mysql.connector.connect(host='localhost',user='root',password='1820',database='work')
        pointer = mydb.cursor()
        user = input("Register / Login : ")
        user = user.lower()
        def techlogin():
            username = input("Enter User Name : ")
            username = username.lower()
            select = "select * from teacher"
            pointer.execute(select)
            data =pointer.fetchall()
            for i in data :
                if i[0] == username :
                    passw=input("Enter Password : ")
                    if i[2] == passw :
                        print("Login Sucessful")
                        Access.stud_details("teacher",username)
                        break
                    else :
                        print("Password Incorrect : Try Again")
                        break            
            else :
                print("User is Not Here : Please Register")
                techregister()
        def techregister():
            try :
                username = input("Enter User Name : ")
                username = username.lower()
                Name = input("Enter Your Name : ")
                Passw = input("Enter Password : ")
                Email = input("Enter Email Address : ")
                tup = (username,Name,Passw,Email)
                user = "insert into teacher values(%s,%s,%s,%s)"
                pointer.execute(user,tup)
                mydb.commit()
                print("Registeration Sucessful")
                mydb.close()
            except Exception as err:
                print("Registeration Unsucessful Due to : ",err)
        if user == "login":
            techlogin()
        elif user == "register":
            techregister()
        else :
            print("Wrong Input")
    except Exception as err:
        print("Connection Failed Due to : ",err)
