#第一版 原始
import turtle 
turtle.setup(width=600,height=400,startx=200,starty=200)

def ball():
    turtle.hideturtle()
    #turtle.speed(0)
    turtle.color("red","pink")  
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-270,0)
    for i in range(56):      
        #底下開始隱藏作畫過程
        turtle.tracer(False)
        turtle.clear() 
        turtle.pendown() 
        turtle.begin_fill()
        turtle.circle(20,360,200)  
        turtle.end_fill() 
        turtle.update()   #更新畫面
    #底下開始顯示以上的繪圖結果，n為更新畫面次數，delay為延遲ms。
        turtle.tracer(n=1,delay=50) 
        turtle.penup()     
        turtle.forward(9.8)
        
    b=str(1)
    return b

while(True):
    a=ball()
    print('碰到牆了'+a[0])
    if a[0]=='1':
        turtle.hideturtle()
        #turtle.speed(0)
        turtle.color("red","pink")  
        turtle.pensize(2)
        turtle.penup()
        turtle.goto(270,0)
        for i in range(56):
            #底下開始隱藏作畫過程
            turtle.tracer(False)
            turtle.clear() 
            turtle.pendown() 
            turtle.begin_fill()
            turtle.circle(20,360,200)  
            turtle.end_fill() 
            turtle.update()   #更新畫面
        #底下開始顯示以上的繪圖結果，n為更新畫面次數，delay為延遲ms。
            turtle.tracer(n=1,delay=50) 
            turtle.penup()     
            turtle.backward(9.9)
        
turtle.mainloop()
