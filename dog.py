class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def dog_sit(self):
        print("狗狗坐")


    def dog_rool(self):
        print("狗狗打滚")


my_dog = Dog('tom', 1)
print("my dog name is " + my_dog.name.title() + ".")
print("my dog  is " + str(my_dog.age) + " year old.")
my_dog.dog_sit()
my_dog.dog_rool()
