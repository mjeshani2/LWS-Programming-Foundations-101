## Variable Rules (Expanded)
- Variables are dynamic references to objects in memory—no type declarations needed.

- Assignment: variable_name = value binds the name to an object. Reuse with new_value = old_variable.

## Naming Conventions:

- Valid: Letters, digits (not first), underscores: user_name, _private, score2.

- Invalid: Starts with digit (2score), spaces, hyphens, keywords (if = 1).

- Style: snake_case for variables (PEP 8 standard). Constants: ALL_CAPS.

## Mutability Basics:

- Immutable (can't change in place): int, float, str, bool, tuple. Reassignment creates new object.

- Mutable (change contents): list, dict, set. Modify without reassigning name.

- Rebinding: x = 5; x = "hi"—old int object garbage collected.

- Key Insight: Everything's an object. id(variable) shows memory address—see rebinding effects.