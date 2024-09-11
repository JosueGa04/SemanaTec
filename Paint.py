from turtle import *
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Bucle para dibujar los cuatro lados del cuadrado
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()



def draw_circle(start, end):
    """Draw circle from start to end."""
    # Calcula el radio del círculo basado en la distancia entre los puntos
    radius = abs(end - start) / 2
    up()
    goto(start.x, start.y - radius)  # Move to the bottom of the circle
    down()
    begin_fill()
    circle(radius) # Dibuja el círculo usando el radio calculado
    end_fill()

def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Dibuja el rectángulo considerando la longitud y el ancho
    for count in range(2):
        forward(end.x - start.x)  # Longitud
        left(90)
        forward(end.y - start.y)  # Ancho
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Dibuja el triángulo equilátero
    for count in range(3):
        forward(end.x - start.x)  # Longitud del lado
        left(120)  # Ángulo de 120 grados para un triángulo equilátero

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']  # Obtiene la figura seleccionada del estado
        end = vector(x, y)
        shape(start, end)
        state['start'] = None # Resetea el punto de inicio para el siguiente dibujo


def store(key, value):
    """Store value in state at key."""
    # Asigna el valor a la clave correspondiente en el diccionario de estado
    state[key] = value

# Inicializa el estado del programa con el punto de inicio vacío y la figura predeterminada como una línea
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

# Asigna teclas para cambiar el color de dibujo
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')  # Added new color (yellow)

# Asigna teclas para cambiar la figura de dibujo
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
