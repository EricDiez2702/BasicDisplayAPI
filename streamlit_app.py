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
    "code":'AQDcuAB6IP1-U8eZMno7cuzZO4nkTgNOHyImkIFYaeJ1-mkOk551Heb1b0L0PGi-EW0T_uRPBeuttvS_3N59coz1DgRZ-ABJPdbjMYE0cP0MBPVcKZnRfEspEkqGAdbx15l9jxfOoA6iWqrWZ6jZuuJ13Z49Okg1AIZaYO6GFFCKLogWD4GLI8cs7O9mTRfguo2w8-2UiAkb0spzNcFrV-xXxe3NCBiHZZr_kKvR7HeRCw&state=6f6da625-e4c2-492b-b40c-84337274ec39'
}

response = requests.post(API_URL, data)
print(response.json())
