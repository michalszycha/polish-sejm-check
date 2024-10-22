import streamlit as st
import pandas as pd
from mps_sidebar.mps_sidebar import filtered_mps_table

st.title('Polish sejm check dashboard')

mps = pd.read_csv('../cache/mps_term10.csv')
voting = pd.read_csv('../cache/voting_term10.csv')
voting_per_mp = pd.read_csv('../cache/voting_per_mp_term10.csv')

mps_tab, = st.tabs(["MPs"])

with mps_tab:
    st.header("MPs")
    filtered_mps_table(mps)
