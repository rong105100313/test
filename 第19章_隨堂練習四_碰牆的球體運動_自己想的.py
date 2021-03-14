# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:09:41 2020

@author: GameToGo
"""

import turtle 
turtle.setup(width=600,height=400,startx=200,starty=200)


def turtle2():
    turtle.hideturtle()
    #turtle.speed(0)
    turtle.color("red","pink")  
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-280,0)
    x=2
    right=True
    while(True):      
        #底下開始隱藏作畫過程
        turtle.tracer(False)
        turtle.clear() 
        turtle.pendown() 
        turtle.begin_fill()
        turtle.circle(20,360,200)  
        turtle.end_fill() 
        turtle.update()   #更新畫面
    #底下開始顯示以上的繪圖結果，n為更新畫面次數，delay為延遲ms。
        turtle.tracer(n=1,delay=2) 
        turtle.penup()     
        turtle.forward(x)
        
        if turtle.xcor() >= 280 and right==True:
            x=-2
            right=False
        if turtle.xcor() <= -280 and right==False:
            x=2
            right=True
    
turtle.setup(width=600,height=400,startx=200,starty=200)
turtle2()
turtle.mainloop()
