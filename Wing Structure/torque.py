import math as m
import scipy as sp
from scipy import integrate
from extra_constants import *
thust_torque = 1 #Ignoring the drag becasue invicid fow


cm = []
y = []

S = 1 #Area of that small section of the wing NOT the whole wing
cm = []  #Moment coefficint of the section
c = 1 #Chord length at that y position
M = cm*S*c*q + 1#SOME way to shift the position of the moemnt along the chord  from 0.25c?? to teh flexure axis
