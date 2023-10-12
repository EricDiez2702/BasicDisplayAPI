import streamlit as st
from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay

st.title("The AI knows you better")
instagram_basic_display = InstagramBasicDisplay(app_id='631172465595715', app_secret='74c6eb8f791cb341222af420802db667', redirect_url='https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/')
st.write(instagram_basic_display.get_login_url())
