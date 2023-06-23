# Python Notes

The more problems I do, the more python tricks I've learned. I made this file to store notes concerning python code that I could refer to in the future.
ctrl+shift+v to preview the file in VSCode

## General

### importing libraries

When you do `from itertools import *`, you are litering your namespace with variables. just import the methods that you need.

### Logging

It's better to use logging instead of print statements when you need to write stuff to the terminal, logs have a cleaner format.

### Unpacking

```python
mytuple=1,2
x,y=mytuple
#instead of doing x=mytuple[0]
```

### Declaring variables

You can declare multiple variables in one line, but don't abuse this or it will hurt the style of your code.

### The .zip(arg1,arg2) method

Can be used on multiple data structures, returns a zip object, which is an iterator of tuples. Used on items that have the same length; if the lengths are differet, then the iterator with the least items decides the length of the new iterator.
**note:** You can use enumerate and zip together if you need to acces the indices as well.

### Using Context Managers

Using a context manager, specifically the `with` statement, provides a more concise and structured way to handle resources and their associated cleanup in Python. While a try-except block can be used to handle exceptions, a context manager offers additional benefits:

1. Concise Syntax: The `with` statement provides a more compact syntax compared to the explicit try-except-finally blocks. It improves code readability and reduces the chance of forgetting to handle necessary cleanup steps.

2. Automatic Resource Management: Context managers automate the process of acquiring and releasing resources, such as opening and closing files, acquiring and releasing locks, or establishing and tearing down database connections. The `with` statement ensures that the cleanup actions are always executed, even if an exception occurs.

3. Clearer Code Structure: Context managers provide a clear structure to indicate the beginning and end of the managed block. It enhances code readability and makes it easier to understand the scope and lifetime of resources being managed.

4. Nested Context Management: Context managers can be nested, allowing you to handle multiple resources in a hierarchical manner. Each nested context manager will handle its own resource cleanup, simplifying the management of complex operations involving multiple resources.

Overall, context managers offer a more elegant and efficient way to handle resources and their associated cleanup in Python, resulting in cleaner code and improved resource management. However, there may be cases where a try-except block is more appropriate, such as when you need to handle exceptions in a specific way that is not covered by a context manager. It ultimately depends on the specific requirements and context of your code.

### try-except blocks

When writing except statements, never use a bare except (an except without the specifiying the type of error it is supposd to catch). In python, keyboard interrups and system exits are propagated using exceptions. so if you have a bare except, it is going to catch something like `ctrl+C`, which is usually not 
something we want to do.

### exponentiation

The correct operator for it is `**`, and not `^` (this one is bitwise XOR) 

## Strings

### Formatting

Once common way is to use concatination to form strings. However, fstrings are more readable, easier to write and less prone to error, so use them in most cases.
```python
print(f"Hello {username}! Welcome to {siteName}!")
```

## Dictionaries

If you are trying to loop over a dictionary, and need to access the items within the keys, then use `for key,val in d.items()` instead of having `elem=d[key]`
everywhere inside the loop

### The .get(arg1,arg2) method

Instead of checking whether a key exists with an if statement, use the .get() method, which will check and return the value if it exists, or initialize it will the value you pass to it as the second argument.
```python
dict1.get(key1,0)
```

## Functions

### Default Mutabale arguments

Argument defaults are defined when the function is defined, not when it's run. In the case below, every call to the function is sharing the same list.
So every time it's called, we are not starting with an empty list, but with whatever was left inside from the previous append call.
def append(n, l=[])...     => won't work as intended
-
def append(n, l=None):
    if l is None:
        l = []
...
This will work as intended.

## Files

### Opening/Closing Files

After you're done using a file, it's crucial to close it using f.close(). However, if operations before the close method throw an exception, then the file will never be closed. So either group the commands before in a try-except block, or use a with statement, which will ensure that th efile is closed even if an exception happens.
```python
with open(filename) as f:
    f.write("hello\n")
```

## Loops

With comprehensions, your code will become clearer and more concise. 
```python
dict_comp = {i: i * i for i in range(10)}
list_comp = [x*x for x in range(10)]
set_comp = {i%3 for i in range(10)}
gen_comp - (2*x+5 for x in range(10))
```

However, it's not always a good idea to use comprehensions, specially if it makes your code less readable.

## Types

### Checking types

Using == might result in unexpected behavior and violates an important principle, because of inheritance. For example, a namedtuple is a tuple, but not the built-in tuple; rather its subclass.
You should program in a way where the user can substitute a subclass for its parent class (Liskov Substitution Principle).
Using `isinstance(yourObj, tuple)` is a better idea.

Same goes for when you want to check if an object is None, True or False. instead of == use `is`. Don't check for equality, check for **identity** instead.