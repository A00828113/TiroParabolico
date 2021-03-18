# Codigo de Juego de Tiro Parabólico
# Proósito: Seguir con una aplicación de juegos que maneja la física  como  inteligencia con un grado de
# dificultad aún mayor y requiere de cambios para hacer un juego más retador e interminable.
# Se agregaron las funcionalidades de: hacer el juego interminable; aumentar la velocidad de proyectil y targets
# Autores: Monserrat Da Costa Gomez y Abraham Cepeda
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# La función se llama tap
# parametro de entrada: x (int), y (int)
# parametro de salida: N/A (no regresa valores)
# Descripcion: Responde al tap en la pantalla y lanza el proyectil a la velocidad indicada (la cual fue modificada a la original)
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 550) / 25
        speed.y = (y + 550) / 25

# La función se llama inside
# parametro de entrada: xy (vector)
# parametro de salida: bool
# Descripcion: Revisa que el vector se encuentre dentro de los limites del programa
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# La función se llama draw
# parametro de entrada: N/A
# parametro de salida: N/A (no regresa valores)
# Descripcion: Genera las bolas azules y rojas
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# La función se llama move
# parametro de entrada: N/A
# parametro de salida: N/A 
# Descripcion: controla el movimiento de los targets y la pelota, los rangos de movimiento, velocidad, etc..
def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    
    # Indica cuanto se mueve en el eje x los targets (bolas azules)
    for target in targets:
        target.x -= 1.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            target.x += randrange(100, 200)

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()