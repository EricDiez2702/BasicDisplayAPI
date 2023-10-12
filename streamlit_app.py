import streamlit as st
from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay
import requests

st.title("The AI knows you better")
instagram_basic_display = InstagramBasicDisplay(app_id='631172465595715', app_secret='74c6eb8f791cb341222af420802db667', redirect_url='https://basicdisplayapi-kkg3fuibtjua4gvin89ggb.streamlit.app/')
st.write(instagram_basic_display.get_login_url())

# Get the OAuth callback code
code = requests.args.get('code')

# Get the short lived access token (valid for 1 hour)
short_lived_token = instagram_basic_display.get_o_auth_token(code)

# Exchange this token for a long lived token (valid for 60 days)
long_lived_token = instagram_basic_display.get_long_lived_token(short_lived_token.get('access_token'))

print('Your token is: {}' .format(long_lived_token.access_token))
