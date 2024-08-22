import pandas as pd
import numpy as np

def predict_college(myrank, category, gender, institute_type, predictor_df, branch, college):
    seat_types = predictor_df['Seat Type'].unique().tolist()
    
    # Strict filtering based on institute_type
    if institute_type == 'IIT':
        predictor_df = predictor_df[predictor_df['Institute'].str.startswith('IIT')]
    elif institute_type == 'NIT':
        predictor_df = predictor_df[
            predictor_df['Institute'].str.startswith('NIT') | 
            predictor_df['Institute'].str.startswith('IIEST')
        ]
    elif institute_type == 'IIIT':
        predictor_df = predictor_df[predictor_df['Institute'].str.startswith('IIIT')]
    elif institute_type == 'GFTI':
        predictor_df = predictor_df[~predictor_df['Institute'].str.startswith(('IIT', 'NIT', 'IIIT', 'IIEST'))]
    
    filtered_df = predictor_df[
        (predictor_df['Gender'] == gender) &
        ((predictor_df['Seat Type'] == category) if category != 'All' else True) &
        ((predictor_df['Institute'] == college) if college != 'All' else True) &
        ((predictor_df['Academic Program Name'] == branch) if branch != 'All' else True) &
        ((predictor_df['Opening Rank'] <= myrank+450) &
        (predictor_df['Closing Rank'] >= myrank-450))
    ]
    # Define the category order
    category_order = seat_types
    # Sort by Opening Rank and custom category order
    filtered_df['Seat Type'] = pd.Categorical(filtered_df['Seat Type'], categories=category_order, ordered=True)
    filtered_df = filtered_df.sort_values(by=['Seat Type', 'Opening Rank'])
    return filtered_df
