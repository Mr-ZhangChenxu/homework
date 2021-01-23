class Animal:
    def __init__(self):
        self.name = 'Tom'
        self.color = 'blue'
        self.age = 10
        self.gender = 'male'

    def shout(self):
        # print('This animal could shout')
        print(f'{self.name} could shout')
        return self.name

    def run(self):
        print('This animal could run')

if __name__ == '__main__':
    cat = Animal()
    print(cat.name)
    print(cat.color)
    print(cat.shout())
