import pandas as pd
import voting.extract.VotingExtractor as Extract
import voting.transform.VotingTransform as Transform
import asyncio
import nest_asyncio

nest_asyncio.apply()


def prepare_voting(sittings: pd.DataFrame) -> pd.DataFrame:
    async def get_voting(numbers):
        return await Extract.get_voting(numbers)

    sittings_numbers = sittings['number'].unique()
    loop = asyncio.get_event_loop()
    voting = loop.run_until_complete(get_voting(sittings_numbers))

    voting = Transform.add_id_column(voting)
    voting = Transform.add_percent_of_yes_column(voting)
    voting = Transform.change_columns_order(voting)

    return voting


def prepare_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    voting = Transform.get_voting_per_mp(voting)
    voting = Transform.change_columns_in_voting_per_mp(voting)
    return voting
