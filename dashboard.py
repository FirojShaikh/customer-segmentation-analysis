# Step 7: Creating the Streamlit Dashboard with Custom Colors
# Save this code in a file named 'dashboard.py' and run it with 'streamlit run dashboard.py'

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the RFM DataFrame (ensure rfm is available from previous steps)
# For this example, assume rfm is already computed; in a real app, load it if saved
# e.g., rfm = pd.read_csv('rfm_data.csv') if saved earlier

rfm = pd.read_csv('./data/rfm_data.csv')

# Title of the dashboard
st.title("Customer Segmentation Dashboard")

# Custom color palette for visualizations
custom_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']  # Distinct colors: Red, Teal, Blue, Green
segment_colors = {
    'Loyal Customers': '#FF6B6B',    # Red
    'At-Risk Customers': '#4ECDC4',  # Teal
    'Occasional Buyers': '#45B7D1',  # Blue
    'New Customers': '#96CEB4'       # Green
}

# 1. Visualize RFM Distributions with Custom Colors
st.header("RFM Distributions")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Recency Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(data=rfm, x='Recency', bins=20, color=custom_colors[0], ax=ax1)  # Red
    ax1.set_title("Recency (Days Since Last Purchase)")
    st.pyplot(fig1)

with col2:
    st.subheader("Frequency Distribution")
    fig2, ax2 = plt.subplots()
    sns.histplot(data=rfm, x='Frequency', bins=20, color=custom_colors[1], ax=ax2)  # Teal
    ax2.set_title("Frequency (Number of Invoices)")
    st.pyplot(fig2)

with col3:
    st.subheader("Monetary Distribution")
    fig3, ax3 = plt.subplots()
    sns.histplot(data=rfm, x='Monetary', bins=20, color=custom_colors[2], ax=ax3)  # Blue
    ax3.set_title("Monetary (Total Spending)")
    st.pyplot(fig3)

# 2. Display Cluster Sizes and Attributes
st.header("Segment Sizes and Attributes")
segment_summary = rfm.groupby('Segment').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'CustomerID': 'count'
}).rename(columns={'CustomerID': 'Count'}).sort_values(by='Monetary', ascending=False)
st.table(segment_summary)

# 3. Show Revenue by Segment with Custom Colors
st.header("Revenue by Segment")
revenue_by_segment = rfm.groupby('Segment')['Monetary'].sum().sort_values(ascending=False)
fig4, ax4 = plt.subplots()
bars = revenue_by_segment.plot(kind='bar', ax=ax4, color=[segment_colors[seg] for seg in revenue_by_segment.index])
ax4.set_title("Total Revenue by Segment")
ax4.set_xlabel("Segment")
ax4.set_ylabel("Total Revenue")
for i, v in enumerate(revenue_by_segment):
    ax4.text(i, v, f'${v:,.2f}', ha='center', va='bottom', color='black')
st.pyplot(fig4)

# 4. Include Marketing Recommendations
st.header("Marketing Recommendations")
st.write("- **Loyal Customers**: Offer loyalty rewards, exclusive deals to maintain engagement.")
st.write("- **At-Risk Customers**: Send win-back emails, personalized offers to re-engage.")
st.write("- **Occasional Buyers**: Provide reminders, offer discounts on related items to boost frequency.")
st.write("- **New Customers**: Welcome offers, guided onboarding to encourage repeat purchases.")

fig1.savefig('./output/rfm_dist_recency.png')
fig2.savefig('./output/rfm_dist_frequency.png')
fig3.savefig('./output/rfm_dist_monetary.png')
fig4.savefig('./output/revenue_by_segment.png')