from turtle import*
color('black')
#tracer(1,0)
#ht()
busy = 0
up()
left(90)
forward(320)
left(90)
forward(384)
right(180)


def f8():
  global busy
  if busy == 0:
    busy = 1
    up()
    r = ycor()+10
    print(r)
    forward(5)
    down()
    forward(10)
    right(90)
    forward(20)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(180)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    busy = 0
    r = xcor()
    up()
    print(r)
    if xcor() > 365.0:
      goto(-384.0,ycor() -40)
    down()

def f1():
  global busy
  if busy == 0:
    busy = 1
    up()
    right(90)
    forward(20)
    left(90)
    forward(10)
    left(90)
    down()
    forward(20)
    up()
    right(90)
    busy = 0
    r = xcor()
    print(r)
    up()
    if xcor() > 365.0:
      goto(-384.0,ycor() -40)
    down()


    
def f0():
    global busy
    if busy == 0:
     busy = 1
     up()
     forward(5)
     down()
     forward(10)
     right(90)
     forward(20)
     right(90)
     forward(10)
     right(90)
     forward(20)
     right(90)
     forward(10)
     busy = 0
     r = xcor()
     print(r)
     up()
     if xcor() > 365.0:
      goto(-384.0,ycor() -40)
     down()
     
def f4():
    global busy
    if busy == 0:
     busy = 1
     up()
     forward(5)
     down()
     right(90)
     forward(10)
     left(90)
     forward(10)
     right(90)
     forward(10)
     left(180)
     forward(20)
     busy = 0
     right(90)
     r = xcor()
     print(r)
     up()
     if xcor() > 365.0:
      goto(-384.0,ycor() -40)
     down()
    

    

def f7():
    global busy
    if busy == 0:
     busy = 1
     up()
     forward(5)
     down()
     forward(10)
     right(90)
     forward(20)
     right(180)
     forward(20)
     busy = 0
     right(90)
     r = xcor()
     print(r)
     up()
     if xcor() > 365.0:
      goto(-384.0,ycor() -40)
     down()


def f2():
    global busy
    if busy == 0:
     busy = 1
     up()
     forward(5)
     down()
     forward(10)
     right(90)
     forward(10)
     right(90)
     forward(10)
     left(90)
     forward(10)
     left(90)
     forward(10)
     left(90)
     up()
     forward(20)
     right(90)
     busy = 0
     r = xcor()
     print(r)
     up()
     if xcor() > 365.0:
      goto(-384.0,ycor() -40)
     down()



def f5():
    global busy
    if busy == 0:
     busy = 1
     up()
     forward(5)
     down()
     forward(10)
     right(180)
     forward(10)
     left(90)
     forward(10)
     left(90)
     forward(10)
     right(90)
     forward(10)
     right(90)
     forward(10)
     right(90)
     up()
     forward(20)
     right(90)
     forward(10)
     busy = 0
     r = xcor()
     print(r)
     up()
     if xcor() > 365.0:
      goto(-384.0,ycor() -40)
     down()
    






def f3():
    global busy
    if busy == 0:
     busy = 1
     up()
     forward(5)
     down()
     forward(10)
     right(90)
     forward(10)
     right(90)
     forward(10)
     right(180)
     forward(10)
     right(90)
     forward(10)
     right(90)
     forward(10)
     right(180)
     forward(10)
     left(90)
     forward(20)
     right(90)
     busy = 0
     r = xcor()
     print(r)
     up()
     if xcor() > 365.0:
      goto(-384.0,ycor() -40)
     down()


def f6():
    global busy
    if busy == 0:
     busy = 1
     up()
     forward(5)
     down()
     forward(10)
     right(180)
     forward(10)
     left(90)
     forward(20)
     left(90)
     forward(10)
     left(90)
     forward(10)
     left(90)
     forward(10)
     right(90)
     forward(10)
     right(90)
     forward(10)
     busy = 0
     r = xcor()
     print(r)
     up()
     if xcor() > 365.0:
      goto(-384.0,ycor() -40)
     down()



def f9():
  global busy
  if busy == 0:
    busy = 1
    up()
    forward(5)
    down()
    forward(10)
    right(90)
    forward(20)
    right(90)
    forward(10)
    right(90)
    up()
    forward(10)
    down()
    right(90)
    forward(10)
    left(180)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    busy = 0
    r = xcor()
    print(r)
    up()
    if xcor() > 365.0:
      goto(-384.0,ycor() -40)
    down()




def f10():
  global busy
  if busy == 0:
    busy = 1
    up()
    forward(5)
    right(90)
    forward(15)
    down()
    begin_fill()
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(180)
    forward(5)
    left(90)
    end_fill()
    up()
    forward(15)
    right(90)
    busy = 0
    r = xcor()
    print(r)
    if xcor() > 365.0:
      goto(-384.0,ycor() -40)

    
    



     



onkey(f8,"8")
onkey(f1,"1")
onkey(f0,"0")
onkey(f4,"4")
onkey(f7,"7")
onkey(f2,"2")
onkey(f5,"5")
onkey(f3,"3")
onkey(f6,"6")
onkey(f9,"9")
onkey(f10,".")

listen()

