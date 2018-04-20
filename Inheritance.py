
class Animal:
    def eat(self):
        print ( "eating")

print( "Learning single inheritance\n__________________________________________________")
class Dog(Animal):
    def bark(self):
        print("barking ")
puppy = Dog()
puppy.eat()
puppy.bark()

# Applying multilevel inheritance
class BabyDog(Dog):
    def weeping(self):
        print(" babay dog is weeping")

print("Learning Multilevel inheritance\n_________________________________________________")
baby = BabyDog()
baby.eat()
baby.bark()
baby.weeping()

# Multiple nheritance
print( "Learning Multiple inheritance\n_________________________________________________")


class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")


class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")

Third()