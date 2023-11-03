from core.base import Base

# extend the base class
class Test(Base):
    def initialize(self):
        print("Serving Initialization....")

    def update(self):
        pass


# instantiate class and run the program
Test().run()