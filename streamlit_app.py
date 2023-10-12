import streamlit as st
from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay
import requests

st.title("Basic Display API")
#instagram_basic_display = InstagramBasicDisplay(app_id='631172465595715', app_secret='74c6eb8f791cb341222af420802db667', redirect_url='https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/')
#st.write(instagram_basic_display.get_login_url())

OauthUrl = "https://api.instagram.com/oauth/authorize"
params = {
    'client_id':'631172465595715',
    'redirect_uri':'https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/',
    'scope':'user_profile,user_media',
    'response_type':'code'
}

response = requests.get(OauthUrl, params)
st.write(response.url)

code = st.text_input("Entrez le code d'authentification :")

code_recu = st.checkbox("Code reçu")

if code_recu:
    apiUrl = "https://api.instagram.com/oauth/access_token"
    data = {
        "client_id":'631172465595715',
        "client_secret":'74c6eb8f791cb341222af420802db667',
        "grant_type": "authorization_code",
        "redirect_uri":'https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/',
        "code":code
    }
    
    response1 = requests.post(apiUrl, data)
    st.write(response1.json())
