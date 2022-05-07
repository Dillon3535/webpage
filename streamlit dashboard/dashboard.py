from datetime import date
import altair as alt
from sqlalchemy import false
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")
df = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/allFlows_reduced_withdate.csv", low_memory=False)
df2 = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/Distributionofattacks.csv", low_memory=False)

st.sidebar.title("Real-Time Network Flow DDOS Attacks")
st.sidebar.header("Dillon Alterio DDOS Dashboard")
st.sidebar.write("Welcome to my interactive dashboard, this dashboard contains a dataframe that consist of DDOS attacks on a real-time universities network.  Every column in the dataframe represents a network flow.  Please choose the selector box to view various charts and graphs pertaining to the dataset below:")
page = st.sidebar.selectbox('Please Select a Page:',
  ['Welcome','All Network Flows', 'Network Flow Attack Timeline','Distribution of Attacks', 'Scatter Plot of Packet Sizes to Attacks','Box plot for Packet Attack Size'])

if page == 'Welcome':
  st.title=("CSC 400 Interactive Dashboard")
  st.header=("Please Interact with the sidebar to the left in to interact with the dashboard")
  st.write=("Hello ")

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
  col1, col2 , col3= st.columns(3)
  
  fig = px.scatter(df, x="ipkt", y="attack_t", color="attack_a", title="This chart shows the packet amounts that were used to attack the network")
  col1.plotly_chart(fig,user_container_width = True)

  fig = px.scatter(df, x="attack_t", y="pr", color="attack_a", title="This chart displays the protocol types that were used and what protocols were attacked")
  col2.plotly_chart(fig,user_container_width = True)

if page == 'Line for Packet Attack Size':
  
  clist = df['ID'].unique()
  col1, col2 = st.columns(2)
  
  fig = px.line(df,values='attack_a', names= "attack_t", title = "This line graph sho")
  col2.plotly_chart(fig,use_container_width = True)