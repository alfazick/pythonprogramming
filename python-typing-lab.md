# Python Type Hints Laboratory: Deep Dive into TypedDict and Annotated

## Introduction
This laboratory guide will walk you through the concepts of advanced type hinting in Python, with a special focus on `TypedDict` and `Annotated`. By the end of this lab, you'll understand how to use these tools to create more maintainable and type-safe Python code.

## Prerequisites
- Python 3.9+
- Basic understanding of Python dictionaries
- Understanding of type hints basics (str, int, etc.)

## Part 1: Understanding TypedDict

### What is TypedDict?
`TypedDict` is a special type that lets you define dictionaries with specific types for their keys. Unlike regular dictionaries where all values could be of any type, `TypedDict` enforces specific types for specific keys.

### Basic TypedDict Example
```python
from typing_extensions import TypedDict

class User(TypedDict):
    name: str
    age: int

# Valid usage
user: User = {"name": "John", "age": 30}

# Type checker would flag these as errors:
# user = {"name": "John", "age": "30"}  # age should be int, not str
# user = {"name": "John"}  # Missing required field 'age'
```

### Exercise 1.1: Creating Your First TypedDict
Create a `Product` TypedDict with the following fields:
- name: str
- price: float
- in_stock: bool

```python
class Product(TypedDict):
    name: str
    price: float
    in_stock: bool

# Test your implementation
product: Product = {
    "name": "Laptop",
    "price": 999.99,
    "in_stock": True
}
```

## Part 2: Advanced TypedDict Features

### Optional Fields
You can make fields optional using `NotRequired` from typing_extensions:

```python
from typing_extensions import TypedDict, NotRequired

class UserProfile(TypedDict):
    name: str  # Required
    age: int   # Required
    bio: NotRequired[str]  # Optional

# Both are valid:
user1: UserProfile = {"name": "Alice", "age": 25, "bio": "Python dev"}
user2: UserProfile = {"name": "Bob", "age": 30}  # bio is optional
```

### Nested TypedDicts
TypedDicts can be nested to create complex data structures:

```python
class Address(TypedDict):
    street: str
    city: str
    country: str

class Employee(TypedDict):
    name: str
    address: Address
    department: str

# Usage:
employee: Employee = {
    "name": "Jane",
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "country": "USA"
    },
    "department": "Engineering"
}
```

## Part 3: Understanding Annotated

### What is Annotated?
`Annotated` is a special type that allows you to add metadata to type hints without affecting runtime behavior. It's useful for documentation, validation, and framework-specific information.

### Basic Annotated Example
```python
from typing import Annotated

# Define a type with metadata
UserId = Annotated[int, "Must be positive"]
Username = Annotated[str, "Must be at least 3 characters"]

def create_user(user_id: UserId, username: Username) -> bool:
    # Runtime behavior isn't affected by annotations
    return True
```

### Exercise 3.1: Creating Validated Types
Create validated types for:
- Email (string with @ symbol)
- Age (integer between 0 and 150)
- Price (float greater than 0)

```python
Email = Annotated[str, "Must contain @ symbol"]
Age = Annotated[int, "Must be between 0 and 150"]
Price = Annotated[float, "Must be greater than 0"]

def validate_user(email: Email, age: Age) -> bool:
    # Implementation would go here
    pass
```

## Part 4: Combining TypedDict and Annotated

### Complex Example with Both Features
```python
from typing import Annotated, List
from typing_extensions import TypedDict
from decimal import Decimal

# Define validated types
PositivePrice = Annotated[Decimal, "Must be greater than 0"]
StockCount = Annotated[int, "Must be non-negative"]

class ProductInventory(TypedDict):
    product_id: str
    name: str
    price: PositivePrice
    stock: StockCount
    categories: List[str]

def update_inventory(
    product: ProductInventory,
    new_stock: StockCount
) -> ProductInventory:
    updated = dict(product)
    updated['stock'] = new_stock
    return updated
```

## Part 5: Best Practices and Tips

### 1. Type Checking
- Use a type checker like mypy or pyright
- Run type checking as part of your CI/CD pipeline
```bash
mypy your_file.py
```

### 2. Documentation
Always include meaningful annotations that help other developers:
```python
UserAge = Annotated[int, "Age in years. Must be between 0 and 150"]
```

### 3. Validation
Consider using Annotated types with validation libraries:
```python
from dataclasses import dataclass
from typing import Annotated
from pydantic import BaseModel, Field

# With Pydantic
class User(BaseModel):
    age: Annotated[int, Field(gt=0, lt=150)]
```

## Exercises

### Exercise 5.1: E-Commerce System
Create a complete e-commerce order system using TypedDict and Annotated:
- Order details
- Customer information
- Payment information
- Shipping details

### Exercise 5.2: Data Validation
Implement a validation system using the metadata from Annotated types:
- Create custom validators
- Implement error handling
- Add custom error messages

## Conclusion
You've learned how to:
- Create and use TypedDict for structured dictionary types
- Add metadata to types using Annotated
- Combine both features for complex type-safe applications
- Follow best practices for type hinting in Python

## Additional Resources
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [PEP 589 – TypedDict](https://www.python.org/dev/peps/pep-0589/)
- [PEP 593 – Annotated](https://www.python.org/dev/peps/pep-0593/)
