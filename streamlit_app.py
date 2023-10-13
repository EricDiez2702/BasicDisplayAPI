import streamlit as st
import requests
import json

st.title("Basic Display API")

//Création de URL d'autorisation 
OauthUrl = "https://api.instagram.com/oauth/authorize"
params = {
    'client_id':'631172465595715',
    'redirect_uri':'https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/',
    'scope':'user_profile,user_media',
    'response_type':'code'
}

response = requests.get(OauthUrl, params)
st.write(response.url)

//Récupération du code 
code = st.text_input("Entrez le code d'authentification :")

code_recu = st.checkbox("Code reçu")

//Génération du token à partir du code d'autorisation
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

    //Récupération du token et de id utilisateur pour accès à son compte
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

    //Récupération de la liste de publication sur compte utilisateur
    mediaListUrl = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,timestamp&access_token={access_token}'
    response3 = requests.get(mediaListUrl)
    st.write(type(response3))

    if response3.status_code == 200:
        st.write(response3.json())
    else:
        st.write(f"La requête a échoué, code d'etat {response3.status_code}.")

    //Récupération des autres photos d'un même album
    testFirstMediaUrl = f'https://graph.instagram.com/18063413599377238/children?fields=id,media_type,media_url&access_token={access_token}'
    response4 = requests.get(testFirstMediaUrl)
    st.write(response4.json())


    //Test automatisation de la récupération des albums
    json_obj = json.loads(response3.content)

    for i in json_obj['media_type']:
        if i == "CAROUSEL_ALBUM":
            id = json_obj['id']
            mediaUrl = f'https://graph.instagram.com/{id}/children?fields=id,media_type,media_url&access_token={access_token}'
            response5 = requests.get(mediaUrl)
            st.write(response5.json())


