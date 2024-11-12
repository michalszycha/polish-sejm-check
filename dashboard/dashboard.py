import streamlit as st
import pandas as pd
from mps_sidebar.mps_sidebar import show_filtered_mps_table
from voting_sidebar.voting_sidebar import voting_table
from mps_voting_sidebar.mps_voting_sidebar import mps_voting

st.title('Polish sejm check dashboard')

mps = pd.read_csv('../cache/mps_term10.csv')
voting = pd.read_csv('../cache/voting_term10.csv')
voting = voting.drop(['votingOptions', 'votes'], axis=1)
voting_per_mp = pd.read_csv('../cache/voting_per_mp_term10.csv')

mps_tab_sidebar, voting_tab_sidebar, mps_voting_sidebar = st.tabs(["MPs", "Voting", "MPs voting"])

with mps_tab_sidebar:
    show_filtered_mps_table(mps)

with voting_tab_sidebar:
    voting_table(voting)

with mps_voting_sidebar:
    mps_voting(mps, voting_per_mp)
