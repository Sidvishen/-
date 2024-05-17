def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
my_func_add = create_operation("add")
print(my_func_add(6,2.0))


multiply = lambda x, y: x * y
print(multiply(16, 16))

def multiply_def(x, y):
   return x * y
print(multiply_def(2, 3))


class Repeater:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return [self.value] * n

repeat_five = Repeater(2.4)
print(repeat_five(8))