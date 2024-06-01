import pandas as pd
import voting.extract.VotingExtractor as Extract
import voting.transform.VotingTransform as Transform
import asyncio


def prepare_voting(sittings: pd.DataFrame) -> pd.DataFrame:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    voting = loop.run_until_complete(Extract.get_voting(sittings['number'].unique()))
    voting = Transform.add_id_column(voting)
    voting = Transform.change_columns_order(voting)
    loop.close()
    return voting


def prepare_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    voting = Transform.get_voting_per_mp(voting)
    voting = Transform.change_columns_in_voting_per_mp(voting)
    return voting
