import streamlit as st
from st_screen_stats import st_screen_data
st.set_page_config(layout="wide")

screen_data = st_screen_data()
st.write(screen_data)
