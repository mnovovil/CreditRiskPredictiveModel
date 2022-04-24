import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def page():
	st.title('Data Analysis')

	st.header('Correlation Matrix')
	sns.set_theme(style="white")
	df = pd.read_csv("heloc_dataset_v1.csv")

	# Compute the correlation matrix
	corr = df.corr()

	# Generate a mask for the upper triangle
	mask = np.triu(np.ones_like(corr, dtype=bool))

	# Set up the matplotlib figure
	f, ax = plt.subplots(figsize=(11, 9))

	# Generate a custom diverging colormap
	cmap = sns.diverging_palette(230, 20, as_cmap=True)

	# Draw the heatmap with the mask and correct aspect ratio
	sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1, vmax=1,
				square=True, linewidths=.5, cbar_kws={"shrink": .5})
	ax.set_title('Correlation Matrix')

	st.pyplot(f)