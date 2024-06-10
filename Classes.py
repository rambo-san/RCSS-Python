class First:
    college="RCSS"
    dot='Skill: '
    def __init__(self,name,skill) -> None:
        self.name=name
        self.skill=skill
    def disp(self,job):
        print(self.name+" "+job+" Studying in "+self.college)
        return self.dot
    def skill(self):
        return self.skill
rep1=First("Shiva","Sing")
print(rep1.disp("is the first Class Rep")+rep1.skill)
rep1=First("Revathi","dance")
print(rep1.disp("is the second Class Rep")+rep1.skill)
rep1=First("Gracen","Tongue")
print(rep1.disp("is the Placement Guy")+rep1.skill)