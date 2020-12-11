import turtle
import requests
from bs4 import BeautifulSoup


def webs(x):
    res = requests.get(url="https://es.wikipedia.org/wiki/Pong", )
    soup = BeautifulSoup(res.content, 'html.parser')
    text = soup.get_text()
    div = [line for line in text.split("\n") if line != ""]

    ntext = []

    for i in range(len(div)):
        a = div[i]
        if "Juego[editar]" == a:
            ntext = div[i + 1]
            ntext = ntext[:-4]

    ntext = ntext.split()
    va = list(map(str, ntext))
    va.append("-1")

    b = 40
    n = 0
    lin = []
    ont = 0
    m = []

    for i in range(len(va)):
        d = va[i] + " "
        c = len(d)
        n = c + n

        if d == "-1 ":
            if lin:
                e = "".join(map(str, lin)).strip(" ")
                m.append(e)
                lin = []
                ont = ont + 1

        elif (n + len(va[i + 1]) + 1) > b + 1:
            lin.append(d)
            n = 0
            e = "".join(map(str, lin)).strip(" ")
            m.append(e)
            lin = []
            ont = ont + 1
        else:
            lin.append(d)
    txt = turtle.Turtle()

    if x == 1:
        txt.speed(0)
        txt.color("white")
        txt.penup()
        txt.hideturtle()
        xpos = 200
        for i in range(ont):
            xpos -= 25
            txt.goto(0, xpos)
            txt.write(m[i], align="center", font=("System", 20, "normal"))
    elif x == 0:
        global vent
        vent.clear()
        print("ok")
        pm()


vent = turtle.Screen()
vent.title("PONG")
vent.bgcolor("black")
vent.setup(width=650, height=650)
vent.tracer(0)
cont = 0
dir1 = 0


def pm():
    global vent
    vent.title("PONG")
    vent.bgcolor("black")
    vent.setup(width=650, height=650)
    vent.tracer(0)

    est = turtle.Turtle()
    est.speed(0)
    est.shape("square")
    est.color("white")
    est.penup()
    est.goto(0, 0)
    est.shapesize(stretch_wid=1, stretch_len=1)

    pun = turtle.Turtle()
    pun.speed(0)
    pun.color("white")
    pun.penup()
    pun.hideturtle()
    pun.goto(0, 270)
    pun.write("Pong", align="center", font=("System", 40, "normal"))
    pun.goto(0, 140)
    pun.write("Mover cursor con", align="center", font=("System", 20, "normal"))
    pun.goto(0, 100)
    pun.write("←      →", align="center", font=("System", 40, "normal"))
    pun.goto(0, -80)
    pun.write("Y seleccionar con ENTER", align="center", font=("System", 20, "normal"))
    pun.goto(0, -140)
    pun.write("Como demo, solo funciona el simbolo de info", align="center", font=("System", 10, "normal"))
    pun.goto(280, -300)
    pun.write("ⓘ", align="center", font=("System", 40, "normal"))

    but = [(0, 0), (279, -230)]

    def izq():
        global cont
        cont -= 1
        if cont == -1:
            cont = 1
        est.goto(but[cont])

    def der():
        global cont
        cont += 1
        if cont == 2:
            cont = 0
        est.goto(but[cont])

    def ent():
        if est.xcor() == 279:
            global vent
            pun.clear()
            global dir1
            global cont
            dir1 += 1
            if dir1 == 2:
                dir1 = 0
            print(dir1)
            webs(dir1)
            cont = 0

    vent.listen()
    vent.onkeypress(der, "Right")
    vent.onkeypress(izq, "Left")
    vent.onkeypress(ent, "Return")

    while True:
        vent.update()


def solo():
    est = turtle.Turtle()
    est.speed(0)
    est.shape("square")
    est.color("white")
    est.penup()
    est.goto(0, 0)
    est.shapesize(stretch_wid=1, stretch_len=1)

    est2 = turtle.Turtle()
    est2.speed(0)
    est2.shape("square")
    est2.color("black")
    est2.penup()
    est2.goto(0, 0)
    est2.shapesize(stretch_wid=1, stretch_len=1)

    p1 = turtle.Turtle()
    p1.speed(0)
    p1.shape("square")
    p1.color("red")
    p1.penup()
    p1.goto(-290, 0)
    p1.dy = 5
    p1.shapesize(stretch_wid=5, stretch_len=1)

    p2 = turtle.Turtle()
    p2.speed(0)
    p2.shape("square")
    p2.color("cyan")
    p2.penup()
    p2.goto(290, 0)
    p2.shapesize(stretch_wid=5, stretch_len=1)

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color(1, 1, 1)
    ball.penup()
    ball.goto(0, 0)
    vel = 0.3
    ball.dx = vel
    ball.dy = vel

    conta = 0
    contb = 0

    pun = turtle.Turtle()
    pun.speed(0)
    pun.color("grey")
    pun.penup()
    pun.hideturtle()
    pun.goto(0, 150)
    pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

    def up1():
        """
        :return: hace que la paleta del jugador 1 se mueva coor unidades hacia arriba
        """
        if p1.ycor() >= 240:
            p1.dy = 0
            p1.sety(p1.ycor() + p1.dy)
        else:
            p1.dy = 20
            p1.sety(p1.ycor() + p1.dy)

    def up2():
        """
        :return: hace que la paleta del jugador 2 se mueva coor unidades hacia arriba
        """
        coor = p2.ycor()
        coor = coor + 20
        p2.sety(coor)

    def down1():
        """
            :return: hace que la paleta del jugador 1 se mueva coor unidades hacia abajo
            """
        if p1.ycor() <= -240:
            p1.dy = 0
            p1.sety(p1.ycor() + p1.dy)
        else:
            p1.dy = -20
            p1.sety(p1.ycor() + p1.dy)

    def down2():
        """
            :return: hace que la paleta del jugador 2 se mueva coor unidades hacia abajo
            """
        coor = p2.ycor()
        coor = coor - 20
        p2.sety(coor)

    vent.listen()
    vent.onkeypress(up1, "w")
    vent.onkeypress(up2, "Up")
    vent.onkeypress(down1, "s")
    vent.onkeypress(down2, "Down")

    while True:
        vent.update()

        ball.setx(ball.xcor() + ball.dx)

        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 300:
            ball.dy = ball.dy * (-1)

        elif ball.ycor() < -300:
            ball.dy = ball.dy * (-1)

        elif ball.xcor() >= 290:
            ball.goto(0, 0)
            ball.dx = ball.dx * (-1)
            conta = conta + 1
            pun.clear()
            pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

        elif ball.xcor() <= -290:
            ball.goto(0, 0)
            ball.dx = ball.dx * (-1)
            contb = contb + 1
            pun.clear()
            pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

        if ((280 < ball.xcor() + 5)
                and (p2.ycor() + 50 > ball.ycor() > p2.ycor() - 50)):
            ball.dx = ball.dx * (-1)

        elif (-280 > ball.xcor() - 5) and (p1.ycor() + 50 > ball.ycor() > p1.ycor() - 50):
            ball.dx = ball.dx * -1

        if contb == 10 or conta == 10:
            vent.clear()
            pm()
            break


pm()
