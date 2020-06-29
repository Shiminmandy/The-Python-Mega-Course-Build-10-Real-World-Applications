# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
"""
1. Find Definition
"""
help(list.append)  # Help on method_descriptor:

# append(self, object, /)
# Append object to the end of the list.
"""
2. List Slices
"""

lst = [12, 13.2, 65, 90, 45]
print(lst[0:3])    # [12, 13.2, 65] start from 0, end before 3
print(lst[:2])     # [12, 13.2] get the first two values
print(lst[3:])     # [90, 45] get the last two values
print(lst[-1])     # 45 the last value in the list
print(lst[-5])     # 12 the first value in the list
print(lst[:-1])    # [12, 13.2, 65, 90] get all values except the last value
print(lst[-5:-1])  # [12, 13.2, 65, 90]

"""
3. Slicing ListS and Strings
"""
lst2 = ['apple', 2, 'banana']
print(lst2[0])     # apple
print(lst2[0][4])  # e lst2[0] is a string

"""
4. Find Index of Value in a list
"""
print(lst2.index('apple'))       # 0
