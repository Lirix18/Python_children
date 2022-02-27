# Рисование квадратной спирали
import turtle
# sides = eval(input('Введите количество сторон от 2 до 10: '))
sides = 6
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'MintCream', 'Lavender', 'SteelBlue', 'pink']
turtle.bgcolor('black')
for x in range(360):
    turtle.pencolor(colors[x%sides])
    turtle.forward(x * 3 / sides + x)
    turtle.left(360 / sides + 1)
    turtle.width(x * sides // 200)
    turtle.left(90)