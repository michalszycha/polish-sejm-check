import streamlit as st
import pandas as pd
from mps_sidebar.mps_sidebar import filtered_mps_table
from voting_sidebar.voting_sidebar import voting_table

st.title('Polish sejm check dashboard')

mps = pd.read_csv('../cache/mps_term10.csv')
voting = pd.read_csv('../cache/voting_term10.csv')
voting = voting.drop(['votingOptions', 'votes'], axis=1)
voting_per_mp = pd.read_csv('../cache/voting_per_mp_term10.csv')

mps_tab, voting_tab = st.tabs(["MPs", "Voting"])

with mps_tab:
    filtered_mps_table(mps)

with voting_tab:
    voting_table(voting)
