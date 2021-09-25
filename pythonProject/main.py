# from functools import reduce
#
# my_list = [1, 2, 3, 3, 4, 31, 321, 413, 42]
#
# print(reduce(lambda acc, item: acc + item, my_list))
# print(my_list)
#
#
# my_list1 = [55, 84, 55, 45, 44]
# print(list(map(lambda item: item**2, my_list1)))
#
# a = [(0, 2), (4, 3), (9, 9), (5, -1)]
#
# a.sort(key=lambda x: x[1])
#
# print(a)

# my_list = [char for char in 'hello']
# my_list2 = [num**2 for num in range(0, 10)]
# my_list4 = [num ** 2 for num in range(0, 100) if 0 == num % 2]
# print(my_list)
# print(my_list4)
# my_list = {char for char in 'hello'}
# my_list2 = [num**2 for num in range(0, 10)]
# my_list4 = {num ** 2 for num in range(0, 100) if 0 == num % 2}
# print(my_list)
# # print(my_list4)
# simple_dict = {
#     'a': 1,
#     'b': 2
# }
# my_dict = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
# print(my_dict)

# my_dict = {num:num*2 for num in [1, 2, 3]}
#
# print(my_dict)
#
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = list(set([x for x in some_list if some_list.count(x) >1]))
# print(duplicates)

# def hello(func):
#     func()
#
# def greet():
#     print('still here!"')
#
# a = hello(greet)
#
# print(a)

# def greet(func):
#     func()
#
#
# def greet2():
#     def func():
#         return 5
#     return func
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('*****')
#         func(*args, **kwargs)
#         print('*****')
#     return wrap_func
#
#
# @my_decorator
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)
#
#
# hello('hi')

# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'Took {t2-t1} s')
#         return result
#     return wrapper
#
#
#  @performance
#  def long_time():
#      for i in range(100000000):
#          i**100
#
#  long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sona',
#     'valid': False #changing this will either run or not run the message_friends function.
# }
#
# def authenticated(fn):
#   def wrapper(*args, **kwargs):
#     if args[0]['valid']:
#         return fn(*args, **kwargs)
#   return wrapper
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user1)

# while True:
#     try:
#         age = int(input('What is your age ?'))
#         print(10/age)
#         raise Exception('Hey cut it out')
#     except ValueError:
#         print('Please enter a number')
#         continue
#     except ZeroDivisionError:
#         print('Please enter age higher 0')
#         break
#     else:
#         print('Thank you')
#     finally:
#         print('ok, I am finally done')
#     print('can you hear me')


# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)
#
#
# print(sum(1, '2'))

# range(100)
# list(range(100))
#
#
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i**20)
#     return result
#
#
# my_list = make_list(10000)
# print(my_list)

# def generator_function(num):
#     for i in range(num):
#         yield i
#
#
# g = generator_function(1)
# next(g)
# next(g)
# print(next(g))

# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(took {t2-t1} s')
#         return result
#     return wrapper
#
#
# @performance
# def long_time():
#     for i in range(100000000):
#         i**100
#
# long_time()

# from time import time
#
#
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f 'Took {t2 - t1} s')
#         return result
#
#     return wrapper
#
#
# @performance
# def long_time():
#     print('1')
#     for i in range(10000000):
#         i * 10
#
#
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(10000000)):
#         i * 10
#
#
# long_time()
# long_time2()


# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator)*2)
#         except StopIteration:
#             break
#
# special_for([1, 2, 3])

# class MyGen():
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration
#
# gen=MyGen(0, 100)
# for i in gen:
#     print(i)


# def fib(number):
#     f0=0
#     list = [0]
#     for i in range(number):
#         list.append(number*5)
#     return list
#
# fib_list = fib(20)
#
# print(fib_list)

# def fib(num):
#     result = [0, 1]
#     for i in range(num):
#         next_item = result[i] + result[i + 1]
#         result.append(next_item)
#     return result
#
#
# fib_list = fib(4)
# # print(fib_list)
#
#
# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
#
#
# fib_number = int(input('Enter require number : '))
#
# for x in fib(fib_number+1):
#     pass
# print(x)
# from utility import *
# from shopping.more_shopping import shopping_cart
# if __name__ == '__main__':
#     print(divide(4,3))
#     print(shopping_cart.buy('apple'))
#     print(max([1, 2, 3]))
#     print(maxi())
#     print(__name__)
#
# class Student():
#     pass
#
#
# st1 = Student()
# print(type(st1))
# import pyjokes
#
# joke = pyjokes.get_joke('en', 'neutral')
# print(joke)

# from collections import Counter, defaultdict, OrderedDict
#
# li = [1, 2, 3, 4, 5, 6, 7, 7]
# sentence = 'Hello'
# print(Counter(li))
# print(Counter(sentence))
#
# dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
# print(dictionary['c'])
#
# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2
# d2 = OrderedDict()
# d2['a'] = 1
# d2['b'] = 2
# print(d2 == d)

# import datetime
#
# print(datetime.date.today())
#
# from time import time
# print(time())

# from array import array
#
# arr = array('i', [1, 2, 3])
#
# print(arr)

# import pdb
#
# def add(num1, num2):
#     pdb.set_trace()
#     t=4*54
#     return num1+num2
#
#
# add(4, 5)

# my_file = open ('test.txt')
#
# print(my_file)

#
# import re
#
# pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = 'bv.com'
# pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,12}\d")
# password = "gagafaf#4rsw"
# a = (pattern.search(string))
# check = pattern2.fullmatch(password)
# print(check)


# import re
# p = input("Input your password")
# x = True
# while x:
#     if len(p) < 6 or len(p) > 12:
#         break
#     elif not re.search("[a-z]", p):
#         break
#     elif not re.search("[0-9]", p):
#         break
#     elif not re.search("[A-Z]", p):
#         break
#     elif not re.search("[$%#@]", p):
#         break
#     elif re.search("\s", p):
#         break
#     else:
#         print("Valid Password")
#         x = False
#         break
#
#
# if x:
#     print("Not a Valid Password")

# def do_stuff(num=0):
#     try:
#         if num:
#             return int(num)+5
#         else:
#             return 'please enter a number'
#     except ValueError as err:
#         return err

import sys
from random import randint
start = int(sys.argv[1])
end = int(sys.argv[2])

generated_num = randint(start, end)

while True:
    try:
        guess_num = int(input(f'Please give a number in range {start}, {end} '))
        if guess_num < start or guess_num > end:
            print('Out of range')
            continue
        if guess_num == generated_num:
            print('You are genius')
            break
        else:
            print('Try again')
    except ValueError:
        print('Please enter a number')