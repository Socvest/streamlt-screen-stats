import streamlit as st
from st_screen_stats import st_screen_data
st.set_page_config(layout="wide")


st.write(st_screen_data())
