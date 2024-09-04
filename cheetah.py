class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age 
    
    def get_needs(self):
        return 60
        
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
        
cheetah = Cheetah(name="Lisa", age=5, gender="Female") 
print(cheetah)
print(cheetah.get_needs())