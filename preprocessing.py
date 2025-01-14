import pandas as pd

def preprocessing():
    
    matches=pd.read_csv('./data/matches.csv')
    deliveries=pd.read_csv('./data/deliveries.csv')
    
    matches = matches.rename(columns={'id': 'match_id'})
    matches=matches.drop(columns=['date','method','umpire1','umpire2','city'])
    deliveries=deliveries.drop(columns=['player_dismissed','dismissal_kind','fielder'],axis=1)
    data=matches.merge(deliveries,on='match_id',how='left')
    data['winner'] = data['winner'].fillna(method='ffill').fillna('Drow')
    data['player_of_match'] = data['player_of_match'].fillna(method='ffill').fillna('Drow')
    
    
    return data

def matches_data():
    matches=pd.read_csv('./data/matches.csv')
    matches = matches.rename(columns={'id': 'match_id'})
    matches=matches.drop(columns=['date','method','umpire1','umpire2','city'])
    matches['winner'] =matches['winner'].fillna(method='ffill').fillna('Drow')
    matches['player_of_match'] = matches['player_of_match'].fillna(method='ffill').fillna('Drow')
    
    
    return matches