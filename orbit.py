import math
import turtle
try:
  import tkinter #for python3
except:
  import Tkinter #for python2


print("Enter the following information where the center of the gravitational force is (0, 0)")
s_x = float(input("x-coord of starting position: "))
s_y = float(input("y-coord of starting position: "))
s = [s_x, s_y]

v_x = float(input("x-coord of starting velocity: "))
v_y = float(input("y-coord of starting velocity: "))
v = [v_x, v_y]

k = float(input("gravitational constant: "))

mass = float(input("mass: "))

iterations = int(input("number of iterations: "))

zoom = float(input("zoom amount: "))

"""
#CIRCLE (almost)
s = [5, 5]
v = [0.707106, -0.707106]
k = 1
mass = 1
"""

"""
#ELLIPSE
s = [2, 7]
v = [1, -1]
k = 1.5
mass = 1
"""
"""
#HYPERBOLA
s = [-30, 2]
v = [1, 0.2]
k = 0.3
mass = 1
"""
"""
#PARABOLA (almost)
s = [-50, -100]
v = [2, 0.2]
k = 10
mass = 1
"""
a = [0, 0]

points = []
  
#print(str(0) + "     " + str(s[0]) + "   " + str(s[1]))


for i in range(0, iterations):
  d = math.sqrt(s[0]**2 + s[1]**2)
  
  a[0] = -(k*(mass/d**2) * s[0])
  a[1] = -(k*(mass/d**2) * s[1])
  
  #print(str(a[0]) + "   a   " + str(a[1]))
  #print(str(v[0]) + "   v   " + str(v[1]))
  
  v[0] += a[0]
  v[1] += a[1]
  
  s[0] += v[0]
  s[1] += v[1]
  
  points.append([s[0], s[1]])
  
  #print(str(i+1) + "     " + str(s[0]) + "   " + str(s[1]))
  
t = turtle.Turtle()
t.goto(0,0)
t.penup()
for i in points:
  x = zoom*i[0]
  y = zoom*i[1]
  
  t.goto(x, y)
  t.pendown()
  
try:
  tkinter.mainloop()
except:
  Tkinter.mainloop()

