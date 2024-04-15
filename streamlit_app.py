# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:55:36 2024

@author: Soormayee
"""
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import numpy as np
import streamlit as st
import datetime
from datetime import date
st.title('WELCOME TO THE PALACE ROYALE HOTEL')


a=[] 
b=[] 
c=[] 
d=[] 
e=[] 
f=[] 
g=[]
h=[]
j=[]
#engine=create_engine('mysql+pymysql://root:soormayee,1@localhost/soormayee1')
#mycon=engine.connect()

    

    
load=st.button("I am a customer") 
load1=st.button("I am an employee")
if "load_state" not in st.session_state:
    st.session_state.load_state=False
if load or st.session_state.load_state:
    st.session_state.load_state=True
    
    DF2=pd.read_csv(hotel.csv)
                          
    st.dataframe(DF2)
    st.text("To continue booking,enter your personal details")
    p=st.text_input(("Please enter your Aadhar card number: ")) 
    q=st.text_input(("Please enter your Name: ")) 
    r=st.text_input(("Please enter your Phone Number: ")) 
    s=st.number_input(("Please enter your Age: ")) 
    a.append(p) 
    b.append(q) 
    c.append(r) 
    d.append(s) 
    st.text("Enter\n1 Executive,\n 2 for Royal,\n 3 for Royal family suite")
    t=st.radio('Select Room type',('Executive','Royal','Royal Family Suite'))
    u=st.radio("Will you be requiring an extra bed?:Enter Y/N",('YES','NO'))
    w=st.radio("Do you want to include Breakfast in your package:",('Yes','No'))
    dt = pd.to_datetime(st.date_input("Enter check-in date"))
    dt1 = pd.to_datetime(st.date_input("Enter check-out date"))
    v=(dt1-dt).days
                      
                      
   #To calculate price                     
        
    price=pd.Series([])
    i=[0,1,2]
        
    if(st.button("View bill")):
        
        if(t =='Executive'):
            price[0]=7000*v
            st.write("ROOM TYPE:",DF2.iloc[0,1],"X",v,":",price[0])
                              
        elif(t =='Royal'):
               
            price[0]=15000*v
            st.write("ROOM TYPE:",DF2.iloc[1,1],"X",v,":",price[0])
                
        else:
               
            price[0]=28000*v
            st.write("ROOM TYPE:",DF2.iloc[2,1],"X",v,":",price[0])
               
        if(u =='Yes'):
               
            price[1]=3000
            st.write("EXTRA BED: Yes ::",price[1])
               
        else:
            price[1]=0
            st.write("EXTRA BED: No::",price[1])
                
                
        if (w =='Yes'):
         
            price[2]=1000*v
            st.write("BREAKFAST INCLUDED:Yes::",price[2])
               
                
        else:
             
            price[2]=0
            st.write("BREAKFAST INCLUDED:No::",price[2])
                
        price1=pd.DataFrame({'s_no':i,'Price':price})
        total_price=price.sum()
        st.text("Total bill")
        st.text(total_price)
        e.append(total_price)
        f.append(t)
        g.append(u)
        h.append(v)
        j.append(w)
        l=np.arange(1,11)
else:
    if "load1_state" not in st.session_state:
        st.session_state.load1_state=False
    if load1 or st.session_state.load1_state:
        st.session_state.load1_state=True
        pas=st.text_input("enter password to continue",type="password")
        if(pas=='admin123'):
            info1=pd.read_sql('select information1.*,ROOM_TYPE,NUMBER_OF_DAYS,EXTRA_BED,BREAKFAST_INCLUDED,TOTAL_BILL from information1,sales where Aadhar_Number=AADHAR;',mycon)
            st.dataframe(info1)
            sales1=info1.TOTAL_BILL.sum()
            st.write("Sales for first month:",sales1)
            info2=pd.read_sql('select personal12.*,Room_type,Number_of_days,Extra_bed,Breakfast_included,Total_bill from personal12,Sales22 where Aadhar_Number=AADHAR;',mycon)
            st.dataframe(info2)
            sales2=info2.Total_bill.sum()
            st.write("Sales for second month:",sales2)
            info3=pd.read_sql('select personal33.*,Room_type,Number_of_days,Extra_bed,Breakfast_included,Total_bill from personal33,Sales44 where Aadhar_Number=AADHAR;',mycon)
            st.dataframe(info3)
            fig = plt.figure() 
            sales3=info3.Total_bill.sum()
            st.write("Sales for Third month:",sales3)
            l2=['Month 1','Month 2','Month 3']
            l1=[sales1,sales2,sales3] 
            plt.plot(l2,l1)
           
            st.pyplot(fig)
        else:
            st.text("wrong")
    #TO CREATE A DATAFRAME OF USER PREFERENCES AND STORING IT INTO SQL
                #data1={"Aadhar_Number":a,"Name":b,"Phone_Number":c,"Age":d}
               # print(data1)
               # DF1=pd.DataFrame(data1,index=[1])
               # DF1.to_sql('personal_details1',mycon,index=False,if_exists='append')"""

    #total_sales=pd.DataFrame({'Number_of_days':h,'Room_type':f,'Extra_bed':g,'Breakfast_Included':j,'Total_bill':e})
    #st.dataframe(total_sales)
    #info=pd.read_sql('SELECT * FROM information1;',mycon,)
