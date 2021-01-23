from animal import Animal


class Cat(Animal):
    def __init__(self):
        self.hair = 'short_hair'
        super().__init__()

    def catch_mouse(self):
        print(f'{self.name} could catch mouse')

    def shout(self):
        print(f'{self.name} 可以喵喵叫')

tom = Cat()
print(tom.hair)
print(tom.name)
print(tom.catch_mouse())
print(tom.shout())