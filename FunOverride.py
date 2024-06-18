class Parent:
    def disp(self):
        print("This is parent")
class Child(Parent):
    def disp(self):
        print("This is child")
c=Child()
c.disp()