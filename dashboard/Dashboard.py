import streamlit as st

class Dashboard:

	def __init__(self) -> None:
		self.pages = []
	
	def Add_Page(self, title, func) -> None:
		self.pages.append({
                "title": title, 
                "function": func
            })

	def run(self):
		page = st.sidebar.selectbox('Select Page', self.pages, format_func = lambda x: x['title'])
		page['function']()
