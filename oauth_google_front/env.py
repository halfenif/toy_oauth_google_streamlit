import streamlit as st
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    IS_DEBUG: bool

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str
    GOOGLE_TOKEN_URL: str
    GOOGLE_AUTHORIZATION_URL: str
    GOOGLE_REVOKE_URL: str
    GOOGLE_USERINFO_URL: str

    model_config = SettingsConfigDict(
        # Load .env first
        env_file=('.env')
    )