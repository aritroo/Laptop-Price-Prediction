import streamlit as st
import numpy as np
import math
import pickle
from PIL import Image
import urllib.request


# importing the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")
#st.image('banner.png')

# brand
company = st.sidebar.selectbox('Brand',df['Company'].unique())

# type of laptop
type = st.sidebar.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.sidebar.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

#weight
weight = st.sidebar.number_input('Weight of Laptop')

# touchscreen
touchscreen = st.sidebar.selectbox('Touchscreen',['No','Yes'])

# IPS
ips = st.sidebar.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.sidebar.number_input('Screen Size')

# resolution
resolution = st.sidebar.selectbox('Screen Resolution',['1920x1080','13366x768','1600x900','3840x2160','3200x1800',
'2880x1800','2560x1600','2560x1440','2304x1440'])

# cpu
cpu = st.sidebar.selectbox('CPU',df['Cpu brand'].unique())

# hdd
hdd = st.sidebar.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# ssd
ssd = st.sidebar.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

# gpu
gpu = st.sidebar.selectbox('GPU',df['Gpu Brand'].unique())

# os
os = st.sidebar.selectbox('OS',df['os'].unique())

if(company=='Apple'):
    st.image('apple.png')

elif(company=='HP'):
    if(type=='Gaming'):
        st.image('hp_gaming.jpg')
    else:
        st.image('hp.png')
elif(company=='Acer'):
    if(type=='Gaming'):
        st.image('acer_gaming.png')
    else:
        st.image('acer_notebook.png')
elif(company=='Asus'):
    if(type=='Gaming'):
        st.image('asus_gaming.jpg')
    else:
        st.image('asus_notebook.jpg')
elif(company=='Dell'):
    if(type=='Gaming'):
        st.image('dell_gaming.jpg')
    else:
        st.image('dell_notebook.jpg')
elif(company=='Chuwi'):
    st.image('Chuwi.jpg')
elif(company=='MSI'):
    if(type=='Gaming'):
        st.image('msi_gaming.jpg')
    else:
        st.image('msi_notebook.jpg')
elif(company=='Lenovo'):
    if(type=='Gaming'):
        st.image('lenevo_gaming.jpg')
    else:
        st.image('lenevo_notebook.jpg')
elif(company=='Microsoft'):
    st.image('microsoft.png')



if st.button('Predict Price'):
    # query
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size

    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query = query.reshape(1, 12)

    st.title("The Predicted Price of Selected Configuration : " + 
    str(int(np.exp(pipe.predict(query)[0]))) + " Rupees")
