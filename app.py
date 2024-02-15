import pickle
import streamlit as st
st.title("laptop price predictor")
# import the model
pipe = pickle.load(open('mypipe.pkl','rb'))
data = pickle.load(open('mydata.pkl.pkl','rb'))
# brand
brand = st.selectbox('Brand',data['Company'].unique())
# type of laptop
type = st.selectbpox('type',data['TypeName'].unique())
# ram
type = st.selectbox('Ram(in GB'),[2,4,6,8,12,16,24,32,64]
# weight
weight = st.number_input('weight of the laptop')
# touchscreen
touchscreen = st.selectbox('TouchScreen',['NO','YES'])
# ips
ips = st.selectbox('Ips',['NO','YES'])
# screen size
screensize = st.number_input('Screen Size')
# resolution
resolution = st.selectbox('Screen Resolution',['1920*1000','1366*768',
'1600*900','3840*2160','3200*1800','2800*1800','2560*1600','2560*1440',
'2304*1440'])
# cpu
cpu = st.selectbox('Brand',data['Cpu brand'].unique())
# hdd
hdd = st.selectbox('HDD(in GB'),[0,128,256,512,1024,2048]
# ssd
ssd = st.selectbox('Ssd(in GB'),[0,8,128,256,512,1024]
# gpu
gpu = st.selectbox('gpu',data['gpu brand'].unique())
# 0s
os = st.selectbox(('Os'),data['Os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
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

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))














