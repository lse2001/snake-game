class Animal:  # Notes on inheritance
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):  # super class

    def __init__(self):
        super().__init__()  # allows Fish class to inherit all the attributes and methods of the Animal class
        # Animal class is the super class
        # The call to super() in the initializer is recommended, but not strictly required

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water!")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# Slicing like a ninja!!
piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(piano_keys[2:5])  # prints indexes (2,4) ---> upper bound is excluded
print(piano_keys[2::])  # starts at index 2 and prints all the way to the end
print(piano_keys[:5:])  # starts at index 0, ends at index 4
print(piano_keys[::2])  # prints everything with a step of 2
print(piano_keys[::-1])  # prints the list starting from the end and goes to the beginning
# also works with tuples
# start : stop : step
