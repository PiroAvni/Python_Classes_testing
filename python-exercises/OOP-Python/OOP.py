class Dino:
    species = "archosaurs"

    def __init__(self, name, period):
        self.name = name
        self.period = period
        print('Dino Created')

    def __str__(self):
        return f"{self.name} is from the {self.period} period"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def update_period(self, new_period):
        self.period = new_period

    # Static Method
    @staticmethod
    def dinosarus_chillin():
        print("The dinosaurs are chillin")

    # Class Method
    @classmethod
    def printSpecies(cls):
        print("The species is:", cls.species)


Dino.printSpecies()


giganotosaurus = Dino("Steve", "Late Cretaceous")
allosaurus = Dino("James", "Late Jurassic")

# print(giganotosaurus.name, giganotosaurus.period)
# print(allosaurus.name, allosaurus.period)

# print(giganotosaurus)
# print(allosaurus)


print(giganotosaurus.speak('Rawwr'))

print(giganotosaurus.update_period('Triassic'))

print(giganotosaurus.period)



class Allosaurus(Dino):
    def __init__(self, nutrition):
        self.nutrition = nutrition
        
    def swin(self):
        return f"{self.name} is swimming"
    
    



