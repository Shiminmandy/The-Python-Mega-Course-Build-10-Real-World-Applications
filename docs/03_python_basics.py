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

"""
18. writing text to a file
"""
with open("file/WeatherTemp.py", 'w') as newfile:
    newfile.write("hot")
print(newfile)
# if the file already exit, the file will cover the origin content
# if the file does not exit, python will create one in required place

"""
19.Appending Text to an Existing File
"""
with open("file/WeatherTemp.py", 'a+') as newfile2:  # + for updating
    newfile2.write("\ncold")
    newfile2.seek(0)  # because of the cursor, use built in function back to the 0 position
    get_content = newfile2.read()
print(get_content)

"""
20. Modules
"""
# import + modules' name
# get a list of modules
import sys
import time

print(sys.builtin_module_names)
# ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp',)
# ('_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp',)
# ('_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', )
# ('_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', )
# ('_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit',)
# ('audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', )
# ('msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
# these were written in C language inside the python software

# standard python modules
import os

# while True:
#     if os.path.exists("file/vegetables.txt"):
#         with open("file/vegetables.txt") as file:
#             print(file.read())
#     else:
#         print("File does not exist.")
#     time.sleep(3)  # because the file does not created, we will get File does not exist every 3 seconds

# third-party modules
# pip is used to install other third-party libraries
import pandas

while True:
    if os.path.exists("file/temps_today.csv"):
        data = pandas.read_csv("file/temps_today.csv")
        print(data.mean())
        print(data.mean()["st1"])  # 22.15
    else:
        print("File does not exist.")
    time.sleep(5)
# st1    22.15
# st2    20.55
# dtype: float64
