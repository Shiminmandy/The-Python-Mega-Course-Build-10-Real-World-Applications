# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1

"""
11. Dictionary Loop and String Formatting
"""
phone_numbers = {'Mike': '+017324005678', 'Jack': '+17324568967'}
# 1.
for key, value in phone_numbers.items():
    print(key, value)  # Mike +017324005678  Jack +17324568967
# 2.
for numbers in phone_numbers.items():
    print(numbers)  # we will get tuples: ('Mike', '+017324005678') ('Jack', '+17324568967')
# 3.
for numbers in phone_numbers.keys():
    print(numbers)  # only get names
# 4.
for numbers in phone_numbers.values():
    print(numbers)  # only get phone numbers
# 5. add string formatting
for key, value in phone_numbers.items():
    print("{} has the phone number {}".format(key, value))
    # Mike has the phone number +017324005678
    # Jack has the phone number +17324568967

"""
12. While Loops
"""
# answer = ''
# while answer != 'n':                         # if input is 'n', the loop will end
#     answer = input("Enter your answer:")
# other expression with break and continue


