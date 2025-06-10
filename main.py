import streamlit as st

st.header("Gemini English Grammar Check")
st.write("Hello")

st.button("Click me")
# st.download_button("Download file", data)

import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)

url = 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet'
st.link_button("Go to gallery", url)
st.page_link('https://docs.streamlit.io/develop/quick-reference/cheat-sheet', label="Home")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


# st.data_editor("Edit data", df)
st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")

# # Use widgets' returned values in variables:
# for i in range(int(st.number_input("Num:"))):
#     foo()
# if st.sidebar.selectbox("I:",["f"]) == "f":
#     b()
# my_slider_val = st.slider("Quinn Mallory", 1, 88)
# st.write(slider_val)

# Disable widgets to remove interactivity:
st.slider("Pick a number", 0, 100, disabled=True)