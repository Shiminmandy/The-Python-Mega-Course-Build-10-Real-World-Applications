# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
"""
1. Find Definition
"""
help(list.append)  # Help on method_descriptor:
help(len)  # Help on built-in function len in module builtins:

# len(obj, /)
#     Return the number of items in a container.

# append(self, object, /)
# Append object to the end of the list.
"""
2. List Slices
"""

lst = [12, 13.2, 65, 90, 45]
print(lst[0:3])  # [12, 13.2, 65] start from 0, end before 3
print(lst[:2])  # [12, 13.2] get the first two values
print(lst[3:])  # [90, 45] get the last two values
print(lst[-1])  # 45 the last value in the list
print(lst[-5])  # 12 the first value in the list
print(lst[:-1])  # [12, 13.2, 65, 90] get all values except the last value
print(lst[-5:-1])  # [12, 13.2, 65, 90]

"""
3. Slicing ListS and Strings
"""
lst2 = ['apple', 2, 'banana']
print(lst2[0])  # apple
print(lst2[0][4])  # e lst2[0] is a string

"""
4. Find Index of Value in a list
"""
print(lst2.index('apple'))  # 0

"""
5.Create Your Own Functions
"""

# control + /
# # create a function to calculate the mean of a list
# def mean(mylist):  # inside the parenthesis is parameter(optional)/input, the input will be a list
#     the_mean = sum(mylist) / len(mylist)  # indent with four spaces
#     return the_mean
#     # print(the_mean)                     # it will print the same mean, but also with a None.
#     # Because python execute all lines above, they didn't see a return statement so they return a None in the output


# # call the function
# print(mean([34, 6, 7]))  # 15.666666666666666
# print(type(mean), type(sum))  # <class 'function'> <class 'builtin_function_or_method'>
# mymean = mean([90, 87, 90])
# print(mymean + 10)

"""
6. If Conditional
"""


# make some changes to the same function
# dict.keys() returns only key items
# dict.values() returns items without keys
def mean(value):
    if type(value) == dict:  # type() will return the type of input
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


# we want the function return the means even if the input is a dictionary
temp = {'morning': 26, 'noon': 30, 'evening': 20}
# find length of dictionary
print(len(temp))  # 3 the length of temp is 3
print(mean(temp))  # 25.3333333333333
