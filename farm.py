import time

class FarmLocation:
    def __init__(self, spaces):
        self.spaces = spaces
        self.animals = []
        self.location_type = None

    def __str__(self):
        return f"{self.location_type} has {len(self.animals)}/{self.spaces} spaces filled"

    @property
    def is_full(self):
        if len(self.animals) >= self.spaces:
            return True
        return False
        
class Field(FarmLocation):
        def __init__(self, spaces):
            super().__init__(spaces)
            self.location_type = "field"
                
class Barn(FarmLocation):
        def __init__(self, spaces):
            super().__init__(spaces)
            self.location_type = "barn"

class Animal:
    animal_type = None
    
    def __init__(self, name, age, hungry):
        self.name = name
        self.age = age
        self.hungry = hungry
        self._stuff_in_belly = 0
        self._location = None

    def __str__(self):
        return (
            f"{self.name} is {self.age} years old. He is a {self.__class__.animal_type}."
            f" '{self.name}' jumps in the {self.location}"
        )

    @property
    def location(self):
        return self._location.location_type if self._location is not None else "void"
            

    def talk(self, sound="zzzZZzz"):
        return f"{self.name} says {sound}"

    def eat(self):
        if not self.is_hungry:
            return self.poop()
        self._stuff_in_belly += 1
        return f"{self.name} is eating"

    def poop(self):
        self._stuff_in_belly = 0
        return f"{self.name} poops, then looks relieved."

    @property
    def is_hungry(self):
        if self._stuff_in_belly > 2:
            return False
        return True
    
    def move(self, new_location):
        if self._location is new_location:
            return f"{self.name} is already here."
        
        if new_location.is_full:
            return f"{new_location.location_type} is full"

        if self._location is not None:
            self._location.animals.remove(self)

        
        self._location = new_location
        new_location.animals.append(self)
        return f"{self.name} moved to the {new_location.location_type}"
        
class Dog(Animal):
    animal_type = "dog"
    
    def talk(self, sound="Bark"):
        return super().talk(sound)

    def fetch(self, thing):
        print(f"{self.name} dashes after the {thing}...")
        time.sleep(0.5)
        print(f"{self.name} returns {thing} to you.")
        return thing
              
    def hungry(self):
        return f"{self.hungry}, they're always hungry."

class Cat(Animal):
    animal_type = "cat"

    def talk(self, sound="Meow"):
        return super().talk(sound)
    
    def description(self, sound):
        return f"{self.name} makes a meow {sound} sound."

class Cow(Animal):
    animal_type = "cow"
    
    def talk(self, sound="Mooo"):
        return super().talk(sound)

# Testing 
field = Field(2)
barn = Barn(1)
dog = Dog("fox", 6, "yes")
cat = Cat("lizzy", 9, "always")
dog.move(barn)

cat.move(field)
cat.move(barn)
print("Cat is in the", cat.location)
print("Field contains", field.animals)
