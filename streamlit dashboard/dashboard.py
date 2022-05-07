from datetime import date
from turtle import color
import altair as alt
from pyparsing import White
from sqlalchemy import false
import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components 

st.set_page_config(layout = "wide")
df = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/allFlows_reduced_withdate.csv", low_memory=False)
df2 = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/Distributionofattacks.csv", low_memory=False)

st.sidebar.title("Real-Time Network Flow DDOS Attacks")
st.sidebar.header("Dillon Alterio DDOS Dashboard")
st.sidebar.write("""Welcome to my interactive dashboard, this dashboard contains a dataframe that consist of DDOS attacks on a real-time universities network. 
                    Every column in the dataframe represents a network flow.  Please choose the selector box to view various charts and graphs pertaining to the dataset below:""")

st.header("Real-Time Network Flow DDOS Attacks")
page = st.sidebar.selectbox('Please Select a Page To View:',
  ['Welcome','All Network Flows', 'Network Flow Attack Timeline','Distribution of Attacks', 'Scatter Plot of Packet Sizes to Attacks','Line for Packet Attack Size'])

if page == 'Welcome':
  components.html("""
                  <style>
                    html {background-color: white;}
                    html {font-family:courier;}
                    h1 {font-size:300%;}
                    p {font-size:150%;}
                  </style>

                  <html>
                    <body>
                      <h1>Hello,welcome to my interactive Dashboard</h1>
                        <p> Attacks on networks are becoming more sophisticated and pose a serious threat to various types of infrastructures. 
                          Unavailability of services due to various forms of DDOS attacks drastically reduces the confidence in the security of that stored data and the ability for a 
                          business/infrastructure to operate efficently.  Throughout this dashboard, the user will be able to view various interactive dashboards that pertain to a real-life 
                          dataset that contains various forms of DDOS attacks.  This dataset includes a ten month timeframe in which network flows were documentated and processed through 
                          the companies custom built IDS(intrusion detection system).  After their IDS processed the network flows, their system indicates what network flows were DDOS 
                          attacks and what network flows were not.  With this information, I was able to create various interactive dashboards that the user will be able to access to gain a better 
                          knowledge on various aspects of DDOS attacks to a real-life network environment.  The user will gain some knowledge in understanding how, when, and through what protocol
                          these malicious acts were conducted in.</p>
                    </body>
                  </html>""", width=1200, height=600,)
  

if page == 'All Network Flows':
 
  clist = df['pr'].unique()
  attack = st.selectbox("Please Select an Attack Protocol Type:",clist)
  col1, col2 = st.columns(2)

  fig = px.histogram(df[df['pr'] == attack], 
    x = "attack_t", y = "attack_a", color="attack_t", title = 'Attack on Dataset',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)
  
  fig = px.pie(df[df['pr'] == attack],values='attack_a', names= "attack_t", title = "This chart")
  col2.plotly_chart(fig,use_container_width = True)

if page == 'Network Flow Attack Timeline':
  
  clist1 = df['Monthly'].unique()
  attack = st.selectbox("Please Select Monthly View of Attacks",clist1)
  col1, col2 = st.columns(2)
  
  fig = px.histogram(df[df['Monthly'] == attack], 
   x="Monthly", y="attack_a", color="attack_t", title = 'Monthly Attacks on Dataset',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)

  fig = px.pie(df[df['Monthly'] == attack],values='attack_a', names= "attack_t", title = "Pie graph displaying Monthly View")
  col2.plotly_chart(fig,use_container_width = True)

  clist2 = df['Weekly'].unique()
  attack = st.selectbox("Please Select Weekly Views of Attacks",clist2)
  col1, col2 = st.columns(2)
  
  fig = px.histogram(df[df['Weekly'] == attack], 
    x = "Weekly", y = "attack_a", color='attack_t', title = 'Weekly Attacks on Dataset',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)

  fig = px.pie(df[df['Weekly'] == attack],values='attack_a', names= "attack_t", title = "This chart")
  col2.plotly_chart(fig,use_container_width = True)

  clist3 = df['Daily'].unique()
  attack = st.selectbox("Please Select Daily Views of Attacks",clist3)
  col1, col2 = st.columns(2)
  
  fig = px.histogram(df[df['Daily'] == attack], 
    x = "Daily", y = "attack_a", color='attack_t', title = 'Daily Attacks on Dataset',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)

  fig = px.pie(df[df['Daily'] == attack],values='attack_a', names= "attack_t", title = "This chart")
  col2.plotly_chart(fig,use_container_width = True)

if page == 'Distribution of Attacks':
  
  clist = df2['Type of Attack'].unique()
  attack = st.selectbox("Select an attack type:",clist)
  col1, col2 = st.columns(2)
  
  fig = px.bar(df2[df2['Type of Attack'] == attack], 
    x='Type of Attack', y=['Network Flows', 'Network Attack Flows'] ,title = 'DDOS Network Flow Attacks on Dataset', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)
  
  fig = px.pie(df2,values='Network Attack Flows', names= "Type of Attack", title = "This chart")
  col2.plotly_chart(fig,use_container_width = True)

if page == 'Scatter Plot of Packet Sizes to Attacks':
  
  clist = df['ID'].unique()
  col1, col2 = st.columns(2)
  
  fig = px.scatter(df, x="ipkt", y="attack_t", color="attack_a", title="This chart shows the packet amounts that were used to attack the network")
  col1.plotly_chart(fig,user_container_width = True)

  fig = px.scatter(df, x="attack_t", y="pr", color="attack_a", title="This chart displays the protocol types that were used and what protocols were attacked")
  col2.plotly_chart(fig,user_container_width = True)

if page == 'Line for Packet Attack Size':
  
  clist = df['ID'].unique()
  col1, col2, col3, col4 = st.columns(4)
  
  fig = px.line(df, x='Date', y= ['attack_a','ID'] )
  col1.plotly_chart(fig)

  fig = px.line(df, x='Monthly', y= ['attack_a','ID'] )
  col2.plotly_chart(fig)

  fig = px.line(df, x='Weekly', y= ['attack_a','ID'] )
  col3.plotly_chart(fig)

  fig = px.line(df, x='Daily', y= ['attack_a','ID'] )
  col4.plotly_chart(fig)