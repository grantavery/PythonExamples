# all previous tutorials have been using
# procedure-oriented programming
# in this section, we'll make classes and do OOP stuff

# Objects can store data using ordinary variables that
# belong to the object. Variables that belong to an object
# or class are referred to as fields. Objects can also have
# functionality by using functions that belong to a class.
# Such functions are called methods of the class.
# This terminology is important because it helps us to
# differentiate between functions and variables which are
# independent and those which belong to a class or object.
# Collectively, the fields and methods can be referred to as
# the attributes of that class.
# Fields are of two types - they can belong to each
# instance/object of the class or they can belong to the class itself.
# They are called instance variables and class variables respectively.

# the 'self' in Python is equivalent to the 'this' reference in C# and Java


class Person:
    pass


p = Person()
print(p)
# result:
# <__main__.Person instance at 0x10171f518>

print()

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    # for doing initialization of the object
    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""

        print("Greetings, my masters call me {}.".format(self.name))

    # The how_many is actually a method that belongs to the class
    # and not to the object.
    # using the @classmethod decorator
    @classmethod
    def how_many(cls):
        """Prints the current population."""

        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()


# inheritance and polymorphism are both also things, duh



