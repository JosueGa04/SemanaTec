from random import randrange, choice
from turtle import *
from freegames import square, vector

# Inicialización de la comida, serpiente y dirección
food = vector(0, 0)  # Posición inicial de la comida
snake = [vector(10, 0)]  # Posición inicial de la serpiente
aim = vector(0, -10)  # Dirección inicial de movimiento de la serpiente
speed = 100  # Velocidad de movimiento de la serpiente

# Colores disponibles (sin incluir el rojo)
colors = ['blue', 'yellow', 'purple', 'orange', 'pink']

# Asignación de colores diferentes entre sí
snake_color = choice(colors)  # Color aleatorio para la serpiente
food_color = choice([color for color in colors if color != snake_color])  # Color aleatorio para la comida, diferente al de la serpiente

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
    head = snake[-1].copy()  # Crea una copia de la cabeza de la serpiente
    head.move(aim)  # Mueve la cabeza en la dirección actual

    if not inside(head) or head in snake:
        # La serpiente muere si se sale del área de juego o se choca a sí misma
        square(head.x, head.y, 9, 'red')  # Dibuja un cuadrado rojo en la posición de la cabeza
        update()
        return

    snake.append(head)  # Agrega la nueva cabeza a la serpiente

    if head == food:
        # Si la cabeza de la serpiente alcanza la comida
        print('Snake:', len(snake))  # Imprime la longitud de la serpiente
        food.x = randrange(-15, 15) * 10  # Reubica la comida en una nueva posición aleatoria
        food.y = randrange(-15, 15) * 10
        speed = max(10, speed - 5)  # Aumenta la velocidad de la serpiente al comer
    else:
        snake.pop(0)  # Elimina el segmento más antiguo de la serpiente si no ha comido

    clear()  # Limpia la pantalla para redibujar

    # Dibuja la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibuja la comida
    square(food.x, food.y, 9, food_color)
    update()  # Actualiza la pantalla
    ontimer(move, speed)  # Llama a la función move nuevamente después de un intervalo de tiempo

def move_food():
    """Mueve la comida de forma aleatoria un paso sin salirse de la ventana."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]  # Posibles direcciones de movimiento para la comida
    move_direction = choice(directions)  # Elige una dirección aleatoria
    new_position = food + move_direction  # Calcula la nueva posición de la comida

    if inside(new_position):
        # Mueve la comida si la nueva posición está dentro de los límites
        food.move(move_direction)

    ontimer(move_food, 500)  # Vuelve a mover la comida cada 500ms

# Configuración de la ventana y controles
setup(420, 420, 370, 0)  # Configura el tamaño de la ventana y su posición
hideturtle()  # Oculta el cursor de la tortuga
tracer(False)  # Desactiva el trazado automático para mejorar el rendimiento
listen()  # Escucha eventos de teclado
onkey(lambda: change(10, 0), 'Right')  # Cambia la dirección a la derecha cuando se presiona la tecla 'Right'
onkey(lambda: change(-10, 0), 'Left')  # Cambia la dirección a la izquierda cuando se presiona la tecla 'Left'
onkey(lambda: change(0, 10), 'Up')  # Cambia la dirección hacia arriba cuando se presiona la tecla 'Up'
onkey(lambda: change(0, -10), 'Down')  # Cambia la dirección hacia abajo cuando se presiona la tecla 'Down'

# Inicia el movimiento
move()  # Comienza el movimiento de la serpiente
move_food()  # Inicia el movimiento aleatorio de la comida
done()  # Finaliza la configuración y entra en el bucle principal de eventos

