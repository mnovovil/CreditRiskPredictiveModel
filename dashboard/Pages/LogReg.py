import streamlit as st
import pickle
from Pages import Form

def page():
	st.title('Logistic Regression Model')
	st.write('Utilize a Logisitic Regression Model to make your prediction. Enter the application into the form below.')

	with open('logistic_regression_model.p', 'rb') as f:
		model = pickle.load(f)

	st.write(Form.page())
