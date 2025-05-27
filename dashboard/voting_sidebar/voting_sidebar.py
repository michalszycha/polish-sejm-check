import streamlit as st
import pandas as pd


def voting_table(voting: pd.DataFrame):
    voting_on_list = voting[voting['kind'] == 'ON_LIST']
    voting = voting[voting['kind'] != 'ON_LIST']

    voting = voting.drop(['voteOptionCount'], axis=1)
    voting_on_list = voting_on_list.drop(['yes', 'no', 'abstain', 'percentOfYes'], axis=1)

    st.header("Yes/No Voting")
    st.dataframe(data=voting, hide_index=True)

    st.header("List Voting")
    st.dataframe(data=voting_on_list, hide_index=True)
