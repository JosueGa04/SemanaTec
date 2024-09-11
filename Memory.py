from random import *
from turtle import *

from freegames import path

# Carga la imagen del coche desde los recursos de freegames
car = path('car.gif')
# Crea una lista de números del 0 al 31, duplicados para que haya pares (64 elementos en total)
tiles = list(range(32)) * 2
# Estado del juego, guarda la marca seleccionada actualmente (None al inicio)
state = {'mark': None}
# Lista booleana que indica si cada cuadro está oculto (64 elementos, todos inicialmente True)
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    # Calcula el índice basado en las coordenadas (x, y). La cuadrícula tiene 8 cuadros por fila,
    # así que se usa esta fórmula para convertir las coordenadas en un índice de 0 a 63.
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # Convierte un número de cuadro (de 0 a 63) en coordenadas (x, y)
    # Modifica el valor para que encaje en la cuadrícula de 8x8 (50 píxeles por cuadro)
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


taps = 0 # Contador de taps

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps # Permite modificar la variable global 'taps'
    spot = index(x, y) # Convierte las coordenadas del clic en un índice de cuadro
    mark = state['mark']
    taps += 1 #Aumenta el contador de taps

    # Si no hay ninguna marca seleccionada, si se hace clic en el mismo lugar, o si los cuadros no coinciden
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False  # Revela el cuadro actual
        hide[mark] = False  # Revela el cuadro anterior
        state['mark'] = None  # Resetea la marca

def all_revealed():
    """Return True if all tiles are revealed."""
    # Verifica si todos los cuadros de la lista 'hide' están en False (es decir, todos están revelados)
    return all(not hidden for hidden in hide)

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Itera sobre los 64 cuadros (8x8) de la cuadrícula
    for count in range(64):
        if hide[count]:  # Si el cuadro está oculto
            x, y = xy(count)  # Obtiene las coordenadas del cuadro
            square(x, y)  # Dibuja un cuadro en esas coordenadas  
    
    mark = state['mark']  
        
    #Dibujar los emojis en el cuadro marcado
    images = ['🐶', '🐱', '🦁', '🐸', '🐰', '🐼', '🐨', '🐻', '🦊', '🐯', '🐮', '🐷', '🐵', '🐔', '🐧', '🐦', '🐙', '🦄', '🐢',
              '🦕', '🐍', '🦉', '🦅', '🐞', '🐝', '🦋', '🐠', '🦑', '🐬', '🐋', '🦓', '🦒']

    # Si hay un cuadro marcado y aún está oculto
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 5)
        color('black')
        # Escribe el emoji correspondiente al cuadro marcado en el centro del cuadro
        write(images[tiles[mark] % len(images)], align='center', font=('Arial', 30, 'normal'))

    #Mostrar numero de taps
    up()
    goto(0, -250)
    write(f"Taps: {taps}", align='center', font=('Arial', 20, 'normal'))

    # Si todos los cuadros están revelados
    if all_revealed():
        goto(0, 0)
	# Muestra el mensaje "¡Ganaste!"
        write("¡Ganaste!", align='center', font=('Arial', 40, 'bold'))
    else:
        update()  # Actualiza la pantalla
        ontimer(draw, 100)  # Repite la función draw cada 100 milisegundos   
    
# Baraja los cuadros antes de comenzar el juego
shuffle(tiles) #Funcion que acomoda los cuadros
setup(420, 420, 370, 0) 
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()   
done()
