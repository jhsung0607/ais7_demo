import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="자동차 연비 app",
    page_icon="🚗",
    layout = "wide",
)

st.markdown("# 자동차 연비🚗")
st.sidebar.markdown("# 부릉부릉")
st.write("""
### 자동차 연비
""")

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
data_load_state = st.text('Loading data...')
data = load_data(url)
data_load_state.text("Done! (using st.cache)")


st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   data = data[data.model_year == selected_year]

if len(selected_origin) > 0:
   data = data[data.origin.isin(selected_origin)]

st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=data, x="origin").set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)

sns.countplot(data=data, x="cylinders").set_title("실린더 갯수별 자동차 연비 데이터 수")
st.pyplot(fig)

pxh = px.histogram(data, x="origin", title="지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)
