import streamlit as st
import base64
from PIL import Image
import streamlit.components.v1 as components
import json
import requests
from bs4 import BeautifulSoup
from auth import API_KEY


def st_title(title_text, color=(108, 144, 170)):
    st.markdown(f"""<p style="background: rgb{color}; padding: 1.05em 1.05em; margin: 0px 0.0em; line-height: '
                    f'1; border-radius: 0.25em;"><b>{title_text.upper()}</b></p>""", unsafe_allow_html=True)
    st.markdown("----")


def st_html(html_path, width=600, height=400):
    html = open(html_path, 'r', encoding='utf-8')
    source_code = html.read()
    components.html(source_code, width, height)


def st_gif(gif_path, sidebar=False):
    code = _generate_base64_str_for_gif(gif_paths=gif_path)
    if sidebar:
        st.sidebar.markdown(code, unsafe_allow_html=True)
    else:
        st.markdown(code, unsafe_allow_html=True)


def st_img(img_path, sidebar=False):
    img_to_show = Image.open(img_path)
    if sidebar:
        st.sidebar.image(img_to_show)
    else:
        st.image(img_to_show)


def _generate_base64_str_for_gif(gif_bytes=None, gif_paths=None):
    if gif_paths is None and gif_bytes is None:
        raise SyntaxError("gif_bytes or gif_paths should be defined")

    if gif_paths:
        try:
            gif_bytes = _load_bytes(gif_paths)
        except FileNotFoundError:
            return

    data_url = base64.b64encode(gif_bytes[0]).decode("utf-8")
    return f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">'


def _load_bytes(paths):
    bytes = []

    if type(paths) is str:
        with open(paths, "rb") as reader:
            bytes.append(reader.read())

    elif type(paths) is list:
        for p in paths:
            with open(p, "rb") as reader:
                bytes.append(reader.read())

    else:
        raise TypeError("wrong type of data")

    return bytes


def yandex_api(esr_start, esr_end, api_key=API_KEY):

    request_txt = f"https://api.rasp.yandex.net/v3.0/search/?apikey={api_key}" \
                  f"&format=json" \
                  f"&from={esr_start}" \
                  f"&to={esr_end}" \
                  f"&transport_types=train" \
                  f"&system=esr"

    getpage = requests.get(request_txt)
    getpage_soup = BeautifulSoup(getpage.text, 'html.parser')
    json.loads(str(getpage_soup))
