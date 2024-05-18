def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if is_prime_number(result):
            print("Простое")
        return result
    return wrapper
def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)