#Quinton Dean
#This program creates a simple DB using sqlite3 in python

import sqlite3
myDB = sqlite3.connect(':memory:')

cursDB = myDB.cursor()

def createTable():
    cursDB.execute('CREATE TABLE Inventory(number INTEGER PRIMARY KEY, name TEXT, provider TEXT, price REAL, quantity INTEGER)')

'''cursDB.execute('CREATE TABLE Inventory(number INTEGER PRIMARY KEY, name TEXT, provider TEXT, price REAL, quantity INTEGER)')'''

def addCust(number, name, provider, price, quantity):
    cursDB.execute('''INSERT INTO Inventory (number, name, provider, price, quantity) VALUES (?,?,?,?,?)''',(number,name,provider,price,quantity))

'''cursDB.execute('INSERT INTO Inventory VALUES(03200, "Milk", "Borden", 3.59, 1200)')
cursDB.execute('INSERT INTO Inventory VALUES(03201, "Ice cream", "Haagen Dazs", 5.29, 100)')
cursDB.execute('INSERT INTO Inventory VALUES(05632, "Lemon juice", "Simply orange", 3.49, 500)')
cursDB.execute('INSERT INTO Inventory VALUES(23790, "Energy drink", "Monster energy", 28.99, 700)')
cursDB.execute('INSERT INTO Inventory VALUES(23791, "Sprite", "Coca Cola", 12.79, 2000)')'''


def main():
    createTable()

    addCust('03200', "Milk", "Borden", 3.59, 1200)
    addCust('03201', "Ice cream", "Haagen Dazs", 5.29, 100)
    addCust('05632', "Lemon juice", "Simply orange", 3.49, 500)
    addCust('23790', "Energy drink", "Monster energy", 28.99, 700)
    addCust('23791', "Sprite", "Coca Cola", 12.79, 2000)

    myDB.commit()
    print('This is A')
    cursDB.execute('SELECT * FROM Inventory')
    for i in cursDB:
        print("\n")
        for j in i:
            print(j)
    print('This is C')
    cursDB.execute('SELECT * FROM Inventory WHERE quantity < 1000')
    for i in cursDB:
        print("\n")
        for j in i:
            print(j)
    print('This is D')        
    cursDB.execute('SELECT name,price,quantity FROM Inventory')
    for i in cursDB:
        print("\n")
        for j in i:
            print(j)
    print('This is E')
    cursDB.execute('SELECT COUNT(*) FROM Inventory')
    print(i)

    myDB.close()
main()
