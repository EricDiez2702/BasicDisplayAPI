import streamlit as st
import requests

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

    mediaUrl = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,timestamp&access_token={access_token}'
    response3 = requests.get(mediaUrl)
    st.write(type(response3))

    if response3.status_code == 200:
        st.write(response3.json())
    else:
        st.write(f"La requête a échoué, code d'etat {resposne3.status_code}.")

    firstMedia = response3.json(0)
    st.write(firstMedia)
