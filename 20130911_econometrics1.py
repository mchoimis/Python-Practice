import math
import decimal

w=0.75
mu=w*0.08+(1-w)*0.05
Var=pow(w, 2)*pow(0.07, 2) + pow((1-w), 2)*pow(0.04, 2) + 2*w*(1-w)*0.07*0.04*0.25
print w
print Var
print mu
print math.sqrt(Var)
