""" 
Script to solve transverse bars in rectangular combined footings
"""

import math
import streamlit as st

PI = 3.14159

c = 400 # column dimension in mm
d = 375 # effective depth

B = 3250 # Footing size
W = c+d/2+240 # Effective width

Pu = 1280e3 # Ultimate load of column

print(f"W: {W} mm")

qu = Pu / (B*W)

print(f"qu: {1000*qu} kPa")

x = (B - c)/2
print(f"x: {x} mm")

Mu = 0.5*qu*W*x**2

print(f"Mu: {Mu/1e6} kN-m")

fc = 28
fy = 280

db = 20

Ab = PI*db**2/4

Rn = Mu / (0.9*W*d**2)
print(f"Rn: {Rn} MPa")

rreqd = 0.85*fc/fy*(1-(1-2*Rn/(0.85*fc))**0.5)*100

print(f"rreqd: {rreqd} %")

rmin=min(max(1.4/fy*100,fc**0.5/(4*fy)*100),4/3*rreqd)
print(f"rmin: {rmin} %")

r = max(rmin,rreqd)

print(f"use r: {r} %")

As = r*W*d/100
print(f"As: {As} mm2")

n = As / Ab
print(f"n: {n}")
print(f"say n = {math.ceil(n)} pcs")
