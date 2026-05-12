# Object-Oriented Programming: Class Usage Patterns

## Table of Contents

1. [Overview](#overview)
2. [Instance Properties](#1-instance-properties)
   - [Method A: Using `__init__`](#method-a-using-__init__)
   - [Method B: Using `@property` Decorator](#method-b-using-property-decorator)
3. [Class Methods](#2-class-methods)
   - [When to Use](#when-to-use)
   - [Example 1](#example-1-calling-class-methods-before-instantiation)
   - [Example 2](#example-2-calling-class-methods-from-properties)
4. [Static Methods](#3-static-methods)
   - [When to Use](#when-to-use-1)
5. [Quick Reference Table](#quick-reference-table)
6. [Best Practices](#best-practices)

---

## Overview

There are three primary ways to use classes in Python:

1. **Instance Properties** - Data and behavior tied to specific object instances
2. **Class Methods** - Methods that operate on class-level data
3. **Static Methods** - Utility functions grouped within a class

---

## 1. Instance Properties

Instance properties are attributes that belong to individual objects created from a class. They can be defined in two ways:

### Method A: Using `__init__`

```python
class Profile:
    def __init__(self) -> None:
        self.name = "Kevin Wasike Wakhisi"
        self.alias = "christianwhocodes"

my_profile = Profile()  # Parentheses required to instantiate
print(my_profile.name)   # Kevin Wasike Wakhisi
print(my_profile.alias)  # christianwhocodes
```

### Method B: Using `@property` Decorator

```python
class Profile:
    @property
    def motto(self) -> str:
        return "A child of the Most High God, highly favored and adored!"

my_profile = Profile()
print(my_profile.motto)  # Accessed like an attribute, not a method
```

**Output:**

```
Kevin Wasike Wakhisi
christianwhocodes
A child of the Most High God, highly favored and adored!
```

**Best Practice:** Define properties in `__init__` or use `@property` when you need computed attributes or controlled access.

---

## 2. Class Methods

Class methods operate on class-level data rather than instance data. They use `cls` instead of `self` and are decorated with `@classmethod`.

### When to Use

- When you need to modify class-level variables
- For alternative constructors
- When the method needs access to the class itself

### Example 1: Calling Class Methods Before Instantiation

```python
from typing import Optional

class Profile:
    # Class-level variable (private by convention)
    _name: Optional[str] = None

    def __init__(self) -> None:
        self.name = self._name  # Instance attribute set from class variable
        self.alias = "christianwhocodes"

    @property
    def motto(self) -> str:
        return "A child of the Most High God, highly favored and adored!"

    @classmethod
    def set_name(cls, provided_name: str) -> None:
        """Class method to modify class-level data"""
        cls._name = provided_name

# Usage
Profile.set_name("Kevin Wasike Wakhisi")  # Call on class, not instance
my_profile = Profile()

print(my_profile.name)   # Kevin Wasike Wakhisi
print(my_profile.alias)  # christianwhocodes
print(my_profile.motto)  # A child of the Most High God, highly favored and adored!
```

**Key Points:**

- Use `@classmethod` decorator (not `@property`)
- First parameter is `cls` (refers to the class)
- Can be called on the class itself: `Profile.set_name(...)`

### Example 2: Calling Class Methods from Properties

You can also call class methods from within instance properties to set class-level data dynamically:

```python
from typing import Optional

class Profile:
    # Class-level variable (private by convention)
    _name: Optional[str] = None

    def __init__(self) -> None:
        self.alias = "christianwhocodes"

    @property
    def motto(self) -> str:
        return "A child of the Most High God, highly favored and adored!"

    @classmethod
    def set_name(cls, provided_name: str) -> None:
        """Class method to modify class-level data"""
        cls._name = provided_name

    @property
    def name(self) -> str:
        self.set_name("Kevin Wasike Wakhisi")  # Call class method from property
        assert self._name is not None
        return self._name

# Usage
my_profile = Profile()
print(my_profile.name)   # Kevin Wasike Wakhisi
print(my_profile.alias)  # christianwhocodes
print(my_profile.motto)  # A child of the Most High God, highly favored and adored!
```

**Note:** In this pattern, the `name` property calls the class method `set_name()` internally, which modifies the class-level `_name` variable. This allows the property to dynamically set and return the value.

---

## 3. Static Methods

Static methods are regular functions grouped within a class for organizational purposes. They don't access instance or class data.

### When to Use

- For utility functions related to the class conceptually
- When you don't need access to `self` or `cls`
- To namespace related functions together

```python
class Profile:
    @staticmethod
    def name() -> str:
        return "Kevin Wasike Wakhisi"

    @staticmethod
    def alias() -> str:
        return "christianwhocodes"

    @staticmethod
    def motto() -> str:
        return "A child of the Most High God, highly favored and adored!"

# Usage - call directly on the class
print(Profile.name())   # Kevin Wasike Wakhisi
print(Profile.alias())  # christianwhocodes
print(Profile.motto())  # A child of the Most High God, highly favored and adored!
```

**Key Points:**

- Use `@staticmethod` decorator
- No `self` or `cls` parameter needed
- Called on the class: `Profile.name()`
- Essentially a regular function organized within a class

---

## Quick Reference Table

| Type                  | Decorator           | First Parameter | Access To             | Called On         | Use Case                                           |
| --------------------- | ------------------- | --------------- | --------------------- | ----------------- | -------------------------------------------------- |
| **Instance Property** | `@property` or none | `self`          | Instance data         | Instance          | Object-specific data/behavior                      |
| **Class Method**      | `@classmethod`      | `cls`           | Class & instance data | Class or Instance | Modify class-level data, alternative constructors  |
| **Static Method**     | `@staticmethod`     | None            | Nothing in class      | Class or Instance | Utility functions, no class/instance access needed |

---

## Best Practices

1. **Instance Properties (`self`)**: Use when data is specific to each object
2. **Class Methods (`cls`)**: Use when you need to work with class-level variables or create alternative constructors
3. **Static Methods**: Use for utility functions that are conceptually related to the class but don't need access to class or instance data

**Remember:** Always use parentheses when instantiating a class: `my_obj = MyClass()` not `my_obj = MyClass`
