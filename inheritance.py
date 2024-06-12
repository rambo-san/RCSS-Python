# class Teacher:
#     def __init__(self) -> None:
#         print("In Teacher")
# class Person:
#     def __init__(self) -> None:
#         print("in Person")

# class Student(Person,Teacher):
#     def __init__(self) -> None:
#         Person.__init__(self)
#         Teacher.__init__(self)
#         print("in Student")
# st=Student()

class Vehicle:
    def __init__(self,brand,model) -> None:
        self.model=model
        self.brand=brand

class Car(Vehicle):
    def __init__(self, brand, model,platenumber,color) -> None:
        super().__init__(brand, model)
        self.platenumber=platenumber
        self.color=color
    def disp(self):
        print("Brand : ",self.brand, self.model)
c=Car("Honda","Civic","KL03X1232","Red")
c.disp()