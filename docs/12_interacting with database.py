# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import sqlite3
import psycopg2
""" 
1. Connect to a database
2. Create a cursor object
3.Write an SQL query
4. Commit changes
"""

def create_table():
    conn = sqlite3.connect("lite.db")
    # if you dont have this file the database will create one for u and the connection will be established
    cur = conn.cursor()  # cursor object
    cur.execute("CREATE TABLE store (item TXET, quantity INTEGER, price REAL)")
    # enter SQL code inside the brackets, SQL code always goes inside quotes
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('Wine Glass', 8,10.5)") 'Wine Glass' is TEXT, 8 is INTEGER, 10.5 is  REAL
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()





def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

# insert("Wine Glass", 8, 10.5)
# insert("Coffee Cup", 10, 5)
# delete("Coffee Cup")
# update(11,6,"Wine Glass")
# print(view())
# [('Coffee Cup', 10, 5.0), ('Coffee Cup', 10, 5.0), ('Coffee Cup', 10, 5.0)]