# classes.py
# Simple class example with methods and representation.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        self.age += 1

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

if __name__ == "__main__":
    p = Person("Lina", 30)
    print(p.greet())
    p.have_birthday()
    print("After birthday:", p)