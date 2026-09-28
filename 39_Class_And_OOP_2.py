class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a loud sound")

class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")

    def speak(self):
        print(f"{self.name} makes a loud sound")

dog1 = Dog("Joy", 13, "Husky")
dog2 = Dog("Jack", 5, "German Sheperd")
animal1 = Animal("Joy", 13)

animal1.speak()
print(dog2.name, dog2.age, dog2.breed)
dog1.bark()
dog2.speak()

