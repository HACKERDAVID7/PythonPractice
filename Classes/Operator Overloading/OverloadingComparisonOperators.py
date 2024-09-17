'''
Advantages of Operator Overloading
Here are some advantages of operator overloading:

Improves code readability by allowing the use of familiar operators.
Ensures that objects of a class behave consistently with built-in types and other user-defined types.
Makes it simpler to write code, especially for complex data types.
Allows for code reuse by implementing one operator method and using it for other operators.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False