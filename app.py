
# *****************STRING METHODS****************
# course = "Python Programming"
# print(course.upper())
# print(course.title())
# print(course.rstrip())
# print(course.find("gra"))
# print(course.replace("Python", "Python Course"))
# print("thone" not in course)
# print(course)


# ****************Numbers********************
import asyncio
import math

# print(10/3)
# print(10//3)
# print(10 % 3)
# print(10**3)

# x = 10
# x += 2
# print(x)

# print(round(5.321))
# print(abs(-90))

# print(math.ceil(4.1))
# print(math.fabs(-39))
# print(math.factorial(5))
# print(math.copysign(6, -2))

# x = int(input("x:"))
# y = x - 1
# print(y)
# print(type(y))

# print(bool(0))
# print(bool("anything!"))

# comparison operators
# print("bageeee" > "desf")
# print(20 == "20")

# Conditional Statements
# age = int(input("enter age:"))
# if age > 18:
#     print("age > 18")
# elif age <= 18:
#     print("age <= 18")
# else:
#     print("invalid number")

# # Ternary Operator
# age = int(input("enter your age:"))
# print("Eligible" if age > 18 else "Not Eligible")

# Logical Operators
# highIncome = False
# lowIncome = True

# if (highIncome or lowIncome) and not highIncome:
#     print("Great")
# else:
#     print("false")

# income = 20000
# if 1000 <= income < 30000:
#     print("Great income")

# **************LOOPS**************
# for num in range(1, 20, 2):
#     print("Number is:", num)
#     if num:
#         print("valid")
#     else:
#         print("Number is out of range")

# for x in range(1, 10):
#     print(x)
#     for y in range(1, 4):
#         for z in range(1, 6):
#             print(f"({x},{y},{z})")

# temp = 35
# if temp > 30:
#     print("its a hot day")
# elif temp < 30:
#     print("its a cool day")
# else:
#     print("its a day")

# age = 22
# if (age == 18 or age == 21):
#     print("Eligible")
# elif not age < 18:
#     print("not eligible")

# message = "Eligible" if age>18 else "Not eligilbe"
# print(message)

# valid = True
# for x in range(3,20,5):
#     print(x, x+2, "Hey its a for loop!")
#     for y in range(1,10,2):
#         print(y,x)
#         if valid:
#             print("Hey! Valid is true")
#             for z in range(1,10,2):
#                 print(type(range(z)))

# for x in [1,2,3,4,5,6]:
#     print("num=",x, x*2)

# number = 100
# while number > 0:
#     print(number)
#     number //=2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO",command)

# count = 0
# for x in range(1,10):
#     if(x%2==0):
#         count += 1
#         print(x)
# print(f"we have {count} even numbers")


# def greet(firstName,lastName):
#     return f"Hello {firstName} {lastName}"

# print(greet("Nawwal","Aftab"))

# def numIncrement(num, inc1 = 1, inc2 = 1):
#     return num + inc1 + inc2

# increment = numIncrement(10,2,2)
# print(increment)

# def multiply( num1 , num2):
#     result = num1 * num2
#     if(num1 % num2 == 0):
#         return f"{num1} and {num2} are even, Multiplication is {result}"

# num1 = int(input("enter a number:"))
# num2 = int(input("enter another number:"))

# print(multiply(num1, num2))

# def args(*numbers):
#     for num in numbers:
#         print(num)
#         return 0

# print(args("Apple","Banana"))


# def EvenOdd(num1, num2):
#     if(num1 % 2 == 0 or num2 % 2 == 0):
#         print(math.factorial(num1))
#         print(math.factorial(num2))
#     else:
#         print(num1.abs() * 3)
#         print(num2.abs() * 3)

# num1 = int(input("enter a number:"))
# num2 = int(input("enter a number:"))

# EvenOdd(num1,num2)

# def greet(firstName, lastName):
#     return f"Hello {firstName} {lastName}".title()

# print(greet("nawwal","aftab"))

# def userSummary(first_Name, last_Name, age):
#     fullName = f"{first_Name} {last_Name}".title()
#     print(fullName)

#     if age > 18:
#         print("Adult")
#     else:
#         print("Minor")

#     if age % 2 == 0:
#         print(math.factorial(age))
#     else:
#         print(age*3)

#     return f"Created a function that does: Takes first name, last name, and age as input Capitalizes the first and last nameChecks if the person is an Adult (18+) or MinorIf age is even, calculates the factorial of ageIf age is odd, multiplies age by 3Returns a summary message"

# fName = input("Enter your first name:")
# lName = input("Enter your last name:")
# age = int(input("Enter your age:"))

# userSummary(fName, lName, age)

# numbers = (1,2,3)
# numbers(0) = 3
# print(numbers)

# List = can be of any type and mutable
# Tuple = can be of any type but immutable
# Set = can be of any type and avoids duplicates
# Dict = key value pairs, mutable, keys are unique

# set1 = set({1,2,3,4,3,3,"nawwal","d","d",False})
# set1.add(20)
# print(set1)


# dict1 = {
#     "name":"Nawwal",
#     "age": 21,
#     "gender": "Male"
# }

# dict1["name"] = "Nawwal Aftab Waseer"
# dict1["city"] = "Karachi"
# dict1["age"] += 10

# dict1Keys = dict1.keys()
# dict1Valeus = dict1.values()
# dict1Items = dict1.items()

# print(dict1Keys)
# print(dict1Valeus)
# print(dict1Items)

# print(dict1)

# frozenSet = frozenset({1,2,3,3,4,2,3,4,5,6,7,6,7,6,6,8,})
# print(frozenSet)

# list1 = [x * x for x in range(1,10) if x%2 == 0]
# print(list1)

# set1 = {x for x in range(1,10,2) }
# print(set1)

# import math
# from functools import wraps

# def user_summary_decorator(func):
#     @wraps(func)
#     def wrapper(first_name, last_name, age):
#         fullName = f"{first_name} {last_name}".title()
#         print(f"Full Name: {fullName}")

#         if age > 18:
#             print("Adult")
#         else:
#             print("Minor")

#         if age % 2 == 0:
#             print(f"Factorial of age: {math.factorial(age)}")
#         else:
#             print(f"Age multiplied by 3: {age * 3}")

#         # Call the original function (optional)
#         return func(first_name, last_name, age)

#     return wrapper

# from my_utils import *

# print(math_utils.add(3,4))
# # print(string_utils.to_upper("hello"))

# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}

# merged = d1 | d2
# print(merged)

# my_set = {1,2,3,4}
# print(3 in my_set)

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(10, 20)

# print(p.x)
# print(p.y)

# import heapq

# nums = [5, 1, 8, 3]
# heapq.heapify(nums)
# print(nums)

# from collections import deque

# dq = deque([1,2,3])
# dq.appendleft(0)
# dq.append(4)

# print(dq)

# dq.popleft()
# dq.pop()

# print(dq)

# from queue import Queue

# q = Queue()
# q.put(1)
# q.put(2)

# print(q.get())
# print(q.get())


# import heapq

# nums = [5, 1, 8, 3]
# max_heap = [-n for n in nums]
# heapq.heapify(max_heap)

# largest = -heapq.heappop(max_heap)
# print("Largest:", largest)

# # Classes
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         print(f"Person {self.name}")

#     def __str__(self):
#         print(f"My name is {self.name}")

#     def __len__(self):
#         print(len(self.name))

#     def __getitem__(self):
#         print(self.name[2])

#     def __call__(self):
#         print(self.name,"hello!")

# p = Person("Nawwal", 22)
# print(p.name)
# print(repr(p.name))
# print(str(p.name))
# print(len(p.name))
# print(p.name[2])
# print(p.name)

# class Dog:
#     species = "4 wheelers"

#     def __init__(self, name):
#         self.name = name

# d1 = Dog("Sheru")
# d2 = Dog("Maxi")
# print(d1.species)
# print(d1.name)
# print(d2.name)

# #rasing exceptions
# def validate_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative!")
#     return age
# validate_age(2)

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print(result)
# except ZeroDivisionError:
#     print("You cannot divide by zero!")
# except ValueError:
#     print("Invalid input, please enter a number.")


# with open('textFile.txt', 'w') as file:
#     file.write("Adding Text!!!!!!!!!!\n")

# with open('textFile.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('textFile.txt', 'a') as file:
#     file.write("Added a new line!")

# with open('textFile.txt', 'r+') as file:
#     content = file.read()
#     print(content)

#     file.write("Again changed this using r+ mode")

# import os

# print(os.path.exists('textFile.txt'))
# print(os.path.abspath('textFile.txt'))
# print(os.path.isdir('my_utils'))
# print(os.path.isfile('textFile.txt'))

# numbers = [1,2,3,4,5]
# iteratable = iter(numbers)

# print(next(iteratable))
# print(next(iteratable))
# print(next(iteratable))
# print(next(iteratable))
# print(next(iteratable))

# #generators & yield
# def sumNumbers(n):
#     sum = 0
#     for x in range(n):
#         sum = sum + x
#         yield sum

# num = int(input("Enter a number:"))

# generator = sumNumbers(num)

# for value in generator:
#     print("Current sum",value)
#     input("enter to continue...")

# # square function using generator & yield
# def squareNumber(n):
#     square = 1
#     for i in range(n):
#         square = i * i
#         yield square

# number = int(input("Enter a numebr:"))

# generator = squareNumber(number)


# for value in generator:
#     print("current square is:",value)
#     input("press enter to continue...")

# # Custom iterators
# class MyCounter:
#     def __init__(self, max_num):
#         self.max_num = max_num
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= self.max_num:
#             num = self.current
#             self.current += 1
#             return num
#         else:
#             raise StopIteration

# counter = MyCounter(3)

# for num in counter:
#     print(num)


# # Partial functions
# from functools import partial

# def multiply(x, y):
#     return x * y


# times_five = partial(multiply, 5)

# print(times_five(3))
# print(times_five(10))

# # Map method
# numbers = [1,2,3,4,5]
# squared = map(lambda x: x*x, numbers)
# print(list(squared))

# from typing import List, Optional, Union, Literal, TypedDict

# def numbers_total(nums: List[int]) -> int:
#     return sum(nums)

# def greet(name: Optional[str] = None) -> str:
#     return f"Hello {name or 'Guest'}"

# def status(flag: Union[int, str]) -> str:
#     return f"Flag is {flag}"

# def confirm(answer: Literal['yes', 'no']) -> str:
#     return f"You answered {answer}"

# class Person(TypedDict):
#     name: str
#     age: int

# person: Person = {"name": "Nawwal", "age": 22}

# # runtime type checking using isinstance & get_type_hints
# def greet(value):
#     if isinstance(value, str):
#         print("this is a string")
#     elif isinstance(value,int):
#         print("this is a integer")
#     else:
#         print("unknown type")

# greet("nawwal")

# from typing import get_type_hints
# def greet1(name:str , age:int)->str:
#     return f"hello {name}, your age is {age} "
# print(get_type_hints(greet1))

# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int

# user = User(name="Nawwal", age="22")
# print(user)

# THREADING
import threading


def print_numbers():
    for i in range(5):
        print(f"Number: {i}")


thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# async/await in python

# Coroutine example
# async def main():
#     print("hello")
#     await asyncio.sleep(2)
#     print("after 5 seconds")

# asyncio.run(main())

# Task example
# async def greet():
#     print("hello!")
#     await asyncio.sleep(3)
#     print("after 3 seconds!")

# async def main():
#     task = asyncio.create_task(greet())
#     print("Task has started!")
#     await task


# asyncio.run(main())

# async code example
# async def downloadFile():
#     print("Downloading File...")
#     await asyncio.sleep(2)
#     print("File downloaded!")

# asyncio.run(downloadFile())


# Create three async functions:fetch_users(): waits 2 seconds, then prints "Users fetched!"fetch_orders(): waits 3 seconds, then prints "Orders fetched!"fetch_products(): waits 1 second, then prints "Products fetched!In the main() function:Start all 3 tasks concurrently using asyncio.create_task.After all fetches are done, print "All data fetched!".
async def fetchUsers():
    await asyncio.sleep(2)
    return "Users Fetched!"


async def fetchOrders():
    await asyncio.sleep(3)
    return "Orders Fetched!"


async def fetchProducts():
    await asyncio.sleep(1)
    return "Products Fetched!"


async def main():
    # task1 = asyncio.create_task(fetchUsers())
    # task2 = asyncio.create_task(fetchOrders())
    # task3 = asyncio.create_task(fetchProducts())
    # await task1
    # await task2
    # await task3

    result = await asyncio.gather(
        fetchUsers(),
        fetchOrders(),
        fetchProducts()
    )

    return result

asyncio.run(main())

# PDB DEBUGGING
# import pdb
# def add_numbers(a, b):
#     pdb.set_trace()  # 🔴 This pauses execution here
#     result = a + b
#     return result

# add_numbers(5, 3)
#added