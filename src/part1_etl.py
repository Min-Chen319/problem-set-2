'''
PART 1: ETL
- This code sets up the datasets for Problem Set 2
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import os
import pandas as pd

def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def extract_transform():
    # Step 1: Load data
    pred_universe = pd.read_csv(
        'https://www.dropbox.com/scl/fi/a2tpqpvkdc8n6advvkpt7/universe_lab9.csv?rlkey=839vsc25njgfftzakr34w2070&dl=1')
    arrest_events = pd.read_csv(
        'https://www.dropbox.com/scl/fi/n47jt4va049gh2o4bysjm/arrest_events_lab9.csv?rlkey=u66usya2xjgf8gk2acq7afk7m&dl=1')

    # Step 2: Aggregates
    charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
    charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name='count')

    # Step 3: PART 4 - Add felony_charge DataFrame
    felony_charge = arrest_events.groupby("arrest_id")["charge_degree"].apply(
        lambda x: any(charge == "F" for charge in x)
    ).reset_index(name="has_felony_charge")

    # Step 4: Merge with pred_universe
    merged_df = pred_universe.merge(felony_charge, on="arrest_id", how="left")

    return pred_universe, arrest_events, charge_counts, charge_counts_by_offense, felony_charge, merged_df
