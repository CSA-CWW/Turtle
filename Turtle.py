import turtle
wn = turtle.Screen()
wn.bgcolor("white")
bob = turtle.Turtle()
bob.pensize (5) 
bob.color('blue','black')
def spiral():
    bob.right(6)
    bob.forward(1)
for spiral in range(275):
    bob.speed(0) 
    bob.right(50)
    bob.forward(1 * spiral)
y = "."
x = input("Did you like the shape i just drew?")
print ("So that's a" +x+ " well that's good to know.") 


#Cameron#
#Prog#
#9/14/17# 
