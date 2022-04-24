import streamlit as st

def page():
	st.title("Home Equity Line of Credit (HELOC) Application Evaluation")

	st.write("Using this dashboard, you can identify whether to accept or reject HELOC applications. \
			You may choose from the models in the drop-down to aid in your decision.")
	
	st.write('Provided Models:')
	st.markdown("""
		* Logistic Regression
		* K-Nearest Neighbors
		* Decision Tree
		* Gradient Boosting
	""")
