import streamlit as st
import pickle

def page():
	st.markdown("<h1 style='text-align: center; color: white;'> Application Form</h1>", unsafe_allow_html=True)
	
	st.markdown("<p style='text-align: center; color: white;'> (This form utilizes a Logistic Regression Model to make the prediction.) </p>", unsafe_allow_html=True)

	with open('logistic_regression_model.p', 'rb') as f:
		model = pickle.load(f)

	with st.form("Application"):
		c1, c2 = st.columns(2)
		with c1:
			ExternalRiskEstimate = st.number_input('External Risk Estimate', step = 1)
			MSinceOldestTradeOpen = st.number_input('Months Since Oldest Trade Open', step = 1)
			AverageMInFile = st.number_input('Average Months in File', step = 1)
			NumSatisfactoryTrades = st.number_input('Number Satisfactory Trades', step = 1)
			NumTrades60Ever2DerogPubRec = st.number_input('Number Trades 60+ Ever', step = 1)
			NumTrades90Ever2DerogPubRec = st.number_input('Number Trades 90+ Ever', step = 1)
			PercentTradesNeverDelq = st.number_input('Percent Trades Never Delinquent', step = 1)
			MSinceMostRecentDelq = st.number_input('Months Since Most Recent Delinquency', step = 1)
			MaxDelq2PublicRecLast12M = st.number_input('Max Delq/Public Records Last 12 Months. See tab "MaxDelq" for each category', step = 1)
			MaxDelqEver = st.number_input('Max Delinquency Ever. See tab "MaxDelq" for each category', step = 1)
			NumTotalTrades = st.number_input('Number of Total Trades (total number of credit accounts)', step = 1)
		with c2:
			NumTradesOpeninLast12M = st.number_input('Number of Trades Open in Last 12 Months', step = 1)
			PercentInstallTrades = st.number_input('Percent Installment Trades', step = 1)
			MSinceMostRecentInqexcl7days = st.number_input('Months Since Most Recent Inq excl 7days', step = 1)
			NumInqLast6M = st.number_input('Number of Inq Last 6 Months', step = 1)
			NumInqLast6Mexcl7days = st.number_input('Number of Inq Last 6 Months excl 7days. Excluding the last 7 days removes inquiries that are likely due to price comparision shopping.', step = 1)
			NetFractionRevolvingBurden = st.number_input('Net Fraction Revolving Burden. This is revolving balance divided by credit limit', step = 1)
			NetFractionInstallBurden = st.number_input('Net Fraction Installment Burden. This is installment balance divided by original loan amount', step = 1)
			NumRevolvingTradesWBalance = st.number_input('Number Revolving Trades with Balance', step = 1)
			NumInstallTradesWBalance = st.number_input('Number Installment Trades with Balance', step = 1)
			NumBank2NatlTradesWHighUtilization = st.number_input('Number Bank/Natl Trades w high utilization ratio', step = 1)
			PercentTradesWBalance = st.number_input('Percent Trades with Balance', step = 1)

		submit = st.form_submit_button("Submit")

	if submit:
		prediction = model.predict([[ExternalRiskEstimate, MSinceOldestTradeOpen, AverageMInFile, NumSatisfactoryTrades,
									NumTrades60Ever2DerogPubRec, NumTrades90Ever2DerogPubRec, PercentTradesNeverDelq,
									MSinceMostRecentDelq, MaxDelq2PublicRecLast12M, MaxDelqEver, NumTotalTrades, 
									NumTradesOpeninLast12M, PercentInstallTrades, MSinceMostRecentInqexcl7days, NumInqLast6M,
									NumInqLast6Mexcl7days, NetFractionRevolvingBurden, NetFractionInstallBurden, 
									NumRevolvingTradesWBalance, NumInstallTradesWBalance, NumInstallTradesWBalance,
									NumBank2NatlTradesWHighUtilization, PercentTradesWBalance]])
	
		st.write(prediction)

	
