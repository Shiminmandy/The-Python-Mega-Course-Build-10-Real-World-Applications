# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
# import sqlite3
import psycopg2
""" 
1. Connect to a database
2. Create a cursor object
3.Write an SQL query
4. Commit changes
"""

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    # if you dont have this file the database will create one for u and the connection will be established
    cur = conn.cursor()  # cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # enter SQL code inside the brackets, SQL code always goes inside quotes
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('Wine Glass', 8,10.5)") 'Wine Glass' is TEXT, 8 is INTEGER, 10.5 is  REAL
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))  this is not a good way
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()





def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()


def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()


create_table()
# insert("Orange", 10, 15)
"""
go to 'tool'-->Query Tool, print 'SELECT * FROM store
"""
print(view())
# delete("Orange")
update(20, 15.0, "Apple")
# insert("Wine Glass", 8, 10.5)
# insert("Coffee Cup", 10, 5)
# delete("Coffee Cup")
# update(11,6,"Wine Glass")
# print(view())
# [('Coffee Cup', 10, 5.0), ('Coffee Cup', 10, 5.0), ('Coffee Cup', 10, 5.0)]