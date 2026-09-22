Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#OPERATORS
def add():
    a=6
    b=7
    c=a+b
    print(c)

    
add()
13

def add(a,b):
    c=a+b
    print(c)

    
add(5,3)
8

def add(a,b):
    c=a+b
    return c

print(add(8,7))
15

a=input("enter value a:")
enter value a:5
b=input("enter value b:")
enter value b:4
>>> c=a+b
>>> print(c)
54
>>> 
>>> #concatenation
>>> name="Menaga"
>>> name*6
'MenagaMenagaMenagaMenagaMenagaMenaga'
>>> name.format()
'Menaga'
>>> print("My name is {0} and my age is {1}".format(name,age))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print("My name is {0} and my age is {1}".format(name,age))
NameError: name 'age' is not defined
>>> age=24
>>> KeyboardInterrupt
>>> print("My name is {0} and my age is {1}".format(name,age))
My name is Menaga and my age is 24
>>> print("My name is {%s} and my age is {%d}",format(name,age))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print("My name is {%s} and my age is {%d}",format(name,age))
TypeError: format() argument 2 must be str, not int
>>> KeyboardInterrupt
>>> print("My name is {%s} and my age is {%d}".format(name,age))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print("My name is {%s} and my age is {%d}".format(name,age))
KeyError: '%s'
>>> KeyboardInterrupt
>>> KeyboardInterrupt
>>> print("My name is %s and my age is %d"%(name,age))
My name is Menaga and my age is 24
>>> "My name is ",name,"My age is ", age)
SyntaxError: unmatched ')'
>>> ("My name is ",name,"My age is ", age)
('My name is ', 'Menaga', 'My age is ', 24)
