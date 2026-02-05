## Purpose
Understanding different kinds of data in Python.  
Every value in Python has a **data type**, which tells Python what kind of data it is and what operations can be performed on it.

---

## Common Built-in Data Types

### 1. int (Integer)
- Used for **whole numbers**
- No decimal point

**Examples**
```python
age = 18
score = 100
temperature = -5
2. float (Floating-point number)
Used for numbers with decimal points

Examples

price = 99.99
pi = 3.14
height = 5.8
3. str (String)
Used for text

Always written inside quotes (single or double)

Examples

name = "Alex"
message = 'Hello, world'
game = "Minecraft"
4. bool (Boolean)
Used for true or false values

Only two possible values: True or False

Note: Capital T and F are required

Examples

is_logged_in = True
game_over = False
The type() Function
Used to check the data type of a value or variable

Syntax

type(value)
Examples

x = 10
print(type(x))        # <class 'int'>

y = 3.5
print(type(y))        # <class 'float'>

name = "Alex"
print(type(name))     # <class 'str'>

is_active = True
print(type(is_active)) # <class 'bool'>
Why Data Types Matter
Python behaves differently based on data type

Helps avoid errors

Makes code predictable and easier to understand

Example

print(10 + 5)        # 15 (math addition)
print("10" + "5")    # 105 (string joining)

## Learning Outcome

- By the end of this:

- You can identify int, float, str, and bool

- You can use type() to check data types

- You understand what kind of data you are working with before writing logic