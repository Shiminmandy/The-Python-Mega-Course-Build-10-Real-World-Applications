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
while True:
    answer = input("Enter your answer:")
    if answer == 'n':
        break
    else:
        continue

"""
13. Building the Maker function
"""


# help(str.startswith)


def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")  # it should be a tuple inside the built in function str.startwith()
    capitalized = phrase.capitalize()  # str.title() capitalizes every word's first letter
    # if it is true that the start of phrase is included in the tuple
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    user_input = input('Say something: ')
    if user_input == "\end":
        break
    else:
        # results.append(user_input)

        # print(results)         # ['how are you', 'the weather is good']
        results.append(sentence_maker(user_input))

# print(results)                   # ['How are you?', 'The weather is good.']
print(" ".join(results))           # How are you? Pretty good.

"""
14. List
"""
# 1. each value in the list divided by 10
temps = [221, 234, 340, 230]
new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
print(new_temps)                   # [22.1, 23.4, 34.0, 23.0]

# 2. other way to solve
new_temps = [temp / 10 for temp in temps]
print(new_temps)                   # [22.1, 23.4, 34.0, 23.0]

# 3. with if conditional
temps2 = [221, 234, 340, -100, 230]
new_temps2 = [temp /10 for temp in temps if temp != -9999]
print(new_temps2)                  # [22.1, 23.4, 34.0, 23.0]

# 4. with if/else conditional
new_temps3 = [temp / 10 if temp != -100 else 0 for temp in temps2]
print(new_temps3)                  # [22.1, 23.4, 34.0, 0, 23.0]

