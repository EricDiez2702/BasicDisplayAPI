import streamlit as st
from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay

instagram_basic_display = InstagramBasicDisplay(app_id='631172465595715', app_secret='74c6eb8f791cb341222af420802db667', redirect_url='http://localhost:8501/')
print(instagram_basic_display.get_login_url())

st.title("The AI knows you better")
