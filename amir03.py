class Person:
    def __init__(self, name, family, salary):
        self.__name = name
        self.__family = family
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salay(self, salary):
        self.__salary = salary

    def __add__(self, other):
        return self.__salary + other.__salary
    
    def __sub__(self, other):
        return self.__salary - other.__salary
    
    def __mul__(self, other):
        return self.__salary * other.__salary
    
    def __truediv__(self, other):
        if other.__salary > 0:
            return self.__salary / other.__salary
        else:
            return 0
        
    def __gt__(self, other):
        return self.__salary > other.__salary
    
    def __le__(self, other):
        return self.__salary < other.__salary

    def __eq__(self, other):
        return self.__salary == other.__salary

amirObj = Person("Amir", "solimani", 15000000)
rezaObj = Person("reaz", "Ahmadvandi", 12500000)
mehdiObj = Person("Mehdi", "amiri", 18500000)

# print(type(amirObj))

# print(amirObj + rezaObj)
# print(amirObj - rezaObj)
# print(amirObj * rezaObj)
# print(amirObj / rezaObj)

# print(amirObj > rezaObj)
# print(amirObj < rezaObj)
# print(amirObj == rezaObj)

def sumNumber(n):
    s = 0
    for i in range(n+1):
        s+= i
        yield s
    # return s
    

# print(sumNumber(10))
print(list(sumNumber(10)))