class Grandpaa():
    def grand(self):
        print("Singer")

class Parent(Grandpaa):
    def parants(self):
        print("Dancer")

class Child(Parent):
    def childern(self):
        print("player")

kid=Child()
kid.grand()
kid.parants()
kid.childern()