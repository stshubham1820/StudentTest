import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1820',
    database='school',
    )
pointer = mydb.cursor()
def teacher():
    opinion = int(input('Enter 1 If You want to Add Tecaher 2 If You want to see Techer Data'))
    if opinion==1:
        Name = input('Enter Name :')
        Age = int(input('Enter Age :'))
        Position = input('Enter Position :')
        Experience = int(input('Enter Experience :'))
        Subject = input('Enter Subject :')
        Tup = (Name,Age,Position,Experience,Subject)
        var = "Insert into teacher1 values(%s,%s,%s,%s,%s)"
        pointer.execute(var,Tup)
        mydb.commit()
        print("Data Saved")
        option = int(input('Enter 1 If u want to run again Else Exit : '))
        if option == 1:
            teacher()#recursion
        else :
            print("Exit")
    elif opinion==2:
        var = 'Select * from teacher1'
        pointer.execute(var)
        for i in pointer:
            print(i)
        option = int(input('Enter 1 If u want to run again Else Exit : '))
        if option == 1:
            teacher()#recursion
        else :
            print("Exit")   
teacher()