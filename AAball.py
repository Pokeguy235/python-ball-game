import tkinter
import time
import tkinter.messagebox
canvasWidth = 1000
canvasHeight = 1000
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue")
canvas.pack()
bat = canvas.create_rectangle(0, 0, 400, 100, fill="yellow")
ball = canvas.create_oval(0, 0, 100, 100, fill="deep pink")
windowOpen = True
def main_loop():
    while windowOpen == True:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
    if windowOpen == True:
        check_game_over()
score = 0

leftPressed = 0
rightPressed = 0

def on_key_press(event):
    #print("Afifi: press", event.keysym)
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1
    


def on_key_relase(event):
    #print("Afifi: release", event.keysym)
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0

batSpeed = 6
def move_bat():
    batMove = batSpeed*rightPressed - batSpeed*leftPressed
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    if ( batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)

ballMoveX = 4
ballMoveY = -4
setBatTop = canvasHeight-40
setBatBottom = canvasHeight-30
def move_ball():
    global ballMoveX, ballMoveY
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballMoveX < 0  and ballLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (ballLeft, batTop, batRight, batBottom ) = canvas.coords(bat)
        if ballRight > ballLeft and ballLeft < batRight:
            ballMoveY =-ballMoveY
    canvas.move(ball, ballMoveX, ballMoveY)

def check_game_over():
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballTop > canvasHeight:
        playAgain = tkinter.messagebox.askyesno(message="do you want to play again?")
    if playAgain == True:
        reset()
    else:
        close()    
def close():
    global windowOpen
    windowOpen = False
    window.destroy()
def reset():
    global leftPressed, rightPressed
    global ballMoveX, ballMoveY
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30, setBatBottom)
    global score
    score = 0

window.protocol("WM_DELETE_WINDOW",close)
window.bind('<KeyPress>', on_key_press)
window.bind('<KeyRelease>', on_key_relase)

reset()
main_loop()

import tkinter
window = tkinter.Tk()

button = tkinter.Button(window, text="do not press this button",width=40)
button.pack(padx=10, pady=10)
clickCount = 0

def onClick(event):
    print("Button clicked")
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="bruh! do! no! press! it!!!!!!!")
    elif clickCount == 2:
        button.configure(text="gah! next time no more button")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()

import tkinter
import time
import tkinter.messagebox
canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()
bat = canvas.create_rectangle(0, 0, 400, 100, fill="turquoise")
ball = canvas.create_oval(0, 0, 100, 100, fill="deep pink")
windowOpen = True
def main_loop():
    while windowOpen == True:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
    if windowOpen == True:
        check_game_over()
score = 0

leftPressed = 0
rightPressed = 0

def on_key_press(event):
    #print("Afifi: press", event.keysym)
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1
    


def on_key_relase(event):
    #print("Afifi: release", event.keysym)
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0

batSpeed = 6
def move_bat():
    batMove = batSpeed*rightPressed - batSpeed*leftPressed
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    if ( batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)

ballMoveX = 4
ballMoveY = -4
setBatTop = canvasHeight-40
setBatBottom = canvasHeight-30
def move_ball():
    global ballMoveX, ballMoveY
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballMoveX < 0  and ballLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (ballLeft, batTop, batRight, batBottom ) = canvas.coords(bat)
        if ballRight > ballLeft and ballLeft < batRight:
            ballMoveY =-ballMoveY
    canvas.move(ball, ballMoveX, ballMoveY)

def check_game_over():
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballTop > canvasHeight:
        playAgain = tkinter.messagebox.askyesno(message="do you want to play again?")
    if playAgain == True:
        reset()
    else:
        close()    
def close():
    global windowOpen
    windowOpen = False
    window.destroy()
def reset():
    global leftPressed, rightPressed
    global ballMoveX, ballMoveY
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30, setBatBottom)
    global score
    score = 0

window.protocol("WM_DELETE_WINDOW",close)
window.bind('<KeyPress>', on_key_press)
window.bind('<KeyRelease>', on_key_relase)

