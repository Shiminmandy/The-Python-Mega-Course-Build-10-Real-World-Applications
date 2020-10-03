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

"""
7. isinstance()
"""
print(isinstance(3, int))  # True
# skip the use of elif

"""
8. User Input
"""


def describe_weather(temperature):
    if temperature > 25:
        return 'Hot'
    elif 15 <= temperature <= 25:
        return 'Warm'
    else:
        return 'Cold'


user_input = input("please enter the temp:")  # users decide the value of temperature
print(type(user_input))  # <class 'str'>
# print(describe_weather(user_input))         # TypeError: '>' not supported between instances of 'str' and 'int'
print(describe_weather(float(user_input)))  # Because the type of temperature is string, we need to use float()

"""
9.String Formatting
"""
user_input = input("Enter your name:")
reply = "Hello %s!" % user_input  # use more before python 3.6
reply2 = f"Hello {user_input}"
reply3 = f'Hello "{user_input}"'  # use more after python 3.6, quotes for special requirement
print(reply)
# string formatting with multiple variables
# "Hello %s %s!" % (user_input1, user_input2)
# f"Hello {}, {}"

"""
10. For Loops
"""
temp = [10.1, 15.5, 8.9]
for temperature in temp:  # we can name whatever we want instead 'temperature'
    print(round(temperature))  # 10 16 9
    print('Done')
for letter in 'hello':
    print(letter.upper())  # H E L L O


# output will be : 10 Done 16 Done 9 Done H E L L O
# function + for loop


def celsius_to_kelvin(cels):
    return cels + 273.15


temp_lst = [8.8, 25, 15.6]
for temperature in temp_lst:
    print(celsius_to_kelvin(temperature))       # output would be 281.95 298.15 288.75
    
    
    
