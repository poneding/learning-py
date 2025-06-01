print(">>> Function decorator:")

def before_call_code():
    print("Before calling the target function.")
def after_call_code():
    print("After calling the target function.")

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        before_call_code()
        result = original_function(*args, **kwargs)
        after_call_code()
        return result
    return wrapper_function

@decorator_function
def target_function(x, y):
    print(f"Executing target_function with arguments: {x}, {y}")
    return x + y

print("Calling target_function with decorator:")
result = target_function(5, 10)
print(f"Result of target_function: {result}")


print("\n>>> Decorator with arguments:")

def repeat(num_times):
    def decorator_repeat(original_function):
        def wrapper_function(*args, **kwargs):
            for _ in range(num_times):
                result = original_function(*args, **kwargs)
            return result
        return wrapper_function
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")
print("Calling greet with decorator:")
greet("Alice")


print("\n>>> Class decorator:")

def log_class(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def display(self):
            print(f"Class {cls.__name__} is being used.")
            result =  self.wrapped.display()
            print(f"Class {cls.__name__} finished execution.")
            return result
    return Wrapper

@log_class
class MyClass:
    def display(self):
        print("Executing MyClass.display() method.")

obj = MyClass()
obj.display()

print("\n>>> Singleton decorator:")

class SingletonDecorator:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

@SingletonDecorator
class DatabaseConnection:
    def __init__(self):
        print("Database initialized.")

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"db1 is db2: {db1 is db2}")


print("\n>>> Built-in decorators:")
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.name = "Alice"
print(f"Object name: {obj.name}")

print("\n>>> Multiple decorators on a single function:")
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One: Before function call.")
        result = func(*args, **kwargs)
        print("Decorator One: After function call.")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two: Before function call.")
        result = func(*args, **kwargs)
        print("Decorator Two: After function call.")
        return result
    return wrapper

@decorator_one
@decorator_two
def my_function():
    print("Executing my_function.")
print("Calling my_function with multiple decorators:")
my_function()