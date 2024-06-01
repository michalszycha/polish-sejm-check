import pandas as pd


def add_id_column(voting: pd.DataFrame) -> pd.DataFrame:
    return voting.assign(id=range(1, len(voting) + 1))


def map_vote_options(row):
    if isinstance(row['votingOptions'], list):
        option_map = {str(option['optionIndex']): option['option'] for option in row['votingOptions']}
        list_votes = row['votes']['listVotes']
        votes = []
        for option_index, vote_status in list_votes.items():
            if vote_status == 'YES':
                votes.append(option_map.get(option_index, 'Unknown'))
            row['votes']['vote'] = votes
    return row


def normalize_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    df = pd.json_normalize(voting['votes'])
    df['sitting'] = voting['sitting'].values
    df['votingId'] = voting['id'].values
    df['votingNumber'] = voting['votingNumber'].values
    df['votingTitle'] = voting['title'].values
    df['votingTopic'] = voting['topic'].values
    df['votingDescription'] = voting['description'].values
    return df


def get_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    voting = voting.query('kind != "TRADITIONAL"')
    voting_with_options = voting.dropna(subset=['votingOptions'])
    voting_yes_no = voting[pd.isna(voting['votingOptions'])]

    voting_with_options = voting_with_options.explode('votes')
    voting_with_options = voting_with_options.apply(map_vote_options, axis=1)
    voting_with_options_normalized = normalize_voting_per_mp(voting_with_options)

    voting_yes_no = voting_yes_no.explode('votes')
    voting_yes_no_normalized = normalize_voting_per_mp(voting_yes_no)

    return pd.concat([voting_with_options_normalized, voting_yes_no_normalized], axis=0)


def change_columns_order(voting: pd.DataFrame) -> pd.DataFrame:
    return voting[
        [
            'id',
            'date',
            'sitting',
            'sittingDay',
            'votingNumber',
            'title',
            'topic',
            'description',
            'kind',
            'totalVoted',
            'notParticipating',
            'yes',
            'no',
            'abstain',
            'votingOptions',
            'votes',
        ]
    ]


def change_columns_in_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    return voting[
        [
            'MP',
            'firstName',
            'lastName',
            'votingId',
            'sitting',
            'votingNumber',
            'votingTitle',
            'votingTopic',
            'votingDescription',
            'vote',
        ]
    ]
