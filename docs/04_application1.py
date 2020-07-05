# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import json

data = json.load(open("file/data.json"))
# print(type(data))   # <class 'dict'>  dictionary type can help us find word and definition conveniently
# print(data)       # we will get a dictionary which contains key words and their definitions
# test
# print(data['rain'])
"""
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.',
 'To fall from the clouds in drops of water.']
"""


def translate(word):
    return data[word]

def main():
    word = input("Enter word: ")
    print(translate(word))
if __name__ == '__main__':
    main()