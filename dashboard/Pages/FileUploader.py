from io import StringIO

import pandas as pd
import streamlit as st
import pickle

def page():
	st.title('File Upload')
	st.write('Upload your file below pretty please with a cherry on top.')

	with st.form("File Upload"):
		uploaded_file = st.file_uploader("Choose a file")
		if uploaded_file is not None:
			# To read file as bytes:
			bytes_data = uploaded_file.getvalue()

			# To convert to a string based IO:
			stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

			# To read file as string:
			string_data = stringio.read()

			# Can be used wherever a "file-like" object is accepted:
			dataframe = pd.read_csv(uploaded_file)
			
		submit = st.form_submit_button("Submit")
	if submit:
		with open('../logistic_regression_model.p', 'rb') as f:
			model = pickle.load(f)
		
		y_pred = model.predict(dataframe)

		st.write(y_pred)
			
