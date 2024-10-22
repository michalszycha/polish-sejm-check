import streamlit as st
import pandas as pd


def filtered_mps_table(mps: pd.DataFrame):
    clubs = mps.club.unique().tolist()

    chosen_clubs = []
    for club in clubs:
        if st.checkbox(club):
            chosen_clubs.append(club)

    if chosen_clubs:
        filtered_mps = mps[mps.club.isin(chosen_clubs)]
    else:
        filtered_mps = mps

    st.dataframe(data=filtered_mps, hide_index=True)
