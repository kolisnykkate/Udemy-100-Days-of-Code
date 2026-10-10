def add(*args):
    summ = 0
    print(args[0])
    print(type(args))
    for arg in args:
        summ += arg
    return summ

print(add(1,2,3,4,5,6,7,8,9))
print(add(10, 10, 10))
print(add(100, 11))

def calculate(n, m,  **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add'] # зазвичай при оголошенні функції до значення не доступаються за ключем,
    m *= kwargs['multiply'] # хоча це можна використати при перевірці умови if, напр. if key == "add"
    print(n)
    print(m)

calculate(2, 3, add = 3, multiply = 5)

class Car:

    def __init__(self, **kw):
        self.make = kw['make'] # in a dict we can get hold of a value through the square bracket method
        self.model = kw.get('model') # or use the .get() method
        self.year = kw.get('year') # does not crush if not specified
        # self.color = kwargs['color'] # crushes if not specified

my_car = Car(make = "Nissan", model = "Leaf")
print(my_car.model)
print(my_car.year)