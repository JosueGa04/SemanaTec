from random import randrange, choice
from turtle import *
from freegames import square, vector

# Inicialización de la comida, serpiente y dirección
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = 100

# Colores disponibles (sin incluir el rojo)
colors = ['blue', 'yellow', 'purple', 'orange', 'pink']

# Asignación de colores diferentes entre sí
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])


def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Devuelve True si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mueve la serpiente un segmento hacia adelante."""
    global speed  # Acceso a la variable global para modificar la velocidad
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # La serpiente muere
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        speed = max(10, speed - 5)  # Aumenta la velocidad al comer
    else:
        snake.pop(0)

    clear()

    # Dibuja la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibuja la comida
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, speed)


def move_food():
    """Mueve la comida de forma aleatoria un paso sin salirse de la ventana."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_direction = choice(directions)
    new_position = food + move_direction

    if inside(new_position):
        food.move(move_direction)

    ontimer(move_food, 500)  # Vuelve a mover la comida cada 500ms


# Configuración de la ventana y controles
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Inicia el movimiento
move()
move_food()  # Inicia el movimiento aleatorio de la comida
done()
