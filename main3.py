
def greet(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


def display(*args):
    for arg in args:
        print(arg)

display("apple", "banana", "cherry")


def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Alice", age=20, roll_number=101)