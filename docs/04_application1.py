# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import json

data = json.load(open("file/data.json"))
print(type(data))   # <class 'dict'>  dictionary type can help us find word and definition conveniently
# print(data)       # we will get a dictionary which contains key words and their definitions
