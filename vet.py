class Vet:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age 
        self.salary = salary
        
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
        
vet = Vet(name="Sushi", age=21, salary=300000)   
print(vet)
