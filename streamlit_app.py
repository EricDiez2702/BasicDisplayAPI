import streamlit as st
import requests
import json

st.title("Basic Display API")

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

    data = response1.json()

    user_id = data.get('user_id')
    access_token = data.get('access_token')
    fields = 'id,username'

    accountUrl = f'https://graph.instagram.com/{user_id}?fields={fields}&access_token={access_token}'
    response2 = requests.get(accountUrl)
    
    if response2.status_code == 200:
        st.write(response2.json())
    else:
        st.write(f"La requête a échoué, code d'etat {response2.status_code}.")

    mediaListUrl = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,timestamp&access_token={access_token}'
    response3 = requests.get(mediaListUrl)
    st.write(type(response3))

    if response3.status_code == 200:
        st.write(response3.json())
    else:
        st.write(f"La requête a échoué, code d'etat {resposne3.status_code}.")

    json_obj = json.load(response3.content)

    for i in json_obj['media_type']:
        if i == "CAROUSEL_ALBUM":
            id = json_obj['id']
            mediaUrl = f'https://graph.instagram.com/{id}/children?fields=id,media_type,media_url&access_token={access_token}'
            response4 = requests.get(mediaUrl)
            st.write(response4.json())


