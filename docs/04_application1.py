# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import json
from difflib import get_close_matches

data = json.load(open("file/data.json"))
# print(type(data))   # <class 'dict'>  dictionary type can help us find word and definition conveniently
# print(data)       # we will get a dictionary which contains key words and their definitions
# test
# print(data['rain'])
"""
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.',
 'To fall from the clouds in drops of water.']
"""
# start code
"""
1.考虑用户输入单词是否在字典包中
    若在，返回定义
    若不在，返回string
2.考虑大小写问题
    自动小写化用户输入的单词
3.考虑输入相似单词
    如果字典中与输入单词相似的单词超过0个
        询问是否需要第一个相似单词 y/n
        如果y，则返回第一个相似单词
        如果n，则返回message
4. output为list
    for loop 循环结果
4.考虑多次输入单词
"""


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:  # we will get several words that similar to the user input
        similar_word = get_close_matches(word, data.keys())[0]
        answer = input("Did you mean %s instead? Enter Y if yes, or N if no. " % similar_word)
        if answer == "Y" or answer == "y":
            return data[similar_word]
        elif answer == "N" or answer == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


def main():
    word = input("Enter word: ")  # global variable
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output )


if __name__ == '__main__':
    main()
