import mysql.connector
from tabulate import tabulate
con = mysql.connector.connect(host="localhost",user="root",password="root",database="bank_system")
import datetime as dt

def acc_opening():
    accno=int(input("enter account number: "))
    name=input("enter name: ")
    address=input("enter address: ")
    initial_deposit=int(input("enter initial deposit: "))
    cur=con.cursor()
    cur.execute("insert into bank_master values(%s,%s,%s,%s,%s);",(accno,name,dt.date.today(),address,initial_deposit))
    cur.execute("insert into bank_trans(accno,name,deposit,tdate,balance) values (%s,%s,%s,%s,%s);",(accno,name,initial_deposit,dt.date.today(),initial_deposit))
    con.commit()

#acc_opening()

def deposit():
    cur=con.cursor()
    accno=int(input("enter accno: "))
    amount=int(input("enter deposit amount: "))
    cur.execute("select * from bank_master where accno=%s",(accno,))
    row=cur.fetchone()
    cur.execute("update bank_master set balance=%s where accno=%s;",(row[4]+amount,accno))
    cur.execute("insert into bank_trans(accno,name,deposit,tdate,balance) values(%s,%s,%s,%s,%s);",(row[0],row[1],amount,dt.date.today(),row[4]+amount))
    con.commit()

#deposit()

def withdraw():
    cur=con.cursor()
    accno=int(input("enter accno: "))
    amount=int(input("enter withdraw amount: "))
    cur.execute("select * from bank_master where accno=%s", (accno,))
    row = cur.fetchone()
    cur.execute("update bank_master set balance=%s where accno=%s;", (row[4] - amount, accno))
    cur.execute("insert into bank_trans(accno,name,withdraw,tdate,balance) values(%s,%s,%s,%s,%s);",(row[0], row[1], amount, dt.date.today(), row[4] - amount))
    con.commit()

#withdraw()

def displayAll():
    cur = con.cursor()
    cur.execute("Select * from bank_master;")
    rows = cur.fetchall()
    print(tabulate(rows,headers=["Account Number","Name","Open date","Address","Balance"]))

#displayAll()

def displayOne():
    cur = con.cursor()
    accno = int(input("enter accno: "))
    cur.execute("Select * from bank_master where accno=%s;",(accno,))
    rows = cur.fetchall()
    print(tabulate(rows,headers=["Account Number","Name","Open date","Address","Balance"]))

#displayOne()

def change_name():
    cur=con.cursor()
    accno=int(input("enter account number: "))
    name=input("enter new name: ")
    cur.execute("update bank_master set name=%s where accno=%s;",(name,accno))
    con.commit()

#change_name()

def change_add():
    cur=con.cursor()
    accno=int(input("enter account number: "))
    address=input("enter new address: ")
    cur.execute("update bank_master set address=%s where accno=%s;",(address,accno))
    con.commit()

#change_add()

def statement():
    cur=con.cursor()
    accno=int(input("enter accno: "))
    cur.execute("select * from bank_trans where accno=%s;",(accno,))
    rows=cur.fetchall()
    for i in rows:
        print(i)

#statement()
