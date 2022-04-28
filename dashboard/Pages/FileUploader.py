from io import StringIO

import pandas as pd
import streamlit as st
import pickle

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

	st.markdown(
		f"""
		<div>
			<h1><img class="img" src="https://cdn-icons-png.flaticon.com/512/180/180855.png"/> File Upload </h1>
		</div>
		""",
		unsafe_allow_html=True
	)
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
		with open('logistic_regression_model.p', 'rb') as f:
			model = pickle.load(f)
		
		y_pred = model.predict(dataframe)

		i = 1
		for pred in y_pred:
			if pred == 1:
				st.write("Application " + str(i) + ": Reject") 
			else:
				st.write("Application " + str(i) + ": Accept") 
			i += 1