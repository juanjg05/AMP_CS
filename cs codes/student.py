class Student:
    def __init__(self, name, cs_level, num_theory, floor_number):
        self.name = name
        self.cs_level = cs_level
        self.num_theory = num_theory
        self.floor = floor_number
    def __str__(self):
        return self.name
    def get_floor(self):
        return self.floor
    
    def relocate(self, new_floor):
        self.floor = new_floor
        print(f'{self.name} has been relocated to {self.floor}')

if __name__ == "__main__":
    margarita = Student('Margarita', 2,'rainbow', 6)
    print(margarita.relocate(1))

