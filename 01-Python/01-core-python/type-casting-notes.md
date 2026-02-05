# Type Casting in Python

---

## Why Type Casting Is Needed

### Example
```python
age = "18"
print(age + 1)
```

### Reason
- "18" is a string
- 1 is an integer

Python cannot add a string and an integer.

### Correct usage
```python
age = int(age)
print(age + 1)
```

Type casting prevents runtime errors and makes programs safer and more predictable.

---

## 3. int() – Converting to Integer

### Description
`int()` converts a value into a whole number.

### Valid conversions
- "10" → 10
- 12.9 → 12
- 5 → 5

### Invalid conversions
- "10.5"
- "ten"
- "abc"

### Rule
`int()` works only with integers or numeric strings that represent whole numbers.

---

## 4. float() – Converting to Floating-Point Number

### Description
`float()` converts a value into a decimal number.

### Valid conversions
- "10" → 10.0
- "10.5" → 10.5
- 7 → 7.0
- 12 → 12.0

Use `float()` when decimal precision is required.

---

## 5. str() – Converting to String

### Description
`str()` converts any data type into text.

### Examples
- 10 → "10"
- 5.5 → "5.5"
- True → "True"

### Common use cases
- Displaying values using `print()`
- Combining numbers with text

### Example
```python
score = 100
print("Your score is " + str(score))
```

---

## 6. input() and Type Casting

The `input()` function always returns a string, even if the user types a number.

### Example
```python
age = input("Enter your age: ")
print(type(age))
```

Output:
```text
<class 'str'>
```

### Incorrect usage
```python
age = input("Enter your age: ")
print(age + 1)
```

### Correct usage
```python
age = int(input("Enter your age: "))
print(age + 1)
```

---

## 7. Common Beginner Errors

### Error 1: Mixing strings and numbers
```python
print("Age: " + 18)
```

Fix:
```python
print("Age: " + str(18))
```

---

### Error 2: Converting decimal strings using int()
```python
int("10.5")
```

Fix:
```python
float("10.5")
```

---

### Error 3: Converting non-numeric strings
```python
int("hello")
```

Explanation:
Only numeric values can be converted using `int()` or `float()`.

---

## 8. Type Casting Comparison Table

| Function | Converts To | Accepts | Example Input | Example Output | Common Use Case |
|--------|------------|---------|---------------|----------------|-----------------|
| `int()` | Integer | Whole numbers, numeric strings | "10" | 10 | Whole-number calculations |
| `float()` | Decimal | Numbers, numeric strings | "10.5" | 10.5 | Decimal calculations |
| `str()` | String | Any data type | 100 | "100" | Printing and text formatting |

---

## 9. Learning Outcomes

After studying this topic, you should be able to:
- Convert between basic Python data types
- Handle user input safely
- Avoid common beginner runtime errors
- Understand why type mismatches cause program crashes

---

## 10. Quick Summary

- `int()` is used for whole numbers
- `float()` is used for decimal numbers
- `str()` is used for text conversion
- `input()` always returns a string
- Type casting is essential for safe and error-free programs
