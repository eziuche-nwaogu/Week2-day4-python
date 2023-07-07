## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
#Dog is-a object
class Dog(Animal):
    def __init__(self, name):
        #self has-a name
        self.name = name
#Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        #self has-a name
        self.name = name
#Person is-a object
class Person(object):
    def __init__(self, name):
        #self has-a name
        self.name = name
        ## Person has-a pet of some kind also a class
        self.pet = None
#Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        #employee has-a salary
        self.salary = salary
#Fish is-a fish
class Fish(object):
    pass
#Salmon is-a fish
class Salmon(Fish):
    pass
#halibut is-a fish
class Halibut(Fish):
    pass
## rover is-a Dog Object
rover = Dog("Rover")
#satan is-a cat
satan = Cat("Satan")
#mary is-a person
mary = Person("Mary")
#mary has-a pet
mary.pet = satan
#frank is-a employee
frank = Employee("Frank", 120000)
#frank has-a pet
frank.pet = rover
#flipper is-a fish
flipper = Fish()
#crouse is-a salmon
crouse = Salmon()
#harry is-a halibut
harry = Halibut()