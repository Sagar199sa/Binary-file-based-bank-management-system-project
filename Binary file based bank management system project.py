#!/usr/bin/env python
# coding: utf-8

# In[30]:

import os
import pickle as pc
#Method for Admin Login
def adminLogin():
    login_id='admin'
    paswd='1234'
    uid=input('\n\tEnter user name : ')
    if uid==login_id:
        pas=input('\n\tEnter your login password')
        if pas==paswd:
            adminDashboard()
        else:
            print('\n\tEnterd password is incorrect.')
            input('\n\tPress enter to continue')
    else:
        print('\n\tUser dose not exists')
        input('\n\tPress enter to continue')

#Method to Add a customer

def addCustomer():
    file=open('bank.dat','ab')
    ac=input('\n\tEnter new account number : ')
    name=input('\n\tEnter the name of a costumer : ')
    mobile=input('\n\tEnter moblie number of a costumer : ')
    bal=input('\n\tEnter opening balance : ')
    paswd=input('\n\tEnter New password : ')
    pc.dump(ac,file)
    pc.dump(name,file)
    pc.dump(mobile,file)
    pc.dump(bal,file)
    pc.dump(paswd,file)
    print('\n\t---costumer added successfully---')
    input('\n\tPress enter to continue')
    file.close()

#Method to remove a cusomer

def removeCust(uid):
    userFound = 0
    try:
        file=open('bank.dat','rb')
        temp=open('temp.dat','ab')
        while True:
            data=pc.load(file)
            if data==uid:
                pc.load(file)
                pc.load(file)
                pc.load(file)
                pc.load(file)
                userFound = 1
            else:
                pc.dump(data,temp)
    except:
        file.close()
        temp.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")
    if(userFound==0):
        input("\n\tCustomer Not Found!\n\tPress Enter To Continue ...")
    else:
        input("\n\tCustomer Deleted Successfully!\n\tPress Enter To Continue ...")
#Method for update a customer

def updateCust(uid):
    uf=0
    try:
        file=open('bank.dat','rb')
        temp=open('temp.dat','ab')
        while True:
            data=pc.load(file)
            if data==uid:
                pc.dump(data,temp)
                name=pc.load(file)
                print('\n\tA/C no : ',data)
                print('\n\tName   : ',name)
                pc.dump(name,temp)
                pc.load(file)
                mob=input('\n\tEnter New mobile number: ')
                pc.dump(mob,temp)
                pc.dump(pc.load(file),temp)
                pc.load(file)
                pwd=input('\n\tEnter new password : ')
                pc.dump(pwd,temp)
                uf=1
            else:
                pc.dump(data,temp)
    except:
        file.close()
        temp.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")
    if(uf==0):
        input("\n\tCustomer Not Found!\n\tPress Enter To Continue ...")
    else:
        input("\n\tCustomer Updated Successfully!\n\tPress Enter To Continue ...")

#Method for view costumers

def viewCustomers():
    a=0
    try:
        file=open('bank.dat','rb')
        while True:
            data=pc.load(file)
            print(data,end=' ')
            a+=1
            if a%5==0:
                print()
    except:
        file.close()
    input('\n\tPress enter to continue!')
#method to view a costumer by their A/C

def viewCustomer(uid):
    userFound=0
    try:
        file=open('bank.dat','rb')
        while True:
            data=pc.load(file)
            if uid==data:
                print('\n\tThe available details of customer is mentioned below')
                print('\n\tName            : ',pc.load(file))
                print('\n\tcontact no      : ',pc.load(file))
                print('\n\tAccount Balance : ',pc.load(file))
                print('\n\tPassword        : ',pc.load(file))
                userFound=1
    except:
        file.close()
    if userFound==1:
        input('\n\tUser details fatched successfully!\n\tPress enter to continue!')
    else:
        input('\n\tUser dose not exist!\n\tPress Enter to continue!')
        
#Method for deposite a money in A/C

def deposite(uid,depp):
    userFound=0
    try:
        file=open('bank.dat','rb')
        temp=open('temp.dat','ab')
        while True:
            data=pc.load(file)
            if uid==data:
                name=pc.load(file)
                mob=pc.load(file)
                bal=int(pc.load(file))
                print('\n\tA/C no             : ',data)
                print('\n\tAcount Holder Name : ',name)
                print('\n\tCustomer Phone  no : ',mob)
                print('\n\tLast Balance        : ',bal)
                upbal=depp+bal
                print('\n\tUpdated Balance   : ',upbal)
                pc.dump(data,temp)
                pc.dump(name,temp)
                pc.dump(mob,temp)
                pc.dump(upbal,temp)
                pc.dump(pc.load(file),temp)
                userFound=1
            else:
                pc.dump(data,temp)
    except:
        file.close()
        temp.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")
    if(userFound==0):
        input("\n\tCustomer Not Found!\n\tPress Enter To Continue ...")
    else:
        input("\n\tTransection Successfully Completed!\n\tPress Enter To Continue ...")

#Method to withdrawl money

def withdrawl(uid,wit):
    userFound=0
    try:
        file=open('bank.dat','rb')
        temp=open('temp.dat','ab')
        while True:
            data=pc.load(file)
            if uid==data:
                name=pc.load(file)
                mob=pc.load(file)
                bal=int(pc.load(file))
                print('\n\tA/C no             : ',data)
                print('\n\tAcount Holder Name : ',name)
                print('\n\tCustomer Phone  no : ',mob)
                print('\n\tLast Balance        : ',bal)
                pc.dump(data,temp)
                pc.dump(name,temp)
                pc.dump(mob,temp)
                if bal>wit:
                    upbal=bal-wit
                    print('\n\tYour updated balance is ',upbal)
                    pc.dump(upbal,temp)
                    input('\n\tTransection completed successfully!')
                else:
                    input('\n\tinsufficient Balance\n\ttry Again ')
                    pc.dump(bal,temp)
                pc.dump(pc.load(file),temp)
                userFound=1
            else:
                pc.dump(data,temp)
    except:
        file.close()
        temp.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")
    if(userFound==0):
        input("\n\tCustomer Not Found!\n\tPress Enter To Continue ...")
    else:
        input("\n\tPress Enter To Continue ...")


#Method for admin dashboard
def adminDashboard():
    while True:  
        print('\n\t*****Welcome to ABC Bank Admin Dashboard*****')
        print("\n\t1. Add Customer")
        print("\n\t2. Remove A Customer")
        print("\n\t3. Update A Customer")
        print("\n\t4. View All Customers")
        print("\n\t5. View A Customer By A/c Number")
        print("\n\t6. Deposit")
        print("\n\t7. Withdrawl")
        print("\n\t8. Exit")
        choice = int(input("\n\tEnter Your Choice : "))
        if choice==1:
            addCustomer()
        elif choice==2:
            uid=input('\n\tEnter A/c number to remove a costumer: ')
            removeCust(uid)
        elif choice==3:
            uid=input('Please enter A/C no to update user details : ')
            updateCust(uid)
        elif choice==4:
            viewCustomers()
        elif choice==5:
            uid=input('\n\tenter A/C no to view customer details: ')
            viewCustomer(uid)
        elif choice==6:
            uid=input('\n\tenter A/C no deposite a money : ')
            depp=int(input('\n\tEnter an amount to deposite : '))
            deposite(uid,depp)
        elif choice==7:
            uid=input('\n\tenter A/C no Withrawal the money : ')
            depp=int(input('\n\tEnter an amount to Withdrawl : '))
            withdrawl(uid,depp)
        elif choice==8:
            print('\n\tthanks for visiting have a good day')
            break

#Method for Costumer Login

def cusLogin():
    userFound=0
    try:
        uid=input('\n\tEnter your user id to login your account: ')
        file=open('bank.dat','rb')
        while True:
            data=pc.load(file)
            if data==uid:
                userFound=1
                pc.load(file)
                pc.load(file)
                pc.load(file)
                pas=input('\n\tEnter your Password : ')
                pwd=pc.load(file)
                if pwd==pas:
                    file.close()
                    cusDashboard(uid)
                    break
                else:
                    input('\n\tEntered Wrong Password!\n\ttry again!')
    except:
        file.close()
    if userFound==0:
        input('\n\tWrong A/c NO!\n\tPleas try again')

#Method for Costumer Dashboard

def cusDashboard(uid):
    viewCustomer(uid)
    while True:
        print('\n\t*****Welcome User*****')
        print('\n\t1.Deposite')
        print('\n\t2.Withdraw')
        print('\n\t3.Update')
        print('\n\t4.Logout')
        choice=int(input('\n\tEnter your choice : '))
        if choice==4:
            input('\n\tThanks for visiting us!\n\tHave a Good day!')
            break
        elif choice==1:
            amt=int(input('\n\tEnter deposite amount : '))
            deposite(uid,amt)
        elif choice==2:
            amt=int(input('\n\tEnter withdrawl amount : '))
            withdrawl(uid,amt)
        elif choice==3:
            updateCust(uid)
        else:
            input('\n\tWrong input!\n\tTry again')
#Dashboard
while True:
    print('\t\n*****Welcome to ABC Bank Management System*****')
    print('\t\nPlease chose any one option')
    print('\t\nPress 1 for Admin Login')
    print('\t\nPress 2 for Costumer Login')
    print('\t\nPress 3 to Exit')
    ch=int(input('\t\nEnter any input of your choice : '))
    if ch==3:
        print('\n\tThanks for visiting us')
        break
    elif ch==1:
        adminLogin()
    elif ch==2:
        cusLogin()

