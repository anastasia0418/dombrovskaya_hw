# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, x1 = -3, y1 = -2, x2 = 0, y2 = 2, x3 = 3, y3 = -2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def square(self):
        return abs(0.5*((self.x2 - self.x1)*(self.y3 - self.y1) - (self.x3 - self.x1)*(self.y2 - self.y1)))

    def height(self):
        ab = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return abs(2 * self.square()/ab)

    def perimeter(self):
        ab = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        bc = math.sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)
        ac = math.sqrt((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)
        return ab + bc + ac


triang1 = Triangle()
print(triang1.square())
print(triang1.height())
print(triang1.perimeter())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, x1=-4, y1=-4, x2=-3, y2=3, x3=3, y3=3, x4=4, y4=-4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def itIsTrapez(self):
        a = math.sqrt((self.x2 - self.x1)**2+(self.y2 - self.y1)**2)
        b = math.sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)
        c = math.sqrt((self.x4 - self.x3)**2 + (self.y4 - self.y3)**2)
        d = math.sqrt((self.x1 - self.x4)**2 + (self.y1 - self.y4)**2)
        ac = (self.x4 - self.x1)/d  # для проверки парралельности оснований
        bc = (self.x3 - self.x2)/b
        ab = (self.x2 - self.x1)/a
        cd = (self.x3 - self.x4)/c
        if (a == c) and (ac == bc) or (b == d) and (cd == ab) or (a == c) and (b == d):
            print('Это равнобочная трапеция!')
        else:
            print('Это не равнобочная трапеция!')

    def length(self):
        a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        c = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
        d = math.sqrt((self.x1 - self.x4) ** 2 + (self.y1 - self.y4) ** 2)
        return a, b, c, d

    def square(self):
        sq1 = 0.5*((self.x2 - self.x1)*(self.y4 - self.y1) - (self.x4 - self.x1)*(self.y2 - self.y1))
        sq2 = 0.5*((self.x2 - self.x3)*(self.y4 - self.y3) - (self.x4 - self.x3)*(self.y2 - self.y3))
        return abs(sq1 + sq2)

    def perimeter(self):
        return sum(self.length())

tr = Trapezium()
tr.itIsTrapez()
print(tr.length())
print(tr.perimeter())
print(tr.square())
