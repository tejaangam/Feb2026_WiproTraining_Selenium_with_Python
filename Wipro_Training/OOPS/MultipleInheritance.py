
#multiple parents single child
class Father:
    def driving(self):
        print("Father has a skill to drive")

class Mother:
    def cook(self):
        print("Mother has a skill to cook")

class Child(Father, Mother):
    def bothskills(self):
        print("Child has a skill to study")
        print("Child has both skills of driving and cooking")

c = Child()
c.driving()
c.cook()
c.bothskills()