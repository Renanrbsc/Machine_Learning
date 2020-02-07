from turtle import *
import time

speed(0)
colormode(255)
clrs =["MidnightBlue", "Navy", "DarkBlue", "MediumBlue", "RoyalBlue", "MediumSlateBlue", "CornflowerBlue", "DodgerBlue", "DeepskyBlue", "LightSkyBlue", "SkyBlue", "LightBlue" ]

time.sleep(2) # tempo para iniciar

for j in range(120): # total da circunferencia

   
    cn=0
    c=30
    f=70
    
    for i in range(12): # quantidade de circulos por raio

        pencolor(clrs[cn])
        circle(c)
        left(90)
        penup()
        forward(f)
        right(90)
        pendown()
        c = c*0.8
        f = f*0.8
        circle(c)
        cn = cn+1
        
        

    penup()
    goto(0,0)
    forward(5)
    right(3)
    pendown()

    
exitonclick()