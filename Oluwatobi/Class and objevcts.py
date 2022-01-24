class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)


person1 = Person("Mike", 30, 180)
print(person1)

person2 = Person("Charles", 20, 110)
del person2

print(Person.amount)
    
