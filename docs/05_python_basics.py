# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import mysql.connector

con = mysql.connector.connect(
    user="shimin",
    password="whatever",
    host="108.167.124.172",
    database="shimin_pmldatabase"
)
cursor = con.cursor()