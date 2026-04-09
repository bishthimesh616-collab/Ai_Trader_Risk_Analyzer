import streamlit as st
import pandas as pd
import pickle
import random

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("📊 AI Trading Risk Analyzer")

st.write("Analyze your trading behavior and risk level")

# -------------------------------
# AUTO SENTIMENT (Simulated)
# -------------------------------
sentiment_score = random.choice([0.2, 0.5, 0.8])

if sentiment_score < 0.3:
    sentiment_label = "Fear 😨"
elif sentiment_score < 0.7:
    sentiment_label = "Neutral 😐"
else:
    sentiment_label = "Greed 😈"

st.subheader("📈 Current Market Sentiment")
st.write(sentiment_label)

# -------------------------------
# USER INPUT
# -------------------------------
st.subheader("📥 Enter Trading Details")

pnl = st.number_input("Closed PnL (Profit/Loss)", value=0.0)

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("🔍 Predict Risk"):

    # Match model features
    input_df = pd.DataFrame([[sentiment_score, pnl]],
                            columns=["sentiment_score", "Closed PnL"])

    prediction = model.predict(input_df)[0]

    # -------------------------------
    # OUTPUT
    # -------------------------------
    st.subheader("📊 Result")

    if prediction == "High":
        st.error("🚨 Risk Level: HIGH")
        st.write("⚠️ Advice: Reduce trading frequency and avoid high leverage")

    elif prediction == "Medium":
        st.warning("⚠️ Risk Level: MEDIUM")
        st.write("👉 Advice: Trade cautiously and manage risk")

    else:
        st.success("✅ Risk Level: LOW")
        st.write("👍 Advice: Safe trading behavior")
