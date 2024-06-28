import streamlit as st
import pandas as pd
import predict
import preprocess as pp

# Load and preprocess data
df_23 = pd.read_excel('josaa.xlsx')
df_23 = pp.preprocess(df_23)
df_22 = pd.read_excel('josaa_2022.xlsx')
df_22 = pp.preprocess(df_22)

def load(year):
    if year == 2023:
        return df_23
    elif year == 2022:
        return df_22

# Set page configuration
st.set_page_config(page_title="JEE Rank Analysis", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
analysis_type = st.sidebar.radio("Select Analysis Type", ['College Predictor', 'Opening and Closing Ranks'])
year = st.sidebar.selectbox('Select Year', [2023, 2022])
df = load(year)

# Page title and description
st.title("🎓 JEE Rank Analysis")
st.markdown("""
Welcome to the JEE Rank Analysis Tool. Use this tool to predict college admissions based on your JEE rank.
Select the analysis type and the year to get started.
""")

if analysis_type == 'College Predictor':
    st.header('🔍 College Predictor')
    predictor_df = load(year)
    
    # User inputs
    with st.form(key='college_predictor_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            myrank = st.number_input("Enter Your Rank", min_value=1, help="Enter your JEE rank to get predictions.")
            category = st.selectbox("Select Category", ['All'] + pp.get_unique_sorted(predictor_df, 'Seat Type'))
            gender = st.selectbox("Select Gender", predictor_df['Gender'].unique())
            institute_type = st.selectbox("Institute Type", ['IIT', 'NIT', 'IIIT', 'GFTI'])
            
        with col2:
            branches = ['All'] + pp.get_unique_sorted(predictor_df, 'Academic Program Name')
            institute_name = ['All'] + pp.get_unique_sorted(predictor_df, 'Institute')
            branch = st.selectbox("Select Branch", branches)
            college = st.selectbox("Select College", institute_name)
        
        submit_button = st.form_submit_button(label='Submit')
    
    # Display results
    if submit_button:
        filter_df = predict.predict_college(myrank, category, gender, institute_type, predictor_df, branch, college)
        
        # Convert rank columns to integers for display
        filter_df['Opening Rank'] = filter_df['Opening Rank'].astype('Int64')
        filter_df['Closing Rank'] = filter_df['Closing Rank'].astype('Int64')
        
        st.markdown("### 🎯 Predicted Colleges")
        st.table(filter_df)
        

elif analysis_type == 'Opening and Closing Ranks':
    st.header('📊 Opening and Closing Ranks')
    st.table(load(year))
    # Add logic for displaying opening and closing ranks
