import pickle
pickle_in=open('Mushroom.pkl','rb')
clf=pickle.load(pickle_in)

import streamlit as st
import pandas as pd
import numpy as np

st.title(" MUSHROOM PREDICTION APPLICATION")
st.header("MUSHROOM PREDICTOR:")  
a=st.selectbox("SELECT THE CAP-SHAPE:",('Convex','flat','Knoobed','Bell','Sunken','Conical'))
if a=='Convex':
  a=0
elif a=='Flat':
  a=1
elif a=='Knobbed':
  a=2    
elif a=='Bell':
  a=3
elif a=='Sunken':
  a=4
else:
  a=5  

b=st.selectbox('SELECT THE CAP-SURFACE:',('Scaly','Smooth','Fibrous','Grooves'))
if b=='Scaly':
  b=0
elif b=='Smooth':
  b=1
elif b=='Fibrous':
  b=2    
else:
  b=3

c=st.selectbox("SELECT THE CAP-COLOR:",('Brown','Gray','Red','Yellow','White','Buff','Pink','Cinnanmon','Purple', 'Green'))
if c=='Brown':
  c=0
elif c=='Gray':
  c=1
elif c=='Red':
  c=2
elif c=="Yellow":
  c=3
elif c=='White':
  c=4
elif c=="Buff":
  c=5
elif c=="Pink":
  c=6
elif c=="Cinnanmon":
  c=7
elif c=="Purple":
  c=8    
else:
  c=9

d=st.selectbox("SELECT STATE OF BRUISES:",('No','Yes'))
if d=='yes':
  d=1
else:
  d=0  

e=st.selectbox("SELECT THE ODOR:",('None','Foul','Fishy','Spicy','Almon','Anise','Pungent','Creosote','Musty'))
if e=='None':
  e=0
elif e=='Foul':
  e=1
elif e=='Fishy':
  e=2
elif e=="Spicy":
    e=3
elif e=='Almond':
  e=4
elif e=="Anise":
  e=5
elif e=="Pungent":
  e=6
elif e=="Creosote":
  c=7
else:
  e=8

f=st.selectbox("SELECT TYPE OF GILL ATTACHMENT:",('Free','Notched'))
if f=='Free':
  f=0
else:
  f=1  

g=st.selectbox("SELECT TYPE OF GILL SPACING:",('Close','Crowded'))
if g=='Close':
  g=0
else:
  g=1   

h=st.selectbox("SELECT THE GILL SIZE:",('Broad','Narrow'))
if h=='Broad':
  h=0
else:
  h=1  

i=st.selectbox("SELECT THE GILL COLOR:",('Buff','Pink','White','Brown','Gray','Chocolate','Purple','Black','Red','Yellow','Orange', 'Green'))
if i=='Buff':
  i=0
elif i=='Pink':
  i=1
elif i=='White':
  i=2
elif i=="Brown":
  i=3
elif i=='White':
  i=4
elif i=="Brown":
  i=5
elif i=="Gray":
  i=6
elif i=="Chocolate":
  i=7
elif i=="Purple":
  i=8    
elif i=='Black':
  i=9
elif i=='Red':
  i=10
elif i=='Yellow':
  i=11
elif i=='Orange':
  i=12
else:
  i=13      

j=st.selectbox("SELECT THE STALK SHAPE:",('tapering','Enlarging'))
if j=='Tapering':
  j=0
else:
  j=1   

k=st.selectbox('SELECT THE STALK ROOT:',('Bulbous','None','Equal','Cup','Rhizomorphs')) 
if k=='Bulbous':
  k=0
elif k=='None':
  k=1
elif k=='Equal':
  k=2    
elif k=='Cup':
  k=3
else:
  k=4  






   








