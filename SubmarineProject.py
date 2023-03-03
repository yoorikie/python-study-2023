from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from math import sqrt
from random import randint
from time import sleep, time

window = Tk()
WIDTH = 800
HEIGHT = 500

window.resizable(False, False)
window.title('$UßM@®INE')
messagebox.showinfo('Information', "Welcome to the Submarine Game! This is a project which took quite a time to make!\nUSAGE:\nWarning this game might glitch your computer if you click on the 'a' key. It is not recommended to those whose computer is quite old. USE ARROW KEYS TO MOVE.\nIMPORTANT MESSAGE!\nMUST BE READ\nClick on the window before moving. Otherwise, game won't work.\nGAME GOAL\n Score as much points as you can to win! THERE ARE NO ENDINGS!\nTHX")
messagebox.showinfo("Добро пожаловать в игру «Подводная лодка»! Это проект, на создание которого ушло довольно много времени!\nИСПОЛЬЗОВАНИЕ:\nПредупреждаем, что эта игра может привести к сбоям в работе вашего компьютера, если вы нажмете клавишу 'a'. Не рекомендуется тем, у кого компьютер достаточно старый. ИСПОЛЬЗУЙТЕ КЛАВИШИ СО СТРЕЛКАМИ ДЛЯ ПЕРЕМЕЩЕНИЯ.\nВАЖНОЕ СООБЩЕНИЕ!\nНЕОБХОДИМО ПРОЧИТАТЬ\nНажмите на окно, прежде чем двигаться. В противном случае игра не будет работать.\nЦЕЛЬ ИГРЫ\n Наберите как можно больше очков, чтобы победить! КОНЦА НЕТ!\nСПС!")
messagebox.askquestion('3,2...', 'START?')
c = Canvas(window, width = WIDTH, height =HEIGHT, bg ='lightblue')
c.pack()
ship_id = c.create_polygon(5, 5, 5, 25, 31, 15, fill ='red', outline ='black')
ship_id2 = c.create_oval(0, 0, 30, 30, outline ='black')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
SHIP_SPD = 10

bub_id =list()
bub_r =list()
bub_speed =list()

MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10

GAP = 100
def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r,
                        outline = 'white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))

def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    elif event.keysym == 'Right':
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)
def move_bubbles():

    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)


c.bind_all('<Key>', move_ship)

def get_coords(id_num):


    pos = c.coords(id_num)


    x = (pos[0] + pos[2])/2

    y = (pos[1] + pos[3])/2


    return x, y

def del_bub(i):
    del bub_r[i]

    del bub_speed[i]

    c.delete(bub_id[i])

    del bub_id[i]

def clean_up_bubs():
    for i in range(len(bub_id)-1, -1, -1):

        x, y = get_coords(bub_id[i])

        if x < -GAP:

            del_bub(i)

def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2-x1)**2 + (y2 -y1)**2)
def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
                points += (bub_r[bub] + bub_speed[bub])
                del_bub(bub)
    return points
BUB_CHANCE = 10
TIME_LIMIT= 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT

def GodMode(event):
    global score
    global bonus
    for NICE in range(1, 900):
        score += 1000
        bonus += 1000
        c.itemconfig(ship_id, fill ='pink', outline ='yellow')
        c.itemconfig(ship_id2, outline ='lightgreen')
        c.create_text(550, 50, text ="YOU'RE IN GOD MODE", font ='impact 15 italic', fill = 'yellow')    
c.create_text(50, 30, text ='TIME', fill ='white', font ='impact')
c.create_text(150, 30, text ='SCORE', fill ='white', font ='impact')
time_text = c.create_text(50, 50, fill ='white')
score_text = c.create_text(150, 50, fill = 'white')
def show_score(score):
    c.itemconfig(score_text, text =str(score))
def show_time(time_left):
    c.itemconfig(time_text, text = str(time_left))
while time() < end:
    window.bind_all('<KeyPress-a>', GodMode)
    if randint(1, BUB_CHANCE) == 1:
            create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end + TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    c.move(ship_id, 0, 0)
    c.move(ship_id2, 0, 0)
    window.update()
    sleep(0.01)
c.create_text(MID_X, MID_Y, \
              text='GAME OVER', fill ='white',  font =('Impact', 30))
c.create_text( MID_X, MID_Y + 30, \
               text ='SCORE: ' + str(score), fill='white')
c.create_text( MID_X, MID_Y + 45, \
               text ='BONUS TIME: ' + str(bonus*TIME_LIMIT), fill='white')
window.mainloop()
