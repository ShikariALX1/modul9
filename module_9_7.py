def is_prime(func):
    def wrapper(*args, **kwargs):
        func2 = func(*args, **kwargs)
        if func2 > 1:
            for i in range(2, func2 + 1):
                if func2 % i == 0:
                    print("Составное")
        else:
            print("Простое")
        return func2
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
