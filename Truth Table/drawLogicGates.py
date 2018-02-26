
gatePos = ['', 250]

def drawInputs(t, inputs, factor=1):
    t.pd()
    posX, posY = -350, 300
    for inp in inputs:
        moveTo(t, posX, posY)
        t.pd()
        t.seth(0)
        t.circle(5)
        
        # standard input
        t.seth(270)
        t.fd(500)

        # Notted input
        t.bk(500)
        t.seth(270)
        t.fd(10)
        t.lt(90)
        t.fd(10)
        t.rt(90)
        t.fd(10)
        drawNot(t, 1, factor)
        t.pd()
        t.fd(480-10*factor)
        
        posX += 20*factor

    # input labels
    posX, posY = -350, 300
    for inp in inputs:
        moveTo(t, posX, posY+10)
        t.write(inp)
        posX += 20*factor

def drawNot(t, heading=2, factor=1):
    headings = [90, 180, 0]
    t.seth(headings[heading-1])
    t.pd()
    # Triangle
    # t.lt(180)
    t.lt(90)
    t.fd(5*factor)
    t.lt(120)
    t.fd(10*factor)
    t.lt(120)
    t.fd(10*factor)
    t.lt(120)
    t.fd(5*factor)
    
    # Circle
    t.pu()
    t.lt(90)
    t.fd(9*factor)
    t.rt(90)

    t.pd()
    t.circle(1*factor)
    t.pu()
    t.lt(90)
    t.fd(2*factor)

def drawAnd(t, inputs, factor=1):
    global gatePos
    if gatePos[0] == '':
        gatePos[0] = -350 + 20*inputs
    else:
        gatePos[1] -= 40
    moveTo(t, gatePos[0], gatePos[1])
    t.pd()
    t.seth(270)
    t.fd(10*factor)
    t.lt(90)
    t.fd(10*factor)
    t.circle(10*factor, 180)
    t.fd(10*factor)
    t.lt(90)
    t.fd(10*factor)

    t.pu()
    t.lt(90)
    t.fd(20*factor)

def drawOr(t, inputs, factor=1):
    global gatePos
    if gatePos[0] == '':
        gatePos[0] = -350 + 20*inputs
    else:
        gatePos[1] -= 40
    moveTo(t, gatePos[0], gatePos[1])

    t.seth(270)
    t.fd(10*factor)
    
    # forward arc and sides
    t.pd()
    t.lt(90)
    t.fd(10*factor)
    t.circle(10*factor, 180)
    t.fd(10*factor)
    t.lt(90)
    
    t.pu()
    t.fd(20*factor)
    
    # rear arc
    t.pd()
    t.lt(90)
    t.circle(10*factor, 180)
    
    # move to output line position
    t.pu()
    t.lt(90)
    t.fd(10*factor)
    t.lt(90)
    t.fd(20*factor)
    
def moveTo(t, x=0, y=0):
    t.pu()
    t.goto(x, y)

def drawLine(t, factor=1):
    t.pd()
    t.fd(10*factor)
    t.pu()

def getNextGate():
    global gatePos
    if gatePos[0] == '':
        gatePos[0] = -350 + 20*inputs
    else:
        gatePos[1] -= 40