# functions.py
# Define and call functions, including default args and docstrings.

def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting message for name."""
    return f"{greeting}, {name}!"

def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

if __name__ == "__main__":
    print(greet("Sam"))
    print(greet("Sam", "Welcome"))
    result = add(4, 5)
    print("4 + 5 =", result)
