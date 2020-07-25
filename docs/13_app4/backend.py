# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


connect()