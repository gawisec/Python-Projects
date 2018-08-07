class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD, before parent altered()"
        super(Child, self).altered()
        print "CHILD, ALTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()