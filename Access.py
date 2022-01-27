from configparser import DuplicateSectionError
import update
def stud_details(user,userid):
    import mysql.connector
    mydb = mysql.connector.connect(host='localhost',user='root',password='1820',database='work')
    pointer=mydb.cursor()
    def techaccess():
        print("Hii "+userid)
        opt=input("Press 1 to See Students Details Press 2 to ADD Students Press 3 For Student Updation : ")
        if opt == "1":
            select = "select username,studentname,email,dob,fathername,mothername,Admdate from student"
            pointer.execute(select)
            data = pointer.fetchall()
            for i in data :
                print(i)
        elif opt == "2":
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
        elif opt == "3":
            user = input("Enter Student UserId : ")
            update.supdate(user)
        else :
            print("Sorry Wrong Input")
    def studaccess():
        print("Hii "+userid)
        opt = input("Would You Like to See Your Data : Y/N : ")
        opt=opt.lower()
        try :
            if opt == 'y': 
                select = "select * from student where username = %s"
                pointer.execute(select,(userid,))
                data = pointer.fetchall()
                print(data)
            else :
                newopt=input("Would You like to update your Data : Y/N : ")
                newopt = newopt.lower()
                try :
                    if newopt == 'y':
                        update.supdate(userid)
                except Exception as Err :
                    print(Err)
        except Exception as err:
            print(err)
    if user == "teacher":
        techaccess()
    else :
        studaccess()
