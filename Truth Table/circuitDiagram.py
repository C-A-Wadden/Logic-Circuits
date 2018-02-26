#import truthTable
import drawLogicGates
import turtle

t = turtle.Turtle()
inputs = ['A', 'B', 'C']
t.speed(0)
t.ht()

drawLogicGates.drawInputs(t, inputs)
drawLogicGates.drawAnd(t, len(inputs))
drawLogicGates.drawAnd(t, len(inputs))
drawLogicGates.drawOr(t, len(inputs))

turtle.done()