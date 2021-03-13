import streamlit as st

# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title("Broken Telephone")
st.write(
    "This projects explores the injection of noise into neural network communication models and mitigation techniques."
)

st.selectbox("Choose your language model:", ["Transformers (BERT)", "RNN Seq2Seq"])
text_input = st.text_input("Enter input text:")
st.selectbox(
    "Choose your channel model:", ["AWGN", "Rayleigh fading", "Atmospheric noise"]
)

st.markdown("## Output:")
st.write(text_input)
