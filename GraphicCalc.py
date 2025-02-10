import turtle
import math

import os

def czytaj(A):
    n = int(input("Stopien wielomianu: "))
    A.clear()  # Czyszczenie listy
    for i in range(n, -1, -1):
        A.append(float(input("a{}=".format(i))))

def Wiel(A, x):
    y = 0
    n = len(A) - 1
    for i in range(0, n + 1):
        y += A[i] * math.pow(x, n)
        n -= 1
    return y

def RysWiel(A, scale_x, scale_y):
    turtle.penup()
    for i in range(-300, 301):
        x = i / scale_x
        y = Wiel(A, x) * scale_y
        if -300 < y < 300:
            turtle.goto(i, y)
            turtle.pendown()

def RysHomo(A, b, scale_x, scale_y):
    turtle.penup()
    for i in range(-300, 301):
        x = i / scale_x
        if Wiel(A, x) != 0:
            y = b / Wiel(A, x) * scale_y
            if -300 < y < 300:
                turtle.goto(i, y)
                turtle.pendown()
        else:
            turtle.penup()

def Sqr(A, b, scale_x, scale_y):
    turtle.penup()
    for i in range(0, 301):
        if i != 0:
            x = i * scale_x
            y = b * math.sqrt(Wiel(A, x)) * scale_y
            if -300 < y < 300:
                turtle.goto(i, y)
                turtle.pendown()
        else:
            turtle.penup()

def Square(x, y, d):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x + d, y)
    turtle.goto(x + d, y + d)
    turtle.goto(x, y + d)
    turtle.goto(x, y)

def BG():
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.tracer(0)
    turtle.penup()
    turtle.pensize(5)
    Square(-300, -300, 600)
    
    turtle.penup()
    turtle.pensize(2)
    turtle.setpos(-300, 0)
    turtle.pendown()
    turtle.setpos(300, 0)
    
    turtle.penup()
    turtle.pensize(2)
    turtle.setpos(0, 300)
    turtle.pendown()
    turtle.setpos(0, -300)


scale_x = 10  # Skalowanie osi x
scale_y = 5 # Skalowanie osi y

BG()
turtle.hideturtle()
turtle.pensize(1)
turtle.tracer(1)



while True:
    print("Wybierz funkcje: ")
    print("1. Wielomianowa")
    print("2. Homograficzna")
    print("3. Pierwiastkowa")
    print("4. Wyjscie")

    choice = int(input())
    turtle.color("red")
    if choice == 1:
        A = []
        czytaj(A)
        RysWiel(A, scale_x, scale_y)
    elif choice == 2:
        A = []
        print("Wpisz wielomian mianownika: ")
        czytaj(A)
        RysHomo(A, 1, scale_x, scale_y)
    elif choice == 3:
        A = []
        print("Wpisz wielomian pod pierwiastkiem: ")
        czytaj(A)
        Sqr(A, 1, scale_x, scale_y)
    elif choice == 4:
        break
    os.system('cls')

    
turtle.mainloop()





#L = [3, 4]
#Q = [2, 5, -30]
#T = [-2, 2, 3, 50]
#H = [1/20, 0]
#S = [3, 20]

#turtle.color("red")
#RysWiel(L, scale_x, scale_y)
#
#turtle.color("sky blue")
#RysWiel(Q, scale_x, scale_y)
#
#turtle.color("magenta")
#RysWiel(T, scale_x, scale_y)
#
#turtle.color("light green")
#RysHomo(H, 20, scale_x, scale_y)
#
#turtle.color("white")
#Sqr(S, 1, scale_x, scale_y)

#