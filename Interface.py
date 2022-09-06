import pickle
pickle_in=open('musroom.pkl','rb')
clf=pickle.load(pickle_in)

import streamlit as st
import pandas as pd
import numpy as np

st.title(" MUSHROOM PREDICTION APPLICATION")
nav=st.sidebar.radio('Navigation',["Home",'Prediction','Dataset','User'])

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
 st.write('CAP-SHAPE: _Convex-0, Flat-1 ,Knobbed-2 , Bell-3 , Sunken-4 , Conical-5_')
 a=st.selectbox("SELECT THE CAP-SHAPE:",(0,1,2,3,4,5))
 st.write('CAP-SURFACE: _Scaly-0 , Smooth-1 , Fibrous-2 , Grooves-3_')
 b=st.selectbox('SELECT THE CAP-SURFACE:',(0,1,2,3))
 st.write('CAP-COLOR: _Brown-0 , Gray-1 , Red-2 , Yellow-3 , White-4 , Buff-5 , Pink-6 , Cinnanmon-7, Purple-8, Green-9_')
 c=st.selectbox("SELECT THE CAP-COLOR:",(0,1,2,3,4,5,6,7,8,9))
 st.write('BRUISES:_Yes-1,No-0_')
 d=st.selectbox("SELECT STATE OF BRUISES:",(0,1))
 st.write('ODOR:_None-0,Foul-1,Fishy-2,Spicy-3,Almond-4,Anise-5,Pungent-6,Creosote-8,Musty-8_')
 e=st.selectbox("SELECT THE ODOR:",(0,1,2,3,4,5,6,7,8))
 st.write("GILL-ATTACHMENT:_Free-0,Notched:1_")
 f=st.selectbox("SELECT TYPE OF GILL ATTACHMENT:",(0,1))
 st.write("GILL-SPACING:_Close:0,Crowded:1_")
 g=st.selectbox("SELECT TYPE OF GILL SPACING:",(0,1))
 st.write("GILL-SIZE:_Broad-0,Narrow-1")
 h=st.selectbox("SELECT THE GILL SIZE:",(0,1))
 st.write("GILL-COLOR:_Buff-0,Pink-1,White-2,Brown-3,Gray-4,Chocolate-5,Purple-6,Black-7,Red-8,Yellow-9,Orange-10,Green-11_")
 i=st.selectbox("SELECT THE GILL COLOR:",(0,1,2,3,4,5,6,7,8,9,10,11))
 st.write("STALK-SHAPE:_Tapering-0,Enlarging-1")
 j=st.selectbox("SELECT THE STALK SHAPE:",(0,1))
 st.write('STALK ROOT:_Bulbous-0, None-1,Equal-2,Cup-3,Rhizomorphs-4_')
 k=st.selectbox('SELECT THE STALK ROOT:',(0,1,2,3,4))
 st.write("STALK-SURFACE-ABOVE-RING:_Smooth-0,Silky-1,Fibrous-2,Scaly-3_")
 l=st.selectbox(" SELECT SURFACE TYPE ABOVE RING:",(0,1,2,3))
 st.write("STALK-SURFACE-BELOW-RING:_Smooth-0,Silky-1,Fibrous-2,Scaly-3_")
 m=st.selectbox("SELECT SURFACE TYPE BELOW RING:",(0,1,2,3))
 st.write("STALK-COLOR-ABOVE-RING:_White-0,Pink:1,Gray-2,Brown-3,Buff-4,Orange-5,Red-6,Cinnanmon-7,Yellow-8_")
 n=st.selectbox("SELECT COLOR OF THE ABOVE RING:",(0,1,2,3,4,5,6,7,8))
 st.write("STALK-COLOR-BELOW-RING:_White-0,Pink:1,Gray-2,Brown-3,Buff-4,Orange-5,Red-6,Cinnanmon-7,Yellow-8_")
 o=st.selectbox("SELECT COLOR OF THE BELOW RING:",(0,1,2,3,4,5,6,7,8))
 st.write("VEIL-TYPE:_Partial-0,Universal-1_")
 p=st.selectbox("SELECT THE VEIL TYPE:",(0,1))
 st.write("VEIL-COLOR:_White-0,Brown-1,Orange-2,Yellow-3_")
 q=st.selectbox("SELECT THE VEILCOLOR:",(0,1,2,3))
 st.write("RING-NUMBER:_One-0,Two-1,None-2")
 r=st.selectbox("SELECT THE NUMBER OF RING:",(0,1,2))
 st.write("RING-TYPE:_Pendant-0,Evanescent-1,Large-2,Flaring-3,None-4")
 s=st.selectbox("SELECT YOUR RING TYPE:",(0,1,2,3,4))
 st.write("SPORE-PRINT-COLOR:_White-0,Brown-1,Black-2,Chocolate-3,Green-4,Purple-5,Orange-6,Yellow-7,Buff-8_")
 t=st.selectbox("SELECT THE SPORE PRINT COLOR:",(0,1,2,3,4,5,6,7,8))
 st.write("POPULATION:_Several-0,Solitary-1,Scattered-2,Numerous-3,Abundant-4,Clustered-5_")
 u=st.selectbox("SELECT THE POPULATION STATE:",(0,1,2,3,4,5))
 st.write("HABITAT:_Woods-0,Grasses-1,Path-2,Leaves-3,Urban-4,Meadows-5,Waste-6_")
 v=st.selectbox("SELECT THE HABITAT TYPE:",(0,1,2,3,4,5,6))

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
    
if nav=='User':
  st.header("_THANK YOU FOR VISITING OUR APP_!!")





   








