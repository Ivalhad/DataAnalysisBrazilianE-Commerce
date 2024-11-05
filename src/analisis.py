import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = os.path.join("data", "olist_order_payments_dataset.csv")
payments_df = pd.read_csv(data_path)

st.title("Data Analysis Brazilian E-Commerce Olist")
st.subheader("Bagaimana preferensi metode pembayaran dari pelanggan, dan apakah metode tertentu mempengaruhi nilai transaksi atau frekuensi pembelian?")

payment_analysis = payments_df.groupby('payment_type').agg(
    total_payment_value=('payment_value', 'sum'),
    transaction_count=('order_id', 'count'),
    avg_payment_value=('payment_value', 'mean')
).reset_index()

st.write("### Summary Table of Payment Methods")
st.dataframe(payment_analysis)

st.write("### Average Transaction Value per Payment Method")
fig, ax = plt.subplots()
sns.barplot(data=payment_analysis, x='payment_type', y='avg_payment_value', palette="viridis", ax=ax)
ax.set_title("Average Transaction Value by Payment Method")
ax.set_xlabel("Payment Method")
ax.set_ylabel("Average Transaction Value")
st.pyplot(fig)

st.write("### Purchase Frequency by Payment Method")
fig, ax = plt.subplots()
sns.barplot(data=payment_analysis, x='payment_type', y='transaction_count', palette="viridis", ax=ax)
ax.set_title("Purchase Frequency by Payment Method")
ax.set_xlabel("Payment Method")
ax.set_ylabel("Frequency")
st.pyplot(fig)
