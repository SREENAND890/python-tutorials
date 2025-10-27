class Bird:
    def sound(self):
        print("Bird makes a sound")


class Parrot(Bird):
    def sound(self):
        print("Parrot says 'Hello'")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")


def make_sound(bird):
    bird.sound()


parrot = Parrot()
sparrow = Sparrow()

make_sound(parrot)
make_sound(sparrow)
