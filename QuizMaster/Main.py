import pgzrun

w = 870
h = 650
WIDTH = w
HEIGHT = h

TITLE= 'Quiz Master'
marqueemessage = ''
G_over = False
score = 0
timeleft = 10
qfilenam = 'questions.txt'
questions = []
qcount = 0
qindex = 0

marqueebox = Rect(0,0,880,80)
questionbox = Rect(0,0,650,150)
timerbox = Rect(0,0,150,150)
skipbox = Rect(0,0,150,330)

answerbox1 = Rect(0,0,300,150)
answerbox2 = Rect(0,0,300,150)
answerbox3 = Rect(0,0,300,150)
answerbox4 = Rect(0,0,300,150)

anwerboxes = [answerbox1, answerbox2, answerbox3, answerbox4]

marqueebox.move_ip(0,0)
questionbox.move_ip(20,100)
timerbox.move_ip(700,100)
skipbox.move_ip(700,270)

answerbox1.move_ip(20,270)
answerbox2.move_ip(370,270)
answerbox3.move_ip(20,450)
answerbox4.move_ip(370,450)


def draw():
    global marqueemessage
    # marqueemessage = 'Welcome to QuizMaster'
    # marqueemessage = marqueemessage + f'Q:{qindex} of {qcount}'
    
    screen.draw.filled_rect(marqueebox, 'Black')
    screen.draw.filled_rect(questionbox, 'Green')
    screen.draw.filled_rect(timerbox, 'White')
    screen.draw.textbox(str(timeleft), timerbox, color = 'Black')
    screen.draw.filled_rect(skipbox, 'Purple')
    screen.draw.textbox('Skip', skipbox, color = 'White', angle = -90)
    screen.draw.filled_rect(answerbox1, 'Gray')
    screen.draw.filled_rect(answerbox2, 'White')
    screen.draw.filled_rect(answerbox3, 'Cyan')
    screen.draw.filled_rect(answerbox4, 'Orange')
    # screen.draw.textbox(marqueemessage, marqueemessage, color = 'White')

def update():
    pass
def rqfile():
    global qcount, questions
    qfile = open(qfilenam, 'r')
    for file in qfile:
        questions.append(file)
        qcount = qcount + 1
    qfile.close()
def readNQ():
    global qindex
    qindex = qindex + 1
    return questions.pop(0).split(',')
def on_mouse_down(pos):
    index = 1
    for answer in anwerboxes:
        if answer.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                gameover()
        index = index + 1
    if skipbox.collidepoint(pos):
        skip_q()    
def correct_answer():
    global score, timeleft, questions, question
    score = score + 1
    if questions:
        question = readNQ()
        timeleft = 10
    else:
        gameover()

def gameover():
    global question, timeleft, G_over
    msg = f'Gamer Over Your Final Score is {score}'
    question = [msg, '--', '--', '--', '--', 5]
    timeleft = 0
    G_over = True

def skip_q():
    global timeleft, question
    if questions and not G_over:
        question = readNQ()
        timeleft = 10
    else:
        gameover()

def update_timeleft():
    global timeleft
    if timeleft:
        timeleft = timeleft - 1
    else:
        gameover()

rqfile()
question = readNQ()
clock.schedule_interval(update_timeleft, 1)

pgzrun.go()