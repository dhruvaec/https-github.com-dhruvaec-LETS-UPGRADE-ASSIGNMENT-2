#!/usr/bin/env python
# coding: utf-8

# In[1]:




# Questions 1:
# Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number.

my_list = []
# print(my_list)
for i in range(10):
    i = int(input())
    if (i % 2) == 0:
        my_list.append(i)
    else:
        continue

print(my_list)

# Output 1:
# []
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# Process finished with exit code 0

# Output 2 :
# []
# 10
# 17
# 21
# 20
# 30
# 14
# 41
# 71
# 57
# 92
# [10, 20, 30, 14, 92]
#
# Process finished with exit code 0

# Output 3:
#
# []
# 13
# 11
# 21
# 31
# 41
# 51
# 57
# 97
# 87
# 77
# []
#
# Process finished with exit code 0


# In[3]:


# Questions 2:
# Create a notebook on LIST COMPREHENSION. This exercise is to put you in a Self learning mode

my_list = []  # empty list creates
print("print empty list :", my_list)

my_list1 = [10, 20, 15, 68, 9, 56, 85, 95, 64, 58, 56, 32, 32]  # int List create

print("List of int :", my_list1)

mixed_list = [10, 'bogi', 20.0, "hydrabad"]
print("mixed list is :", mixed_list)

print('X' * 50)  

from collections import Counter

list = [1, 2, 3, 4, 5, 3, 2, 3, 4, 5, 6, 5, 4, 6, 7, 8, 9, 0, 7, 6, 5, 4, 6, 7, 7, 9]

print(Counter(list))

str = 'hi, i am from hydrabad itself and i am doing cdac in Data science '

word_list = str.split()

print(Counter(word_list))

print('X'*50)

# print(my_list.append(10))

print(my_list1.append(mixed_list))
print(my_list1[1])
print(my_list1[:3])
print(my_list1[3:])
# print(my_list1.count())
print('X'*50)

print(mixed_list)
mixed_list.remove(mixed_list[2])
print(mixed_list)

mixed_list.append("Tejas")
my_list1.append("Anusha")
print(mixed_list)

print(my_list1)
my_list1.remove(my_list1[3])
print(my_list1)

print('X'*50)


my_list.append(13)
my_list.append(11)
my_list.append(1)
my_list.append(2)
my_list.append(20)
my_list.append(17)

print(my_list)

my_list.remove(my_list[3])

print(my_list)

print("Unsorted list :",list)
list.sort()
print("Sorted list :",list)
print('X'* 50)
print("Sum of list  is :",sum(list))

print("ASCII : :",ascii(list))


# In[5]:


# Questions 3:
# You have seen in the videos how powerful dictionary data structure is.
# In this assignment, given a number n, you have to write a program that generates a dictionary d which
# contains (i, i*i), where i is from 1 to n (both included).
# Then you have to just print this dictionary d.
# Example:
# Input: 4
# will give output as
# {1: 1, 2: 4, 3: 9, 4: 16}
# Input Format:
# Take the number n in a single line.
# Output Format:
# Print the dictionary d in a single line.
# Example:
# Input:
# 8
# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

my_dictionary = {}
n = int(input())
my_dictionary = dict()

for i in range(1, n+1): # star and end value
    my_dictionary[i] = i*i

print(my_dictionary)


# Output :
# 5
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
# Process finished with exit code 0


# In[7]:


# Questions 4:
# There is a robot which wants to go the charging point to charge itself.
# The robot moves in a 2-D plane from the original point (0,0). The robot can
# move toward UP, DOWN, LEFT and RIGHT with given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
# The numbers after the direction are steps.
# Write a program to compute the distance between the current position after
# a sequence of movement and original point. If the distance is a float, then
# just print the nearest integer (use round() function for that and then convert
# it into an integer).
# Input Format:
# The first line of the input contains a number n which implies the number of
# directions to be given.
# The next n lines contain the direction and the step separated by a space.
# Output Format:
# Print the distance from the original position to the current position.
# Example:
# Input:
# 4
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Output:
# 2


position = {"x": 0, "y": 0}

fixNumber = int(input())
for i in range(fixNumber):

    inputValue = input()
    if not inputValue:
        break

    # print(inputValue)
    direction, steps = inputValue.split()
    # print(direction)

    if direction == "UP":
        position["y"] += int(steps)

    elif direction == "DOWN":
        position["y"] -= int(steps)

    elif direction == "LEFT":
        position["x"] -= int(steps)

    elif direction == "RIGHT":
        position["x"] += int(steps)

print(int(round((position["x"] ** 2 + position["y"] ** 2) ** 0.5)))  # Formula (x2 + y2)2



# In[ ]:




