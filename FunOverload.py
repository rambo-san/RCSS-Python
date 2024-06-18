def product(a, b):
    p = a * b
    print(p)
def product(a, b, c):
    p = a * b * c
    print(p)
# product(1,2)

product(1,2,3)

class Poly:
    def __init__(self) -> None:
        print("No argument")
    def disp(self,name):
        print(name)
    def disp(self,name,number):
        print(name,number)
    def disp(self,name,number,age):
        print(name,number,age)
p=Poly()
p.disp("Abhi")
p.disp("Abhi","12345")
p.disp("Abhi","12345",23)