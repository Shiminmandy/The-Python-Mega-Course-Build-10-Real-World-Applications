# -*- coding:utf-8 -*-
# @Description: learn to use pandas
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import pandas

# pass lists
df1 = pandas.DataFrame([[10, 20, 30], [40, 50, 60], [70, 80, 90]], columns=['Price', 'Age', 'Value'],
                       index=['First', 'Second', 'Third'])
print(df1)
"""
        Price  Age  Value
First      10   20     30
Second     40   50     60
Third      70   80     90
"""
# pass dictionaries
df2 = pandas.DataFrame([{'Name': ['Shimin', 'Alex']}, {'surName': 'Jack'}])
print(df2)
# [{'Name': ['Shimin', 'Alex']}, {'Name': 'Jack'}]
"""
             Name
0  [Shimin, Alex]
1            Jack
"""
# [{'Name': ['Shimin', 'Alex']}, {'surName': 'Jack'}]
"""
             Name surName
0  [Shimin, Alex]     NaN
1             NaN    Jack
"""
print(type(df2))
# <class 'pandas.core.frame.DataFrame'>
# print(dir(df2)) we will get a list of method of pandas
print(df1.mean())
"""
Price    40.0
Age      50.0
Value    60.0
dtype: float64

"""
print(type(df1.mean()))
# <class 'pandas.core.series.Series'>
print(df1.Price)
"""
First     10
Second    40
Third     70
"""
print(df1.Price.mean())
# 40.0


# read csv file
df = pandas.read_csv("file/supermarkets.csv")
print(df)

# how to use lambda
"""
A lambda function is a small anonymous function
A lambda function can take any number of arguments, but can only have one expresion
"""
x = lambda a: a + 10
print(x(1))  # we will get 11
y = lambda a, b: a * b
print(y(1, 2))  # we will get 2


def myfunc(n):
    return lambda a: a * n


mytriper = myfunc(3)  # mytripler = a: a * 3
print(mytriper(100))  # 300     a = 100
