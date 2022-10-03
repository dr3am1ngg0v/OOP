from abc import *
from itertools import count

class Figure(metaclass = ABCMeta):
    f_number = 0
    
    def __init__(self):
        Figure.f_number += 1
        self.order = Figure.f_number
    
    def __str__(self):
        pass

    def show(self):
        self.out = self.__str__()
        self.out += str(round(self.area(), 3))
        while len(self.out) < 22: 
            self.out += ' '
        self.out += '|' + str(round(self.perimeter(), 3))
        while len(self.out) < 31: 
            self.out += ' '
        self.out += '|' + str(self.order)
        print(self.out)

    def perimeter(self):
        pass

    def area(self):
        pass
    
class Point():
    def __init__(self):
        import math
        self.Point_list = []
        self.Uni = 120
        if N > 3:
           self.Uni = 65
        n = 0 
        if COORD_SYST == 'pol':
            self.ro = int(input('Введите радиус вектор точки:   '))
            self.fi = int(input('Угол фи = pi*'))
            self.coord1 = self.ro*math.cos(self.fi*math.pi)
            self.coord2 = self.ro*math.sin(self.fi*math.pi)
            self.Point_list.append(self.coord1)
            self.Point_list.append(self.coord2)
            n = 2         
        for i in range(n, N):
            self.coord = int(input('Введите {0}:\n'.format(chr(i+self.Uni))))
            self.Point_list.append(self.coord)

    @staticmethod
    def distance_calculate(point_1, point_2):   #Вычисление расстояния между точками
        import math
        a = 0
        for i in range(N):
            a += (point_1.Point_list[i] - point_2.Point_list[i])**2
        return math.sqrt(a) 
        
            
class Triangle(Figure):

    def __init__(self):
        Figure.__init__(self)
        print('Введите координаты для вершин тругольника\n  Первая вершина:')
        self.p1 = Point()
        print(' Вторая вершина:')
        self.p2 = Point()
        print(' Третья вершина:')
        self.p3 = Point()
        self.side_1 = Point.distance_calculate(self.p1, self.p2) 
        self.side_2 = Point.distance_calculate(self.p2, self.p3)
        self.side_3 = Point.distance_calculate(self.p1, self.p3)

    def show(self):
        Figure.show(self)
        
    def perimeter(self):
        Figure.perimeter(self)
        self.per = (self.side_1 + self.side_2 + self.side_3)
        return(self.per)

    def area(self):
        Figure.area(self)
        import math
        self.p_half = self.perimeter()/2
        self.t_area = math.sqrt(self.p_half*(self.p_half-self.side_1)*(self.p_half-self.side_2)*(self.p_half-self.side_3))
        return(self.t_area)

    def __str__(self):
        Figure.__str__(self)
        return '| треугольник |'

class Circle(Figure):

    def __init__(self):
        Figure.__init__(self)
        print('Введите координаты для центра окружности и точки на окружности\n Центр:')
        self.o = Point()
        print(' Точка на окружности:')
        self.p = Point()
        self.r = Point.distance_calculate(self.o, self.p)

    def show(self):
        Figure.show(self)

    def perimeter(self):
        Figure.perimeter(self)
        import math
        self.per = math.pi*2*self.r
        return(self.per)

    def area(self):
        Figure.area(self)
        import math
        self.c_area = math.pi*self.r**2
        return(self.c_area)

    def __str__(self):
        Figure.__str__(self)
        return '| окружность  |'

class Rectangle(Figure):

    def __init__(self):
        Figure.__init__(self)
        import math
        print('Введите координаты 4 вершин по порядку\n    Первая вершина:')
        self.p1 = Point()
        print(' Вторая вершина:')
        self.p2 = Point()
        print(' Третья вершина:')
        self.p3 = Point()
        print(' Четвёртая вершина:')
        self.p4 = Point()
        self.side_1 = Point.distance_calculate(self.p1, self.p2) 
        self.side_2 = Point.distance_calculate(self.p2, self.p3)
        self.side_3 = Point.distance_calculate(self.p3, self.p4)
        self.side_4 = Point.distance_calculate(self.p1, self.p4)

    def show(self):
        Figure.show(self)

    def perimeter(self):
        Figure.perimeter(self)
        import math
        self.per = (self.side_1 + self.side_2 + self.side_3 + self.side_4)
        return(self.per)

    def area(self):
        Figure.area(self)
        import math
        self.p_half = self.perimeter()/2
        self.r_area = math.sqrt((self.p_half-self.side_1)*(self.p_half-self.side_2)*(self.p_half-self.side_3)*(self.p_half-self.side_3))
        return(self.r_area)

    def __str__(self):
        Figure.__str__(self)
        return '|четырёхуг-ник|'

Figures_list = []
N = int(input('Введите размерность пространства(число):    '))
COORD_SYST = input('Введите pol или dec для выбора СК(полярные/декартовы): ')
f_quantity = int(input('Введите необходимое количество фигур:    '))

for some_figure in range(f_quantity):
    figure_type = input('   Какую фигуру создать? Введите:\n\
T для создания треугольника\nC для создания окружности\nR для создания четырёхугольника\n')

    if figure_type == 'T':
        some_figure = Triangle()
        Figures_list.append(some_figure)

    elif figure_type == 'C':
        some_figure = Circle()
        Figures_list.append(some_figure)

    elif figure_type == 'R':
        some_figure = Rectangle()
        Figures_list.append(some_figure)

def sorting(F):
    return F.area()

Figures_list.sort(key=sorting)
print('__________________________________\n| тип фигуры  |Площадь|Периметр|№')
for i in Figures_list:         
    i.show()                    
print('----------------------------------')
