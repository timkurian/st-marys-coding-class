# st-marys-coding-class
Coding classes for St marys class


# The Basics

## Variables

Variables are like boxes that can store something. Python will treat everything as a string unless you tell it to look like something else.

For example

```
x = "52"
y = "48"

print(f'{x+y}')

```

This wont print 100, it will print 5248 ! Why ? It didn't add the numbers together, it put them next to each other!

We need to tell python that this is a number , by not using `"`

```
x = 52
y = 48

print(f'{x+y}')

```

What if it comes from a user?

```
x = input('enter the value of x')
y = input('enter the value of y')

x = int(x)
y = int(y)
print(f'{x+y}')

```

In this example, we've used the `int()` function to convert it. There is `float()`  function for numbers with decimals


## Collections

Dictionarys use a key-value pair
Lists store items in an order
Sets store unique items in no order


## Functions

Functions help you group code together so that you can reuse it and call it when needed.

```
def my_function():
  print('Hello from my function')
```
