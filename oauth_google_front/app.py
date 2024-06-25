# Load .env
from env import Settings
config = Settings()

import streamlit as st
from streamlit_oauth import OAuth2Component
from datetime import datetime
from dateutil import tz

st.title("toy_oauth_google_streamlit")

AUTHORIZATION_URL = config.GOOGLE_AUTHORIZATION_URL
TOKEN_URL = config.GOOGLE_TOKEN_URL
REVOKE_URL = config.GOOGLE_REVOKE_URL
CLIENT_ID = config.GOOGLE_CLIENT_ID
CLIENT_SECRET = config.GOOGLE_CLIENT_SECRET
REDIRECT_URI = config.GOOGLE_REDIRECT_URI
SCOPE = "openid email profile"

oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_URL, TOKEN_URL, TOKEN_URL, REVOKE_URL)

if 'token' not in st.session_state:
  result = oauth2.authorize_button("Continue with Google", REDIRECT_URI, SCOPE, icon="data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 48 48'%3E%3Cdefs%3E%3Cpath id='a' d='M44.5 20H24v8.5h11.8C34.7 33.9 30.1 37 24 37c-7.2 0-13-5.8-13-13s5.8-13 13-13c3.1 0 5.9 1.1 8.1 2.9l6.4-6.4C34.6 4.1 29.6 2 24 2 11.8 2 2 11.8 2 24s9.8 22 22 22c11 0 21-8 21-22 0-1.3-.2-2.7-.5-4z'/%3E%3C/defs%3E%3CclipPath id='b'%3E%3Cuse xlink:href='%23a' overflow='visible'/%3E%3C/clipPath%3E%3Cpath clip-path='url(%23b)' fill='%23FBBC05' d='M0 37V11l17 13z'/%3E%3Cpath clip-path='url(%23b)' fill='%23EA4335' d='M0 11l17 13 7-6.1L48 14V0H0z'/%3E%3Cpath clip-path='url(%23b)' fill='%2334A853' d='M0 37l30-23 7.9 1L48 0v48H0z'/%3E%3Cpath clip-path='url(%23b)' fill='%234285F4' d='M48 48L17 24l-4-3 35-10z'/%3E%3C/svg%3E")
  if result:
    st.session_state.token = result.get('token')
    st.rerun()
else:
    # st.info(st.session_state.token)

    if "expires_at" in st.session_state.token:

        local_timestamp = int(st.session_state.token["expires_at"])

        # Convert UTC timestamp to UTC datetime
        utc_datetime = datetime.fromtimestamp(local_timestamp)
        #utc_datetime = datetime.utcfromtimestamp(local_timestamp)

        # specify your local timezone (e.g., "America/New_York")
        local_tz = tz.gettz('Asia/Seoul')

        # convert to local time
        local_datetime = utc_datetime.replace(tzinfo=tz.UTC).astimezone(local_tz)

        expires_at = local_datetime.strftime('%Y-%m-%d %H:%M:%S')
        st.text_input("expires_at", expires_at)
    else:
        st.error("No expires_at value")

    if "id_token" in st.session_state.token:
        st.text_area("id_token", st.session_state.token["id_token"], height=500)
    else:
        st.error("No id_token value")
    

    
