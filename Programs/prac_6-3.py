class Leaf:
    def __init__(self, number, *args):
        self.number = number
        self.position = args[0]

    def show(self):
        print("\t", end="")
        print(self.position)

    def showNum(self):
        print("\t", end="")
        print(self.number)

class Element:
    def __init__(self, number, *args):
        self.number = number
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def show(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.show()

    def showNum(self):
        print(self.number)
        for child in self.children:
            print("\t", end="")
            child.showNum()


if __name__ == "__main__":
    Hi = Element("A1", "Гильдлидер")
    Item1 = Element("B1", "Заместитель 1")
    Item2 = Element("B2", "Заместитель 2")
    Item11 = Leaf("C1", "Согильдиец 11")
    Item12 = Leaf("C2", "Согильдиец 12")
    Item21 = Leaf("C3", "Согильдиец 21")
    Item22 = Leaf("C4", "Согильдиец 22")
    Item1.add(Item11)
    Item1.add(Item12)
    Item2.add(Item21)
    Item2.add(Item22)

    Hi.add(Item1)
    Hi.add(Item2)
    Hi.show()
    print("Номера:")
    Hi.showNum()