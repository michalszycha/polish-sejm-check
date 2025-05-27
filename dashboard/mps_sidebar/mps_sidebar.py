import streamlit as st
import pandas as pd
import numpy as np


def filter_mps(mps: pd.DataFrame, active: bool):
    clubs = mps.club.unique().tolist()
    st.header("Kluby i koła poselskie")

    if active:
        mps = mps[mps['active'] == True]

    chosen_clubs = []
    for club in clubs:
        if st.checkbox(club):
            chosen_clubs.append(club)

    if chosen_clubs:
        filtered_mps = mps[mps.club.isin(chosen_clubs)]
    else:
        filtered_mps = mps

    return filtered_mps


def show_filtered_mps_table(mps: pd.DataFrame):
    active = st.checkbox("Active")
    filtered_mps_df = filter_mps(mps, active)
    st.header("Posłowie")
    st.dataframe(data=filtered_mps_df, hide_index=True)
    if active:
        st.write(f"Liczba posłów/posłanek z wybranych parti: {len(filtered_mps_df)}/460 {np.round(len(filtered_mps_df)/460*100, 2)}%.")
    else:
        st.write(f"Liczba posłów/posłanek z wybranych parti: {len(filtered_mps_df)}.")
