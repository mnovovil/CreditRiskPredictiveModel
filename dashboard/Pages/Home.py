import streamlit as st
import seaborn as sns
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def page():
	st.markdown(
		"""
		<style>
		.img{
			width:50px;
			height:50px;
		}
		</style>
		""",
		unsafe_allow_html=True
	)

	st.markdown("<h1 style='text-align: center; color: white;'><img class='img' src='https://emojigraph.org/media/messenger/house_1f3e0.png'/> Home Equity Line of Credit (HELOC) Application Evaluation </h1>", unsafe_allow_html=True)

	st.markdown("<h3 style='text-align: center; color: white;'> Using this dashboard, you can identify whether to accept or reject HELOC applications.</h3>", unsafe_allow_html=True)

	st.markdown("""---""")