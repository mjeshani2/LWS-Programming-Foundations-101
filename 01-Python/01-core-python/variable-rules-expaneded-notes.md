## Variable Rules (Beginner-Friendly)

- A variable is just a **name** that points to some data stored in memory.
- You do not need to tell Python the type. Python figures it out automatically.

### Assignment
- Format: `variable_name = value`
- Example idea: a label stuck on a box
- You can reuse a variable by assigning a new value to it

---

## Naming Rules

### Valid Names
- Can use letters, numbers, and underscores
- Must start with a letter or `_`

Examples:
- `user_name`
- `_private`
- `score2`

### Invalid Names
- Cannot start with a number
- Cannot contain spaces or hyphens
- Cannot use Python keywords

Examples:
- `2score`
- `user-name`
- `if`

### Style Rule
- Use lowercase with underscores (snake_case)
- Constants are written in ALL_CAPS

---

## Mutability (Can the Value Change?)

### Immutable Types
These **cannot be changed** once created:
- `int`
- `float`
- `str`
- `bool`
- `tuple`

If you change the value, Python creates a **new object**.

---

### Mutable Types
These **can be changed** without creating a new object:
- `list`
- `dict`
- `set`

You can modify what’s inside them directly.

---

## Reassignment vs Modification

- Reassignment: variable points to a new value
- Modification: value itself changes

Example idea:
- Reassignment = replacing the box
- Modification = adding something inside the same box

---

## Important Idea

- Everything in Python is an object
- Variables point to objects in memory
- When you reassign, the variable points somewhere else
- Old objects are removed automatically if unused

---

## Key Takeaway
- Variables are labels, not boxes
- Same name can point to different objects over time
- Mutable objects change in place
- Immutable objects require reassignment
