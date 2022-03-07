import streamlit as st
import pandas as pd

from st_map import st_map
from st_utils import st_html


def send_parcel():
    df = load_df()
    stations = df["Краткое наименование"].tolist()
    col1, col2 = st.columns(2)
    cities = None
    with col1:
        station_start = st.selectbox("Выберите станцию отправления", stations)
        esr_start = df.loc[df["Краткое наименование"] == station_start].values[0]
        st.info(f"🔵Код ЕСР: {esr_start[0]} \t🌐Координаты: {esr_start[5]}")
    with col2:
        station_end = st.selectbox("Выберите станцию назначения", stations)
        esr_end = df.loc[df["Краткое наименование"] == station_end].values[0]
        st.info(f"🔵Код ЕСР: {esr_end[0]} \t🌐Координаты: {esr_end[5]}")

    cities = df.loc[df["Код ЕСР"].isin([esr_start[0], esr_end[0]])]
    st.dataframe(cities.drop(["coords", ], 1))
    _cities = cities if cities.shape[0] > 1 else None
    st_map(_cities)
    st_html("map.html", width=1400)
    st.info("Найдены следующие маршруты:")
    with st.form("Отправить запрос"):
        st.checkbox("Маршрут 1")
        st.checkbox("Маршрут 2")
        st.checkbox("Маршрут 3")
        submit = st.form_submit_button("OK")
    if submit:
        st.success("Запрос отправлен. Ждите ответ.")


def track_parcel():
    parcel = st.text_input("Введите номер посылки")
    if parcel == '1':
        st.success("Посылка доставлена в пункт назначения")
    elif parcel == '2':
        st.info("Посылка в пути")
        st.markdown("")
        st_map(zoom_start=8)
        st_html("map.html", width=1400)
    else:
        st.error("Посылка не найдена")


def station_stats():
    pass


def train_stats():
    pass


def show_info():
    pass


@st.experimental_memo
def load_df():
    df = pd.read_csv("./data/msc.csv", index_col=0)
    return df
