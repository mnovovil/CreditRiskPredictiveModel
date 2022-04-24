import streamlit as st

def page():
	ExternalRiskEstimate = st.number_input('External Risk Estimate', step = 1)
	MSinceOldestTradeOpen = st.number_input('Months Since Oldest Trade Open', step = 1)
	AverageMInFile = st.number_input('Average Months in File', step = 1)
	NumSatisfactoryTrades = st.number_input('Number Satisfactory Trades', step = 1)
	NumTrades60Ever2DerogPubRec = st.number_input('Number Trades 60+ Ever', step = 1)
	NumTrades90Ever2DerogPubRec = st.number_input('Number Trades 90+ Ever', step = 1)
	PercentTradesNeverDelq = st.number_input('Percent Trades Never Delinquent', step = 1)
	MSinceMostRecentDelq = st.number_input('Months Since Most Recent Delinquency', step = 1)

	return ""
