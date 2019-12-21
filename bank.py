#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LAVANYAA
#
# Created:     13-12-2019
# Copyright:   (c) LAVANYAA 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import linecache
import re
import sys
class bank:
    def __init__(self, balance):
        self.balance=balance
    def withdraw(self,c):
        fi=open("bankk.txt","r+")
        line = linecache.getline("bankk.txt", c)
        sp=line.split(",")
        print(sp)
        print(self.balance)
        f=line.rindex(sp[-1])
        print(f)
        withdrawal=int(input("Enter amount to withdraw "))
        if((int(self.balance)-2000)>withdrawal):
            updatedbal=int(self.balance)-withdrawal
            bal=updatedbal
            print(bal)
            fi.seek(0,0)
            i,sum=0,0
            line=c-1
            for i in range(line):
                linedata=fi.readline()
                length=len(linedata)
                print(length)
                sum+=length
            print(sum)
            sum=sum+f
            print(sum)
            fi.seek(sum)
            balance=str(bal)
            fi.write(balance)
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")
    def deposit(self,c):
        fi=open("bankk.txt","r+")
        line = linecache.getline("bankk.txt", c)
        sp=line.split(",")
        print(sp)
        f=line.rindex(sp[-1])
        print(f)
        print(self.balance)
        depositamt=int(input("Enter amount to be deposited "))
        self.balance=int(self.balance)+depositamt
        bal=self.balance
        print(bal)
        fi.seek(0,0)
        i,sum=0,0
        line=c-1
        for i in range(line):
            linedata=fi.readline()
            length=len(linedata)
            print(length)
            sum+=length
        print(sum)
        sum=sum+f
        print(sum)
        fi.seek(sum)
        balance=str(bal)
        fi.write(balance)
        print("Amount Deposited Successfully")
    def balance(self,c):
        print("Amount Available: "+self.balance)
def validatepwd(pwd):
    specialchar=['@','_','!','#','$','%','^','&','*','(',')','<','>','?','}','{',":"]
    if(len(pwd)<5 or len(pwd)>15):
        print("Password should be 5-15 characters")
    elif not any(i.isdigit() for i in pwd):
        print("Password should contain atleast one number")
    elif not any(i.isupper() for i in pwd):
        print("Password should contain atleast one Uppercase")
    elif not any(i.islower() for i in pwd):
        print("Password should contain atleast one lowercase")
    elif not any(i in specialchar for i in pwd):
        print("Password should contain atleast one special character")
    else:
        return True
def signup():
    f=open("bankk.txt","a")
    f.write("\n"+input("Enter name:")+",")#name
    while True:
        phone=input("Enter phone number:")#phone
        pattern = re.compile("(0/91)?[7-9][0-9]{9}")
        if(pattern.match(phone)):
            f.write(phone+",")
            break
    f.write(input("Enter username:")+",")#username
    while True:
        pas=input("Enter password")#password
        if(validatepwd(pas)):
            f.write(pas+",")
            break
    f.write(input("Enter email id:")+",")#email
    acno=random.randint(0000000000,9999999999)#random ac number
    #f.write("{}".format(acno))
    f.write(str(acno)+","+"0")
    print("Your Account Number is {0}".format(acno))
    f.close()
    print("Do you want to login")
    op=int(input("Enter 1.Yes 2.No"))
    if(op==1):
        login()
    else:
        sys.exit("Thank You")
def transopt(info,c):
    print("Welcome "+info[2])
    customer=bank(info[6])
    print("Enter 1.Withdraw 2.Deposit 3.Check Balance")
    option=int(input("Enter your choice"))
    if(option==1):
        customer.withdraw(c)
    elif(option==2):
        customer.deposit(c)
    elif(option==3):
        customer.check(c)
    else:
        print("Invalid Input")
        signupselect(info)
def login():
    f=open("bankk.txt","r+")
    uname=input("Enter username")
    pwd=input("Enter password")
    count=0
    for row in f:
        info=row.split(",")
        print(info)
        count=count+1
        if(uname==info[2] and pwd==info[3]):
            print(count)
            transopt(info,count)
            break
    else:
        print("Enter valid username password")
        login()
def main():
    print("1.Login 2.Signup")
    opt=int(input("Enter Your Choice: "))
    if(opt==1):
        login()
    elif(opt==2):
        signup()
    else:
        print("Invalid Choice")
        main()
if __name__ == '__main__':
    main()
