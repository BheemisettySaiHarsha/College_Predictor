import pandas as pd
import numpy as np

def preprocess(df):
    df['Institute'] = df['Institute'].str.replace('Indian Institute of Technology','IIT')
    df['Institute'] = df['Institute'].str.replace('National Institute of Technology','NIT')
    df['Institute'] = df['Institute'].str.replace('Indian Institute of Information Technology','IIIT')
    df['Institute'] = df['Institute'].str.replace('International Institute of Information Technology','IIIT')
    df['Institute'] = df['Institute'].str.replace('Indian Institute of Engineering Science and Technology','IIEST')
    # df['Academic Program Name'] = df['Academic Program Name'].str.replace(r'\(.*\)', '', regex=True)
    
    # Convert Opening Rank and Closing Rank to numeric and then to integers
    df['Opening Rank'] = pd.to_numeric(df['Opening Rank'], errors='coerce').astype('Int64')
    df['Closing Rank'] = pd.to_numeric(df['Closing Rank'], errors='coerce').astype('Int64')
    
    return df

def get_unique_sorted(df, column):
    return sorted(df[column].unique().tolist())
