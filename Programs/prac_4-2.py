from abc import ABC, abstractmethod
from typing import List


class OrderItemVisitor(ABC):
    @abstractmethod
    def visit(self, item) -> float:
        ...

class ItemElement(ABC):
    @abstractmethod
    def accept(self, visitor: OrderItemVisitor) -> float:
        ...

class Cake(ItemElement):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)

class Coffee(ItemElement):
    def __init__(self, name: str,
                 price: float,
                 capacity: float):
        self.name = name
        self.price = price
        self.capacity = capacity

    def get_price(self) -> float:
        return self.price

    def get_capacity(self) -> float:
        return self.capacity

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)

class WithOutDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Cake):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost

class OnlyCakeDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Cake):
            cost = item.get_price()
            cost -= cost * 0.15                           #Скидка 15% на торт
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost

class OnlyCoffeeDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Cake):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
            cost -= cost * 0.35                           #Скидка 35% на кофе
        return cost

class AllDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Cake):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        cost -= cost * 0.40                               #Скидка 40% на все товары
        return cost

class Waiter:
    def __init__(self, discount: OrderItemVisitor):
        self.order: List[ItemElement] = []
        self.discount_calculator = discount

    def set_order(self, order: List[ItemElement]) -> None:
        self.order = order

    def set_discount(self, discount: OrderItemVisitor) -> None:
        self.discount_calculator = discount

    def calculate_finish_price(self) -> float:
        price = 0
        if self.order:
            for item in self.order:
                price += item.accept(self.discount_calculator)
        return price


order: List[ItemElement] = [Coffee("Эспрессо мал", 4, 0.3),
                            Coffee("Эспрессо бол", 5, 0.5),
                            Coffee("Латтэ бол", 4, 0.3),
                            Coffee("Латтэ бол", 5, 0.5),
                            Cake("Наполеон", 10.4),
                            Cake("Чизкейк", 11.3),
                            Cake("Прага", 15.2)]
discount = WithOutDiscountVisitor()
waiter = Waiter(discount)
waiter.set_order(order)

n=1
while n==1:
    print("Введите скидку: без скидки, на торт, на кофе, на всё")
    ch=input()
    while ch not in ("без скидки", "на торт", "на кофе", "на всё"):
        print("Повторите ввод")
        ch=input()

    if ch=="без скидки":
        discount = WithOutDiscountVisitor()
        waiter = Waiter(discount)
        waiter.set_order(order)
        print(f"Сумма заказа без учета скидок: "
              f"{round(waiter.calculate_finish_price(),2)}")

    elif ch=="на торт":
        discount = OnlyCakeDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на торт: "
              f"{round(waiter.calculate_finish_price(),2)}")

    elif ch=="на кофе":
        discount = OnlyCoffeeDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на кофе: "
              f"{round(waiter.calculate_finish_price(),2)}")

    elif ch=="на всё":
        discount = AllDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на всё: "
              f"{round(waiter.calculate_finish_price(),2)}")
    print("Хотите повторить? 1-Да")
    n = int(input())