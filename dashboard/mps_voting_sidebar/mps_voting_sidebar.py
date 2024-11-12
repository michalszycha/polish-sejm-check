import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def choose_mp_id(mps: pd.DataFrame):
    choose_options = mps.apply(lambda row: f"{row['id']}, {row['firstName']} {row['lastName']}, {row['club']}", axis=1)
    chosen_id = st.selectbox(
        "Choose MP",
        choose_options
    ).split(',')[0]
    return int(chosen_id)


def plot_mps_voting(voting: pd.DataFrame):
    voting = voting[voting['kind'] != 'ON_LIST']
    vote_counts = voting['vote'].value_counts()
    st.write(vote_counts)

    color_map = {
        'YES': 'blue',  # 'yes' will always be blue
        'NO': 'red',  # 'no' will always be red
        'ABSTAIN': 'yellow',  # 'abstain' will always be yellow
        'ABSENT': 'grey'  # 'absent' will always be grey
    }
    colors = [color_map[label] for label in vote_counts.keys()]

    fig, ax = plt.subplots()
    ax.pie(
        vote_counts,
        labels=vote_counts.keys(),
        autopct='%1.2f%%',
        colors=colors,
    )
    fig.patch.set_alpha(1)
    return fig


def filter_voting(voting: pd.DataFrame):
    votes = voting[voting['kind'] != 'ON_LIST'].vote.dropna().unique().tolist()

    chosen_votes = []
    for vote in votes:
        if st.checkbox(vote):
            chosen_votes.append(vote)

    if chosen_votes:
        filtered_votes = voting[voting.vote.isin(chosen_votes)]
    else:
        filtered_votes = voting

    return filtered_votes


def mps_voting(mps: pd.DataFrame, voting_per_mp: pd.DataFrame):
    mp_id = choose_mp_id(mps)
    mp_voting = voting_per_mp[voting_per_mp['MP'] == mp_id]
    st.pyplot(plot_mps_voting(mp_voting))

    filtered_voting_df = filter_voting(mp_voting)
    st.dataframe(
        data=filtered_voting_df.drop(['MP'], axis=1),
        hide_index=True,
    )
