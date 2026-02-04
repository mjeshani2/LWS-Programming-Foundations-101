# Python Basics Notes

## 1. What Python Syntax Looks Like

- Python reads like plain text
- No semicolons at line ends
- New line = next instruction
- Uses simple keywords like `print`, `if`, `for`

### Comments
- Lines starting with `#` are ignored by Python
- Used for notes and explanations

---

## 2. How Python Runs Your Code

- Your code is executed top to bottom
- Python runs one line at a time
- Values stay in memory after being defined

### Execution Model
- File is loaded
- Line 1 executes
- Line 2 executes
- Continues until the end or an error

### Errors
- Execution stops at the error line
- Python shows the exact line number and reason

### Important Rule
- Variables and functions must be defined before use

---

## 3. Indentation (Structure Using Spaces)

- Python uses indentation instead of braces
- Indentation shows what belongs inside what
- Standard indentation is 4 spaces

### Indentation Rules
- Same block = same indentation level
- Wrong indentation causes `IndentationError`
- Do not mix tabs and spaces

---

## 4. Common Beginner Mistakes

| Mistake | Error | Fix |
|------|------|----|
| Missing indentation after `if` | SyntaxError | Add 4 spaces |
| Case mismatch (`Age` vs `age`) | NameError | Match variable name exactly |
| Variable starts with a number | SyntaxError | Start with letter or `_` |
| Mixing tabs and spaces | IndentationError | Use spaces only |
| Using keywords as names | SyntaxError | Rename variable |

### Rule
- Always read the error message carefully

---

## 5. Variables (Names for Values)

- Variables store data in memory
- Format: `name = value`
- Variables can be reused

### Naming Rules
- Must start with a letter or `_`
- Can contain numbers
- Cannot contain spaces or symbols
- Cannot be Python keywords

### Good Names
- `my_age`
- `_secret`
- `score1`

### Bad Names
- `2score`
- `my-age`
- `if`

### Style Convention
- Use lowercase with underscores

---

## 6. Data Types (Automatic in Python)

- Python assigns types automatically

### Common Types
- Integers: whole numbers
- Floats: decimal numbers
- Strings: text
- Lists: collections
- Booleans: `True` or `False`

---

## 7. Mutability (Change Behavior)

### Immutable Types
- `int`
- `float`
- `str`

- Changing value creates a new object

### Mutable Types
- `list`
- Objects can be changed in place

---

## 8. Memory Model (Conceptual)

- Variables point to objects in memory
- Reassigning changes the reference
- Old objects may be discarded

---

## 9. Scope

- Variables inside functions are local
- Variables outside functions are global
- Local variables are not accessible outside their scope

---

## 10. Practice Order

1. Run `hello.py`
2. Practice variables
3. Experiment with indentation
4. Read error messages