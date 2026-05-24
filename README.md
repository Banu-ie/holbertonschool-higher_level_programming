# Python - Everything is Object

This project explores how Python handles objects, references, mutability, and identity.

## Key Concepts

- Every value in Python is an object with an identity (`id()`), type (`type()`), and value
- `==` checks value equality; `is` checks identity (same object in memory)
- **Immutable types**: `int`, `float`, `str`, `tuple`, `bool`, `frozenset`
- **Mutable types**: `list`, `dict`, `set`
- CPython caches small integers (-5 to 256) and interned strings, so `is` may return `True` unexpectedly
- Assignment (`=`) creates a reference (alias), not a copy
- Functions receive object references — mutating a mutable object inside a function affects the caller; rebinding does not
