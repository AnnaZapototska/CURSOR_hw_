# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class
#
# class Animals:
#     """
#     Parent class, should have eat, sleep
#     """
# class Animal1(Animal):
#     """
#     Some of the animal with 1-2 extra methods related to this animal
#     """

class Animals:
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print(f'{self.__class__.__name__} sleeping')
    def eat(self):
        print(f'{self.__class__.__name__} eating')

class Dog(Animals):
    def barks(self):
        print(f"{self.__class__.__name__} barking")

class Cat(Animals):
    def mew(self):
        print(f'{self.__class__.__name__} meow')

class Cavy(Animals):
    def cheep(self):
       print(f'{self.__class__.__name__} cheeping')

class Lion(Animals):
    def roar(self):
        print(f'{self.__class__.__name__} roar')

class Frog(Animals):
    def croaks(self):
        print(f'{self.__class__.__name__} croaks')

dog = Dog('Sam')
cat = Cat('Murka')
cavy = Cavy('Koki')
lion = Lion('Din')
frog = Frog('Didi')

cat.sleep()
dog.barks()
cavy.cheep()

for item in (dog, cat, cavy, lion, frog):
    print(isinstance(item, Animals))

# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.
#
#  class Human:
#     """
#     Human class, should have eat, sleep, study, work
#     """
#  class Centaur(.. , ..):
#     """
#     Centaur class should be inherited from Human and Animal and has unique method related to it.
#     """

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} eating")
    def sleep(self):
        print(f"{self.name} sleeping")
    def study(self):
        print(f"{self.name} studying")
    def work(self):
        print(f"{self.name} working")

class Centaur(Human, Animals):
    def mythology(self):
        print(f'A {self.name} in mythology')
centaur = Centaur('Iksion', 48)

centaur.eat()
centaur.sleep()
centaur.study()
centaur.mythology()

# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
#   a.
#       class Person:
#           """
#           Make the class with composition.
#           """
#       class Arm:
#           """
#           Make the class with composition.
#           """
class Person:
    def __init__(self):
        arm1 = Arm('Left arm shows')
        arm2 = Arm('Right arm give')
        self.arms = [arm1, arm2]
class Arm:
    def __init__(self, act):
        self.act = act
person = Person()
for arm in person.arms:
    print(arm.act)

#   b.
#       class CellPhone:
#           """
#           Make the class with aggregation
#           """
#       class Screen:
#           """
#           Make the class with aggregation
#           """

class CellPhone:
    def __init__(self, screen):
        self.screen = screen

class Screen:
    def __init__(self, type_display):
        self.type_display = type_display

screen = Screen('LCD')
cell_phone = CellPhone(Screen)
print(screen.type_display)

# 3. class Profile:
#     """
#     Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
#     Override a printable string representation of Profile class and return: list of the params mentioned above
#     """

class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.parameters = [name, last_name, phone_number, address, email, birthday, age, sex]
    def __str__(self):
        return str(self.parameters)

person1 = Profile('Ann', 'Zapototska', '380996326203', 'Lviv', 'cursor@gmail.com', '12.11.1998', '22', 'female')
print(person1)

# 4.* Create an interface for the Laptop with the next methods: Screen,
# Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import abstractmethod, ABC

class Laptop(ABC):

    @abstractmethod
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError

class My_Laptop(Laptop):
    def __init__(self, name, screen_type, keyboard_type, touchpad_type, webcam_type, ports_type, dynamics_type):
        self.name = name
        self.screen_type = screen_type
        self.keyboard_type = keyboard_type
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.ports_type = ports_type
        self.dynamics_type = dynamics_type

    def name(self):
        print(f'Laptop model is {self.name}')

    def screen(self):
        print(f'Screen: {self.screen_type}')

    def keyboard(self):
        print(f'Keyboard: {self.keyboard_type}')

    def touchpad(self):
        print(f'Toucpad: {self.touchpad_type}')

    def webcam(self):
        print(f'WebCam: {self.webcam_type}')

    def ports(self):
        print(f'Ports type: {self.ports_type}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_type}')

laptop = My_Laptop("Acer", "IPS", "EN", 'Yes', "Yes", "2x USB 3.1 Gen. 1 (USB 3.0), HDMI", 'Yes')


laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()
