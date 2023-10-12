import streamlit as st
from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay
import requests

st.title("The AI knows you better")
instagram_basic_display = InstagramBasicDisplay(app_id='631172465595715', app_secret='74c6eb8f791cb341222af420802db667', redirect_url='https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/')
st.write(instagram_basic_display.get_login_url())

API_URL = "https://api.instagram.com/oauth/access_token"
data = {
    "client_id":'631172465595715',
    "client_secret":'74c6eb8f791cb341222af420802db667',
    "grant_type": "authorization_code",
    "redirect_uri":'https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/',
    "code":'AQDZxtkN7zaK5ypFEhR2QaynKStZwad1DH8ezyD9FMvDoyCaehtQhyZ3vHLGuw9BkfeEOl5J-jise6ErJZnYrDMSRPDgJ8QDwibuqGyK2Cg_L0AFcmb-vgUr1i_NapLB15JtffzktwRZlZS7Oo3yAbBA0AZdk-GbKToI1FxPaeNmnkyfGhOw6OBpFHo_5SSuY3LfLs8WyCqzzvecUXHy1BOx8lfSI-n0o0kxZdUvPI0Wag&state=60d6c5e9-3d9b-411c-81f8-9d6fc69dc529'
}

response = requests.post(API_URL, data)
st.write(response.json())
