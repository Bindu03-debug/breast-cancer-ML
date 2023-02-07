# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:09:20 2023

@author: vishn
"""

import pickle
import streamlit as st
import numpy as np
import pandas as pd
#from flask import jsonify



#loding the saved model

KNN_model=pickle.load(open('./svm_model.pickle','rb'))


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://perks.optum.com/blog/sites/default/files/styles/article_feature/public/perks/093020_Breast-Cancer-blog.png?h=369f31b8&itok=iyuGItQj");
background-size: 180%;
background-position: fit;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;

}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding', False)

#silde bar for navigation

#page title
st.title('BREAST CANCER DETECTION')

ch =st.number_input("Enter clump_thickness value",min_value=1,max_value=10,step=1)
cell=st.number_input("Enter the  value of uniform_cell_size",min_value=1,max_value=10)
shape=st.number_input('Enter the value of uniform_cell_shape	',min_value=1,max_value=10)
mar=st.number_input("Enter the value of marginal_adhesion",min_value=1,max_value=10)
S=st.number_input("Enter the value of single_epithelial_size",min_value=1,max_value=10)
b=st.number_input("Enter the value of bare_nuclei",min_value=1,max_value=410)
d=st.number_input("Enter the value of bland_chromatin",min_value=1,max_value=10)
nor=st.number_input("Enter the value of normal_nucleoli",min_value=1,max_value=10)
cell=st.number_input("Enter the value of mitoses",min_value=1,max_value=10)

data=np.asarray([[ch,cell,shape,mar,S,b,d,nor,cell]])

    
predicted=''   
if st.button('Press Here to predict'):
    prd=KNN_model.predict(data) 
    if prd==4:
       predicted="Breast cancer"    
    else:
       predicted="NO Breast cancer"
st.success(predicted)       
        
    
    
    
    
    
    
    
    
    
    
 
    
    
    
    