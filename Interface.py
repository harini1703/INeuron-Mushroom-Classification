import pickle
pickle_in=open('musroom.pkl','rb')
clf=pickle.load(pickle_in)

import streamlit as st
import pandas as pd
import numpy as np

st.title(" MUSHROOM PREDICTION APPLICATION")
nav=st.sidebar.radio('Navigation',["Home",'Prediction','Dataset'])

if nav=='Home':
  st.image("mushroom image.jpg",width=400)
  st.header("Mushroom-A Fungi:")
  st.write("A mushroom or toadstool is the fleshy, spore-bearing fruiting body of a fungus, typically produced above ground, on soil, or on its food source.Toadstool generally denotes one poisonous to humans.Mushroom can be differentiated as Edible and Poisonous")
  st.write("According to statistics China is a major edible mushroom producer.The country produces about half of all cultivated mushrooms, and around 2.7 kilograms (6.0 lb) of mushrooms are consumed per person per year by 1.4 billion people")
  st.write("The total mushroom production in India between 2010 and 2017 was approximately 0.13 million tons, accounting for a 4.3% increase in the average growth rate of mushrooms per annum. In particular, the total production of white button mushrooms is the highest, with a share of about 73% of total mushroom production.")
  st.image("chartmushroom.png",width=500)
  st.header("Edible and Poisonous:")
  st.subheader("Poisonous:")
  st.write("Many mushroom species produce secondary metabolites that can be toxic.Although there are only a small number of deadly species, several others can cause particularly severe and unpleasant symptoms.The death cap is the most poisonous mushroom in the world.The death cap is found throughout Europe and closely resembles edible straw mushrooms and caesar’s mushrooms.It is estimated that as little as half a mushroom contains enough toxin to kill an adult human.It has been involved in the majority of human deaths from mushroom poisoning")
  st.image("mushroom image1.jpg",width=400)
  st.subheader("Edible:")
  st.write("Edible mushrooms are the fleshy and edible fruit bodies of several species of macrofungi.Edibility may be defined by criteria that include absence of poisonous effects on humans and desirable taste and aroma. Edible mushrooms are consumed for their nutritional and culinary value. Mushrooms, especially dried shiitake, are sources of umami flavor.Mushrooms are cultivated in at least 60 countries.A fraction of the many fungi consumed by humans are currently cultivated and sold commercially. Commercial cultivation is important ecologically, as there have been concerns of depletion of larger fungi such as chanterelles in Europe, possibly because the group has grown popular, yet remains a challenge to cultivate.")
  st.image("edible30.jpg",width=500) 
  
  if nav=='Prediction':
  st.subheader("MUSHROOM PREDICTOR:")  
  if nav=='Prediction':
    st.subheader("MUSHROOM PREDICTOR:")

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
    c=8

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

  l=st.selectbox(" SELECT SURFACE TYPE ABOVE RING:",('Smooth','Silky','Fibrous','Scaly'))
  if l=='Smooth':
    l=0
  elif l=='Silky':
    l=1
  elif l=='Fibrous':
    l=2    
  else:
    l=3

  m=st.selectbox("SELECT SURFACE TYPE BELOW RING:",('Smooth','Silky','Fibrous','Scaly'))
  if m=='Smooth':
    m=0
  elif m=='Silky':
    m=1
  elif m=='Fibrous':
    m=2    
  else:
    m=3

  n=st.selectbox("SELECT COLOR OF THE ABOVE RING:",('White','Pink','Gray','Brown','Buff','Orange','Red','Cinnanmon', 'Yellow'))
  if n=='White':
    n=0
  elif n=='Pink':
    n=1
  elif n=='Gray':
    n=2
  elif n=="Brown":
    n=3
  elif n=='Buff':
    n=4
  elif n=="Orange":
    n=5
  elif n=="Red":
    n=6
  elif n=="Cinnanmon":
    c=7
  else:
    c=8    

  o=st.selectbox("SELECT COLOR OF THE BELOW RING:",('White','Pink','Gray','Brown','Buff','Orange','Red','Cinnanmon', 'Yellow'))
  if n=='White':
    n=0
  elif n=='Pink':
    n=1
  elif n=='Gray':
    n=2
  elif n=="Brown":
    n=3
  elif n=='Buff':
    n=4
  elif n=="Orange":
    n=5
  elif n=="Red":
    n=6
  elif n=="Cinnanmon":
    n=7
  else:
    n=8  

  p=st.selectbox("SELECT THE VEIL TYPE:",('partial','Universal'))
  if p=='partial':
    p=0
  else:
    p=1  

  q=st.selectbox("SELECT THE VEILCOLOR:",('White','Brown',"Orange",'Yellow'))
  if q=='White':
    q=0
  elif q=='Brown':
    q=1
  elif q=='Orange':
    q=2
  else:
    q=3

  r=st.selectbox("SELECT THE NUMBER OF RING:",('One','Two','None'))
  if r=='One':
    r=0
  elif r=='two':
    r=1
  else:
    r=2

  s=st.selectbox("SELECT YOUR RING TYPE:",('Pendant','Evanescent','Large','Flaring','None'))
  if s=='Pendant':
    s=0
  elif s=='Evanescent':
    s=1
  elif s=='Large':
    s=2
  elif s=="Flaring":
    s=3
  else:
    s=4    

  t=st.selectbox("SELECT THE SPORE PRINT COLOR:",('White','Brown','Black',"Chocolate",'Green',"Purple",'Orange','Yellow','Buff'))
  if t=='White':
    t=0
  elif t=='Brown':
    t=1
  elif t=='Black':
    t=2
  elif t=="Chocolate":
    t=3
  elif t=='Green':
    t=4
  elif t=="Purple":
    t=5
  elif t=="Orange":
    t=6
  elif t=="Yellow":
    t=7
  else:
    t=8  

  u=st.selectbox("SELECT THE POPULATION STATE:",('Several','Solitary','Scattered','Numerous','Abundant','Clustered'))
  if u=='Several':
    u=0
  elif u=='Solitary':
    u=1
  elif u=='Scattered':
    u=2
  elif u=="Numerous":
    u=3
  elif u=="Abundant":
    u=4
  else:
    u=5

  v=st.selectbox("SELECT THE HABITAT TYPE:",('Woods','Grasses','Path','Leaves','Urban','Meadows','Waste')) 
  if v=='Woods':
    v=0
  elif v=='Grasses':
    v=1
  elif v=='Path':
    v=2
  elif v=="Leaves":
    v=3
  elif v=="Urban":
    v=4
  elif v=="Meadows":
    v=5  
  else:
    v=6



result=''
if st.button('Predict'):
    result=clf.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v]]).squeeze()
    if result==0:
        st.success('THE MUSHROOM IS POISONOUS')
    else:
        st.success('THE MUSHROOM IS NOT POISONOUS')

  






if nav=='Dataset':
  st.header("About the Dataset:")
  st.write("Although this dataset was originally contributed to the UCI Machine Learning repository nearly 30 years ago, mushroom hunting is enjoying new peaks in popularity.")
  st.write("This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like leaflets three, let it be for Poisonous Oak and Ivy.")
  dataset=pd.read_csv("mushrooms.csv")
  if st.checkbox("Show the data"):
    st.dataframe(dataset)
    






   








