
import streamlit as st

from Dashboard import Dashboard
from Pages import Home, DataAnalysis, ApplicationForm, FileUploader

dashboard = Dashboard()

dashboard.Add_Page("Home", Home.page)
dashboard.Add_Page("Data Analysis", DataAnalysis.page)
dashboard.Add_Page("Application Form", ApplicationForm.page)
dashboard.Add_Page("File Uploader", FileUploader.page)

dashboard.run()