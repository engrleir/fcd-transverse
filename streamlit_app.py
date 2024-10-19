""" 
Script to solve transverse bars in rectangular combined footings
"""

import math
import streamlit as st

st.title("RCD Transverse Bar Designer for Rectangular Combined Footings")

PI = 3.14159

c = st.number_input("Column Width, mm") # column dimension in mm
d = st.number_input("Effective Depth, mm") # effective depth

B = st.number_input("Footing Width, B, mm") # Footing size
W = st.number_input("Effective Witdh, mm") # Effective width

Pu = st.number_input("Ultimate Column Load, kN")*1000 # Ultimate load of column

st.write(f"W: {W} mm")

qu = Pu / (B*W)

st.write(f"qu: {1000*qu} kPa")

x = (B - c)/2
st.write(f"x: {x} mm")

Mu = 0.5*qu*W*x**2

st.write(f"Mu: {Mu/1e6} kN-m")

fc = 28
fy = 280

db = 20

Ab = PI*db**2/4

Rn = Mu / (0.9*W*d**2)
st.write(f"Rn: {Rn} MPa")

rreqd = 0.85*fc/fy*(1-(1-2*Rn/(0.85*fc))**0.5)*100

st.write(f"rreqd: {rreqd} %")

rmin=min(max(1.4/fy*100,fc**0.5/(4*fy)*100),4/3*rreqd)
st.write(f"rmin: {rmin} %")

r = max(rmin,rreqd)

st.write(f"use r: {r} %")

As = r*W*d/100
st.write(f"As: {As} mm2")

n = As / Ab
st.write(f"n: {n}")
st.write(f"say n = {math.ceil(n)} pcs")
