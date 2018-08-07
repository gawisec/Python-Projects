## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## References Animal object. Is a class of Animal
class Dog(Animal):

    def __init__(self, name):
        ##??
        self.name = name

## References Animal object, is a class of animal.
class Cat(Animal):

    def __init__(self, name):
        ##??
        self.name = name

## References an object, has a class of object.
class Person(object):
    def __init__(self, name):
        ##??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## References person as an object.
class Employee(Person):

    def __init__(self, name, salary):
        ##Defines employee's initialization as a super class.
        super(Employee, self).__init__(name)
        ##Provides unique to its own, hence a salary.
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a type of fish. Has a relation to a fish.
class Salmon(Fish):
    pass

##Halibut is a type of fish. Has a relation to a fish.
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is a cat.
satan = Cat("Satan")

##Mary is a person.
mary = Person("Mary")

##Mary is a pet of satan.
mary.pet = satan

##Frank is a person, with employee characteristics, his name is Frank and with 12000 salary.
frank = Employee("Frank", 12000)

##Frank has a pet called rover.
frank.pet = rover

##Flipper is a fish.
flipper = Fish()

##Crouse is a salmon.
crouse = Salmon()

##Harry is a halibut.
harry = Halibut()