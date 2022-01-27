def myGenerator(n):
    for x in range(n):
        yield x**2

mini = myGenerator(10)

print(next(mini))
print(next(mini))
print(next(mini))
print(next(mini))
print(next(mini))
