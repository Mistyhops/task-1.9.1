from completed_tasks.rectangle0 import Circle, Rectangle, Square

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print('Площадь прямоугольника:')
print(rect_1.getArea())
print(rect_2.getArea())

square_1 = Square(5)
square_2 = Square(10)

print('Площадь квадрата:')
print(square_1.squareArea(),
      square_2.squareArea())

circle_1 = Circle(4)
circle_2 = Circle(10)

print('Площадь круга:')
print(circle_1.getCircleSquare())


print('-'*15)
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print('Площадь квадрата:')
        print(figure.squareArea())
    elif isinstance(figure, Circle):
        print('Площадь круга:')
        print(figure.getCircleSquare())
    else:
        print('Площадь прямоугольника:')
        print(figure.getArea())

