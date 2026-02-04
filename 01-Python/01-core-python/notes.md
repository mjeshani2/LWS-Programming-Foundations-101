## This file builds your foundational mental model for Python. It focuses purely on concepts—no code here—to help you think like Python does. Read it first to grasp why things work before touching code.

## Python Basics: Core Concepts
Python Syntax Overview
- Python uses clean, readable syntax with minimal punctuation. Keywords like if, for, and while are lowercase and reserved. Statements end with a newline (no semicolons needed, unlike C++ or Java). Comments start with #.

- Example look: variable = value (assignment uses =).

## How Python Executes Code
- Python is interpreted, not compiled. It reads your file line by line from top to bottom:

- The interpreter (like CPython) loads the file.

- It executes each line immediately, maintaining state (variables persist until changed or program ends).

- No separate "compile" step—errors show up as you run.

- This makes debugging fast but means order matters: define variables before using them.

## Indentation: Python's Secret Sauce
No curly braces {} or BEGIN/END. Indentation (spaces or tabs, usually 4 spaces) defines code blocks.

- Increases readability.

- Enforces structure: everything at the same indent level belongs together.

- Wrong indent? SyntaxError—Python treats it like a missing brace.

- Why it matters: Forces clean, nested code (e.g., inside loops or functions).

## Common Beginner Mistakes
- Forgetting indentation (most frequent SyntaxError).

- Using reserved words as variable names (e.g., class = 5).

- Mixing spaces and tabs (use spaces; editors like VS Code auto-fix).

- Assuming case-insensitivity (Python is case-sensitive: Var ≠ var).

- Global vs. local scope confusion (variables inside functions don't "leak" out).

## Variable Rules
Variables store data—think labeled boxes.

- Naming: Start with letter or _, then letters, digits, _. Case-sensitive, snake_case preferred (e.g., user_age).

- Dynamic typing: No need to declare type (age = 25 or age = "twenty-five"—Python figures it out).

- Assignment: name = value creates or updates.

- Immutability note: Numbers/strings can't change in place; lists/dicts can.

- Scope: Local (inside functions) shadows global—use global keyword sparingly.

Master these, and Python feels intuitive.