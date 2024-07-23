# DocStrings
# Annotations

DocStrings are string literals that appear right after the definition of a function, method, class, or module. They provide a convenient way to associate documentation with Python modules, functions, classes, and methods. Function annotations, introduced in Python 3, offer a way to attach metadata to function parameters and return values.

# Lambda Expressions

Lambda expressions in Python are small anonymous functions that can have any number of arguments but can only have one expression. They are useful for creating short, one-time-use functions without formally defining them using the def keyword.

# Lambdas and Sorting

Lambda functions are often used in sorting operations, particularly with the sort() method or sorted() function. They provide a quick way to specify custom sorting criteria for complex data structures like lists of tuples or dictionaries.

# Function Introspection

Function introspection refers to the ability to examine attributes about objects like functions at runtime. Python provides several built-in functions and attributes for introspection, such as dir(), type(), id(), __name__, and __doc__.

# Callables

In Python, a callable is any object that can be called like a function. This includes user-defined functions, built-in functions, methods of classes, class objects, and instances of classes that implement the __call__ method.

# Map, Filter and Zip

map(): Applies a given function to each item in an iterable and returns an iterator of results.
filter(): Creates an iterator from elements of an iterable for which a function returns True.
zip(): Creates an iterator of tuples where each tuple contains the i-th element from each of the input iterables.

These functions are key components in functional programming, allowing for efficient data manipulation without explicit loops.

# Reducing Functions

Reducing functions, like reduce() from the functools module, apply a function of two arguments cumulatively to the items of a sequence, reducing it to a single value. This is useful for performing computations on lists where you want to combine elements.

# Partial Functions

Partial functions, created using functools.partial(), allow you to fix a certain number of arguments of a function and generate a new function. This is useful when you want to create a new function with some preset parameters from an existing function.

# Operator Module

The operator module provides a set of efficient functions corresponding to the intrinsic operators of Python. It's particularly useful in functional programming contexts, offering alternatives to lambda functions for common operations.
These concepts form the foundation of functional programming in Python, enabling more concise, readable, and often more efficient code. By mastering these techniques, developers can write more elegant and powerful Python programs.

time_it(fn, *args, repetitions= 1, **kwargs)
This is a genralized function to call any function user specified number of times and return the average time taken for calls

squared_power_list
Retruns list by raising number to power from start to end -> number**start to number**end. Default start is 0 and end is 5"

polygon_area
Returns area of a regular polygon with number of sides between 3 to 6 bith inclusive

temp_converter 
Converts temprature from celsius 'c' to fahrenheit 'f' or fahrenheit to celsius

speed_converter
Converts speed from kmph (provided by user as input) to different units dist can be km/m/ft/yrd time can be ms/s/min/hr/day