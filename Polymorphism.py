class dog:
    def speak(self):
        print("Bark")
class cat:
    def speak(self):
        print("Meow")
class cow:
    def speak(self):
        print("Mooo")
d=dog()
c=cat()
co=cow()

animals=[d,c,co]

for animal in animals:
    animal.speak()