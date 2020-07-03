# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
"""
16. Reading Text From a File
"""
myfile = open("subjects.txt", 'r')
# print(myfile.read())  # it will print the content inside the txt
# if we want to read the file two times
readfile = myfile.read()
# close file to delete memory
myfile.close()
print(readfile)
print(readfile)

# second way to read the file
with open("subjects.txt", 'r') as openfile:
    content = openfile.read()
print(content)

"""
17. Different Filepath
"""
# if file is in different path(outside), we will get FileNotFound error
with open("../sdfghj.py") as myfile2:
    content2 = myfile2.read()
print(content2)
#  different inner path
with open("file/WeatherTemp.py") as newfile:
    content3 = newfile.read()
print(content3)
