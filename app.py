import streamlit as st
import pandas as pd
import numpy as np
import streamlit_authenticator as stauth
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

from auth import USERNAMES, PASSWORDS
from st_utils import *
from st_pages import *


def main():
    side_menu_list = [
        "Отправить посылку",
        "Отследить посылку",
        "Мониторинг по станции",
        "Мониторинг по маршруту",
        "Информация о проекте"
    ]
    st_img("./data/train.jpg", sidebar=True)
    side_menu_choice = st.sidebar.selectbox("", side_menu_list, key="side_menu")
    side_menu_idx = side_menu_list.index(side_menu_choice)

    # username = st.session_state["username"]
    if side_menu_idx == 0:
        st_title("Отправить посылку")
        send_parcel()
    elif side_menu_idx == 1:
        st_title("Отследить посылку")
        track_parcel()
    elif side_menu_idx == 2:
        st_title("Мониторинг по станции")
        station_stats()
    elif side_menu_idx == 3:
        st_title("Мониторинг по маршруту")
        train_stats()


def auth_basic():
    # authentication
    usernames = [n.lower() for n in USERNAMES]
    hashed_passwords = stauth.hasher(PASSWORDS).generate()
    authenticator = stauth.authenticate(USERNAMES, usernames, hashed_passwords,
                                        'cookie_test', 'signature_key', cookie_expiry_days=30)
    # set page settings
    st.set_page_config(page_title="web-app", page_icon=":package:", layout="wide",
                       menu_items={
                           'Get Help': 'https://alkaline-newsprint-93f.notion.site/263b07c78a1443c598ce223e84016dac',
                           'About': "### Отправка посылок\n----\nПриложение для отправки и трекинга"
                       })
    # change radio orientation
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # login
    name, authentication_status = authenticator.login('Login', 'main')
    print(name, authentication_status)
    if authentication_status:
        st.write('Welcome *%s*' % name)
        st.session_state.update({"username": name})
        main()
    elif not authentication_status:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')


if __name__ == "__main__":
    auth_basic()