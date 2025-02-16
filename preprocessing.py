def preprocessing():
    import pandas as pd
    
    # Load data
    matches = pd.read_csv('./data/matches.csv')
    deliveries = pd.read_csv('./data/deliveries.csv')
    
    # Rename columns and drop unnecessary columns
    matches = matches.rename(columns={'id': 'match_id'})
    matches = matches.drop(columns=['date', 'method', 'umpire1', 'umpire2', 'city'])
    deliveries = deliveries.drop(columns=['player_dismissed', 'dismissal_kind', 'fielder'], axis=1)
    
    # Merge datasets
    data = matches.merge(deliveries, on='match_id', how='left')
    
    # Handle missing values
    data['winner'] = data['winner'].fillna(method='ffill').fillna('Draw')
    data['player_of_match'] = data['player_of_match'].fillna(method='ffill').fillna('Draw')
    
    # Standardize venue names
      # Consolidate all venue replacements into a single replace function
  # Define a mapping dictionary
    venue_mapping = {
    # M Chinnaswamy Stadium variations
    'M.Chinnaswamy Stadium': 'M Chinnaswamy Stadium',
    'M Chinnaswamy Stadium, Bengaluru': 'M Chinnaswamy Stadium',
    
    # Arun Jaitley Stadium and Feroz Shah Kotla variations
    'Feroz Shah Kotla': 'Arun Jaitley Stadium',
    'Arun Jaitley Stadium, Delhi': 'Arun Jaitley Stadium',
    
    # Eden Gardens variations
    'Eden Gardens, Kolkata': 'Eden Gardens',
    
    # Rajiv Gandhi International Stadium variations
    'Rajiv Gandhi International Stadium, Uppal': 'Rajiv Gandhi International Stadium',
    'Rajiv Gandhi International Stadium, Uppal, Hyderabad': 'Rajiv Gandhi International Stadium',
    
    # MA Chidambaram Stadium variations
    'MA Chidambaram Stadium, Chepauk': 'MA Chidambaram Stadium',
    'MA Chidambaram Stadium, Chepauk, Chennai': 'MA Chidambaram Stadium',
    
    # Himachal Pradesh Cricket Association Stadium variations
    'Himachal Pradesh Cricket Association Stadium, Dharamsala': 'Himachal Pradesh Cricket Association Stadium',
    
    # Maharashtra Cricket Association Stadium variations
    'Maharashtra Cricket Association Stadium, Pune': 'Maharashtra Cricket Association Stadium',
    
    # Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium variations
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam': 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
    
    # Narendra Modi Stadium variations
    'Sardar Patel Stadium, Motera': 'Narendra Modi Stadium',
    'Narendra Modi Stadium, Ahmedabad': 'Narendra Modi Stadium',
    
    # Barsapara Cricket Stadium variations
    'Barsapara Cricket Stadium, Guwahati': 'Barsapara Cricket Stadium',
    
    # Ekana Cricket Stadium variations
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow': 'Ekana Cricket Stadium, Lucknow',
    
    # Wankhede Stadium variations
    'Wankhede Stadium, Mumbai': 'Wankhede Stadium',
    
    # Dr DY Patil Sports Academy variations
    'Dr DY Patil Sports Academy, Mumbai': 'Dr DY Patil Sports Academy',
    
    # Punjab Cricket Association IS Bindra Stadium variations
    'Punjab Cricket Association Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium',
    'Punjab Cricket Association IS Bindra Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium',
    'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh': 'Punjab Cricket Association IS Bindra Stadium',
    
    # Brabourne Stadium variations
    'Brabourne Stadium, Mumbai': 'Brabourne Stadium'
     }

# Apply the mapping to the 'venue' column
    data['venue'] = data['venue'].replace(venue_mapping)

    
    return data

def matches_data():
    import pandas as pd
    
    # Load matches data
    matches = pd.read_csv('./data/matches.csv')
    
    # Rename columns and drop unnecessary columns
    matches = matches.rename(columns={'id': 'match_id'})
    matches = matches.drop(columns=['date', 'method', 'umpire1', 'umpire2', 'city'])
    
    # Handle missing values
    matches['winner'] = matches['winner'].fillna(method='ffill').fillna('Draw')
    matches['player_of_match'] = matches['player_of_match'].fillna(method='ffill').fillna('Draw')
    
    # Standardize venue names
    # Consolidate all venue replacements into a single replace function
    # Define a mapping dictionary
    venue_mapping = {
    # M Chinnaswamy Stadium variations
    'M.Chinnaswamy Stadium': 'M Chinnaswamy Stadium',
    'M Chinnaswamy Stadium, Bengaluru': 'M Chinnaswamy Stadium',
    
    # Arun Jaitley Stadium and Feroz Shah Kotla variations
    'Feroz Shah Kotla': 'Arun Jaitley Stadium',
    'Arun Jaitley Stadium, Delhi': 'Arun Jaitley Stadium',
    
    # Eden Gardens variations
    'Eden Gardens, Kolkata': 'Eden Gardens',
    
    # Rajiv Gandhi International Stadium variations
    'Rajiv Gandhi International Stadium, Uppal': 'Rajiv Gandhi International Stadium',
    'Rajiv Gandhi International Stadium, Uppal, Hyderabad': 'Rajiv Gandhi International Stadium',
    
    # MA Chidambaram Stadium variations
    'MA Chidambaram Stadium, Chepauk': 'MA Chidambaram Stadium',
    'MA Chidambaram Stadium, Chepauk, Chennai': 'MA Chidambaram Stadium',
    
    # Himachal Pradesh Cricket Association Stadium variations
    'Himachal Pradesh Cricket Association Stadium, Dharamsala': 'Himachal Pradesh Cricket Association Stadium',
    
    # Maharashtra Cricket Association Stadium variations
    'Maharashtra Cricket Association Stadium, Pune': 'Maharashtra Cricket Association Stadium',
    
    # Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium variations
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam': 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
    
    # Narendra Modi Stadium variations
    'Sardar Patel Stadium, Motera': 'Narendra Modi Stadium',
    'Narendra Modi Stadium, Ahmedabad': 'Narendra Modi Stadium',
    
    # Barsapara Cricket Stadium variations
    'Barsapara Cricket Stadium, Guwahati': 'Barsapara Cricket Stadium',
    
    # Ekana Cricket Stadium variations
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow': 'Ekana Cricket Stadium, Lucknow',
    
    # Wankhede Stadium variations
    'Wankhede Stadium, Mumbai': 'Wankhede Stadium',
    
    # Dr DY Patil Sports Academy variations
    'Dr DY Patil Sports Academy, Mumbai': 'Dr DY Patil Sports Academy',
    
    # Punjab Cricket Association IS Bindra Stadium variations
    'Punjab Cricket Association Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium',
    'Punjab Cricket Association IS Bindra Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium',
    'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh': 'Punjab Cricket Association IS Bindra Stadium',
    
    # Brabourne Stadium variations
    'Brabourne Stadium, Mumbai': 'Brabourne Stadium'
     }

# Apply the mapping to the 'venue' column
    matches['venue'] = matches['venue'].replace(venue_mapping)

    
    return matches
