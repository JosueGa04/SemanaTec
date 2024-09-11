from random import randrange
from turtle import *
from freegames import vector

# Inicialización de la bola y velocidad
ball = vector(-200, -200)  # Posición inicial de la bola
speed = vector(0, 0)  # Velocidad inicial de la bola
targets = []  # Lista para almacenar los objetivos

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        # Reubica la bola y establece la velocidad en función de la ubicación del toque
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10  # Aumentar la velocidad del proyectil en el eje x
        speed.y = (y + 200) / 10  # Aumentar la velocidad del proyectil en el eje y

def inside(xy):
    """Return True if xy within screen."""
    # Verifica si un vector está dentro de los límites de la pantalla
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw ball and targets."""
    clear()  # Limpia la pantalla

    # Dibuja los objetivos en la pantalla
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')  # Dibuja un objetivo azul

    # Dibuja la bola si está dentro de los límites
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  # Dibuja la bola roja

    update()  # Actualiza la pantalla

def move():
    """Move ball and targets."""
    # Agrega un nuevo objetivo con cierta probabilidad
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)  # Posición inicial del objetivo
        targets.append(target)

    # Mueve los objetivos hacia la izquierda
    for target in targets:
        target.x -= 2  # Aumentar la velocidad de los objetivos

    # Mueve la bola y ajusta la velocidad con la gravedad
    if inside(ball):
        speed.y -= 0.7  # Ajusta la gravedad del proyectil
        ball.move(speed)

    dupe = targets.copy()  # Copia de la lista de objetivos para evitar modificaciones durante la iteración
    targets.clear()  # Limpia la lista de objetivos

    # Mantiene los objetivos que están dentro de los límites de la pantalla
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()  # Dibuja la bola y los objetivos

    # Reposiciona los objetivos que han salido de la pantalla
    for target in targets:
        if not inside(target):
            target.x = 200  # Reposiciona el objetivo al borde derecho de la pantalla

    ontimer(move, 20)  # Llama a la función move nuevamente después de 20ms para hacer el juego más rápido

# Configuración de la ventana y controles
setup(420, 420, 370, 0)  # Configura el tamaño y la posición de la ventana
hideturtle()  # Oculta el cursor de la tortuga
up()  # Levanta el lápiz para no dibujar líneas mientras se mueve
tracer(False)  # Desactiva el trazado automático para mejorar el rendimiento
onscreenclick(tap)  # Asocia la función tap con clics en la pantalla
move()  # Inicia el movimiento de la bola y los objetivos
done()  # Finaliza la configuración y entra en el bucle principal de eventos
