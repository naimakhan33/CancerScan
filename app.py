import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import warnings
import os

warnings.filterwarnings("ignore")

# ✅ Model + Scaler file checks + loading
if not os.path.exists("model.pkl"):
    st.error("❌ 'model.pkl' not found. Please make sure it is in the root directory.")
    st.stop()

if not os.path.exists("scaler.pkl"):
    st.error("❌ 'scaler.pkl' not found. Please make sure it is in the root directory.")
    st.stop()

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

        st.error(f"An error occurred during prediction:\n\n{e}")
