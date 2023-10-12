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
    "code":'AQCiIXlY2tWvitBb84v0wv6crFHm-kKEGS5xrGJ8TjidUpdj6fIlkpZPBKmtXvtZevua4OXeAN1aHV_LaHXSPLbz9Go7fJsaK5tSc4jvQUP6B2cu2BCOj3_c1ipRmJaTuJ2Mgo-pbF1yA8xlzY5nzsey_SEAb228WjwrSBSAAHxY3meR6lY61dfd7_OhoS2uNqtcGXiggkO6K0d9FNmQtr08L_bcH-w2NhcsXDZYNa5dQQ&state=60d6c5e9-3d9b-411c-81f8-9d6fc69dc529'
}

response = requests.post(API_URL, data)
st.write(response.json())
