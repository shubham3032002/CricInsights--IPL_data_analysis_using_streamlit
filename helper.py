import numpy as np 
import pandas as pd

def yearwise_champion(data):
    final_matches = data[data['match_type'] == 'Final']  # Filter finals
    final_teams = final_matches[['season', 'team1', 'team2', 'winner']]  # Select relevant columns
    final_teams.columns = ['Year', 'Team 1', 'Team 2', 'Winner']  # Rename columns for readability
    final_teams = final_teams.reset_index(drop=True)  # Reset index
    final_teams.index += 1  # Set index starting from 1
    return final_teams

def count_of_champion(data):
    final_matches = data[data['match_type'] == 'Final']  # Filter finals
    final_teams = final_matches[['season', 'team1', 'team2', 'winner']]  # Select relevant columns
    final_teams.columns = ['Year', 'Team 1', 'Team 2', 'Winner']  # Rename columns for readability
    final_teams = final_teams.reset_index(drop=True)
    
    # Count the number of wins per winner
    champion_count = final_teams['Winner'].value_counts().reset_index()
    champion_count.columns = ['Winner', 'Count']  # Rename the columns
    
    return champion_count

def top_batter(data):
    # Group by 'batter' and count the number of unique 'match_id' for each player
    matches_played = data.groupby('batter')['match_id'].nunique().reset_index(name='Matches Played')

    # Group by 'batter' and sum the total 'batsman_runs' for each player
    total_runs = data.groupby('batter')['batsman_runs'].sum().reset_index(name='Total Runs')

    # Merge the two DataFrames on 'batter' to combine the information
    player_stats = pd.merge(matches_played, total_runs, on='batter')

    # Calculate average runs per match
    player_stats['Average Runs'] = player_stats['Total Runs'] / player_stats['Matches Played']

    # Sort by the number of runs in descending order
    player_stats_sorted = player_stats.sort_values(by='Total Runs', ascending=False)

    # Get the top 10 batters
    top_10_batters = player_stats_sorted.head(10)

    # Reset the index and start it from 1
    top_10_batters = top_10_batters.reset_index(drop=True)
    top_10_batters.index += 1  # Start index from 1

    return top_10_batters

def season_wise_top_batter(data, season):
    # Filter the data for the selected season
    season_data = data[data['season'] == season]

    # Group by 'batter' and count the number of unique 'match_id' for each batter (matches played)
    matches_played = season_data.groupby('batter')['match_id'].nunique().reset_index(name='Matches Played')

    # Group by 'batter' and sum the total 'batsman_runs' for each batter (total runs)
    total_runs = season_data.groupby('batter')['batsman_runs'].sum().reset_index(name='Total Runs')

    # Merge the two DataFrames on 'batter' to combine the information
    player_stats = pd.merge(matches_played, total_runs, on='batter')

    # Sort by 'Total Runs' in descending order to get the top batters
    player_stats_sorted = player_stats.sort_values(by='Total Runs', ascending=False)

    # Get the top 5 batters for the selected season
    top_5_batters = player_stats_sorted.head(5)

    # Reset the index and make it start from 1
    top_5_batters = top_5_batters.reset_index(drop=True)
    top_5_batters.index += 1  # Start index from 1

    return top_5_batters

def top_10_blower(data):
    # Group by 'bowler' and count the number of unique 'match_id' for each player
    matches_played = data.groupby('bowler')['match_id'].nunique().reset_index(name='Matches Played')

    # Group by 'bowler' and sum the total 'is_wicket' for each player
    total_wickets = data.groupby('bowler')['is_wicket'].sum().reset_index(name='Total Wickets')

    # Merge the two DataFrames on 'bowler' to combine the information
    player_stats = pd.merge(matches_played, total_wickets, on='bowler')

    # Sort by the number of matches played in descending order
    player_stats_sorted = player_stats.sort_values(by='Total Wickets', ascending=False)

    # Get the top 10 bowlers
    top_10_bowler = player_stats_sorted.head(10)
     

    # Reset the index and start it from 1
    top_10_bowler = top_10_bowler.reset_index(drop=True)
    top_10_bowler.index += 1  # Start index from 1

    top_10_bowler
    return top_10_bowler
def season_wise_top_bowler(data, season):
    # Filter the data for the selected season
    season_data = data[data['season'] == season]

    # Group by 'bowler' and count the number of unique 'match_id' for each bowler (matches played)
    matches_played = season_data.groupby('bowler')['match_id'].nunique().reset_index(name='Matches Played')

    # Group by 'bowler' and sum the total 'is_wicket' for each bowler (total wickets)
    total_wickets = season_data.groupby('bowler')['is_wicket'].sum().reset_index(name='Total Wickets')

    # Merge the two DataFrames on 'bowler' to combine the information
    player_stats = pd.merge(matches_played, total_wickets, on='bowler')

    # Sort by 'Total Wickets' and 'Matches Played' in descending order to get the top bowlers
    player_stats = player_stats.sort_values(by=['Total Wickets', 'Matches Played'], ascending=False)

    # Reset the index and make it start from 1
    player_stats.reset_index(drop=True, inplace=True)
    player_stats.index = player_stats.index + 1  # Adjust the index to start from 1

    # Return the top 5 bowlers for the selected season
    return player_stats.head(5)





def top_10_man_of_match(matches):
    # Group by 'player_of_match' and count occurrences
    data = matches.groupby("player_of_match").size().sort_values(ascending=False)
    data = data.reset_index()
    data.columns = ['Player_name', 'Man of Match']
    data.reset_index(drop=True, inplace=True)
    data.index = data.index + 1  # Adjust the index to start from 1
   
    return data.head(10)
def season_wise_top_man_of_match(matches, season):
    # Filter data for the selected season and group by 'player_of_match'
    data1 = matches[matches['season'] == season].groupby("player_of_match").size().sort_values(ascending=False)

    # Convert the result to a DataFrame
    data1 = data1.reset_index()

    # Rename the columns for clarity
    data1.columns = ['Player_name', 'Man of Match']

    # Reset the index and make it start from 1
    data1.reset_index(drop=True, inplace=True)
    data1.index = data1.index + 1  # Adjust the index to start from 1

    # Return the top 5 players for the selected season
    return data1.head(5)





################################################################ team performace #################################################################


def played_matches(data):
# Group by 'team1', 'team2', and 'winner' to get the counts of matches played
    team1 = data.groupby('team1').size()
    team2 = data.groupby('team2').size()
    winner = data.groupby('winner').size()

# Combine the counts of matches played by each team
    team = team1.add(team2, fill_value=0)  # Use add to ensure NaN values are handled

# Create a final DataFrame with the team matches and wins
    final_df = pd.concat([team, winner], axis=1).reset_index()

# Rename the columns for clarity
    final_df.columns = ['Team', 'Matches Played', 'Wins']
    final_df.index += 1
# Display the result
    return final_df


def team1_vs_team2(team1, team2, data):
    # Filter head-to-head matches
    h2h_matches = data[
        ((data['team1'] == team1) & (data['team2'] == team2)) |
        ((data['team1'] == team2) & (data['team2'] == team1))
    ]

    # Count matches and results
    total_matches = len(h2h_matches)
    team1_wins = len(h2h_matches[h2h_matches['winner'] == team1])
    team2_wins = len(h2h_matches[h2h_matches['winner'] == team2])

    # Handle scenarios with no matches
    if total_matches == 0:
        return {
            'Total Matches': 0,
            f'{team1} Wins': 0,
            f'{team1} Losses': 0,
            f'{team2} Wins': 0,
            f'{team2} Losses': 0
        }

    return {
        'Total Matches': total_matches,
        f'{team1} Wins': team1_wins,
        f'{team1} Losses': team2_wins,
        f'{team2} Wins': team2_wins,
        f'{team2} Losses': team1_wins
    }

    
def season_team_performance(data, season):
    # Filter matches by the specified season
    season_matches = data[data['season'] == season]
    
    # Calculate matches played by each team
    team_matches_played = season_matches.groupby('team1')['team1'].count() + \
                          season_matches.groupby('team2')['team2'].count()

    # Calculate wins by each team
    team_wins = season_matches.groupby('winner')['winner'].count()

    # Create standings DataFrame
    standings_df = pd.DataFrame({
        'Team': team_wins.index,
        'Matches': team_matches_played,
        'Wins': team_wins
    })

    # Calculate losses (Matches - Wins)
    standings_df['Losses'] = standings_df['Matches'] - standings_df['Wins']

    # Calculate points (adjust based on IPL scoring rules, 2 points per win)
    standings_df['Points'] = standings_df['Wins'] * 2

    # Sort by points and wins in descending order
    standings_df = standings_df.sort_values(by=['Points', 'Wins'], ascending=False)

    # Assign ranks
    standings_df['Rank'] = range(1, len(standings_df) + 1)
    
    # Filter for final match of the specified season
    Final_Winner = data[(data['match_type'] == 'Final') & (data['season'] == season)]
    
    # Extract team1, team2, and winner from final match
    team_1 = Final_Winner['team1']
    team_2 = Final_Winner['team2']
    winner = Final_Winner['winner']

    return standings_df, team_1, team_2, winner

def calculate_team_performance(matches):
    # Total matches played by each team
    total_matches_played = matches.groupby(['team1']).size() + matches.groupby(['team2']).size()

    # Total toss wins for each team
    toss_wins = matches.groupby('toss_winner').size()

    # Total match wins after winning the toss
    match_wins_after_toss = matches[matches['toss_winner'] == matches['winner']].groupby('toss_winner').size()

    # Total matches played after winning the toss (equivalent to toss wins)
    matches_played_after_toss_win = toss_wins

    # Total losses after winning the toss
    match_losses_after_toss = matches_played_after_toss_win - match_wins_after_toss

    # Calculate the win percentage after toss
    win_percentage_after_toss = (match_wins_after_toss / toss_wins) * 100

    # Combine all into a DataFrame
    team_performance_df = pd.DataFrame({
        'Matches Played': total_matches_played,
        'Toss Wins': toss_wins,
        'Match Wins After Toss Win': match_wins_after_toss,
        'Match Losses After WIN': match_losses_after_toss,
        'Win Percentage After Toss Win': win_percentage_after_toss
    }).fillna(0)  # Replace NaN with 0 for missing data

    # Reset the index for display
    team_performance_df.reset_index(inplace=True)
    team_performance_df.rename(columns={'index': 'Team'}, inplace=True)

    # Sort by Matches Played for better clarity
    team_performance_df = team_performance_df.sort_values(by='Matches Played', ascending=False)

    # Optional: Increment numeric columns if needed
    numeric_columns = ['Matches Played', 'Toss Wins', 'Match Wins After Toss Win', 'Match Losses After WIN', 'Win Percentage After Toss Win']
    team_performance_df[numeric_columns] += 1

    return team_performance_df



#########################################player_performance####################################################

def player_performance(data, selected_player):
    # Batting Stats
    batter_data = data[data['batter'] == selected_player]
    matches_played = batter_data['match_id'].nunique()
    total_runs = batter_data['batsman_runs'].sum()
    total_balls_faced = batter_data['ball'].count()
    average = round(total_runs / batter_data['is_wicket'].sum() if batter_data['is_wicket'].sum() > 0 else 0, 2)  # Batting average
    strike_rate = round((total_runs / total_balls_faced) * 100 if total_balls_faced > 0 else 0, 2)  # Batting strike rate
    
    # Bowling Stats
    bowler_data = data[data['bowler'] == selected_player]
    total_wickets = bowler_data['is_wicket'].sum()  # Assuming 'is_wicket' indicates if the bowler took a wicket
    total_balls_bowled = bowler_data['ball'].count()
    bowling_average = round(bowler_data['batsman_runs'].sum() / total_wickets if total_wickets > 0 else 0, 2)  # Bowling average
    economy_rate = round((bowler_data['batsman_runs'].sum() / total_balls_bowled) * 6 if total_balls_bowled > 0 else 0, 2)  # Economy rate

    return {
        'Matches_played': matches_played,
        'Total_runs': total_runs,
        'average': average,
        'strike_rate': strike_rate,
        'Total_wickets': total_wickets,
        'bowling_average': bowling_average,
        'economy_rate': economy_rate
    }
def player_performance_seasonwise(data, selected_player):
    # Filter data for the selected player (both batting and bowling)
    player_batting_data = data[data['batter'] == selected_player]
    player_bowling_data = data[data['bowler'] == selected_player]
    
    # Group by 'season' and aggregate the batting performance stats
    season_stats_batting = player_batting_data.groupby('season').agg(
        total_runs=('batsman_runs', 'sum'),
        total_balls_faced=('ball', 'count'),  # We need the total balls faced for strike rate calculation
        total_matches_played=('match_id', 'nunique')  # Count the unique matches played
    ).reset_index()

    # Calculate strike rate (total runs / total balls faced) and round it to 2 decimal places
    season_stats_batting['strike_rate'] = season_stats_batting.apply(
        lambda x: round((x['total_runs'] / x['total_balls_faced']) * 100, 2) if x['total_balls_faced'] > 0 else 0, axis=1
    )

    # Group by 'season' and aggregate the bowling performance stats
    season_stats_bowling = player_bowling_data.groupby('season').agg(
        total_wickets=('is_wicket', 'sum'),
        total_balls_bowled=('ball', 'count'),
        total_runs_conceded=('batsman_runs', 'sum'),
        total_matches_played=('match_id', 'nunique')  # Count the unique matches played in bowling data
    ).reset_index()

    # Calculate economy rate and round it to 2 decimal places
    season_stats_bowling['economy_rate'] = season_stats_bowling.apply(
        lambda x: round((x['total_runs_conceded'] / x['total_balls_bowled']) * 6, 2) if x['total_balls_bowled'] > 0 else 0, axis=1
    )

    # Merge both batting and bowling stats on 'season'
    season_stats = pd.merge(season_stats_batting[['season', 'total_runs', 'strike_rate', 'total_matches_played']], 
                             season_stats_bowling[['season', 'total_wickets', 'economy_rate', 'total_matches_played']], 
                             on='season', how='outer')

    # Ensure that the total matches played is the maximum value from both batting and bowling stats
    season_stats['total_matches_played'] = season_stats[['total_matches_played_x', 'total_matches_played_y']].max(axis=1)
    
    # Drop the extra columns from the merge
    season_stats = season_stats.drop(columns=['total_matches_played_x', 'total_matches_played_y'])

    return season_stats



#---------------------------------------venue--------------------------------------------------------------------------------------------


def overall_venue(data,selected_venue):
    
       venue_data = data[data['venue'] == selected_venue]
        # Total matches played at the selected venue
       total_matches = venue_data['match_id'].nunique()
       
        # Success rate of batting first vs. chasing teams
       # Success rate of batting first vs. chasing teams
       batting_first_wins = venue_data[venue_data['result'] == 'runs']['match_id'].nunique()
       chasing_wins = venue_data[venue_data['result'] == 'wickets']['match_id'].nunique()
       
       #calculate sucees rate
       batting_first_succes_rate= round((batting_first_wins/total_matches)*100,2 )if total_matches >0  else 0 
       chasing_success_rate = round((chasing_wins / total_matches) * 100, 2) if total_matches > 0 else 0  
       
       
       
       return total_matches, batting_first_succes_rate, chasing_success_rate 
   
def most_runs_and_wicket_venue(data, selected_venue):
    # Filter data for the selected venue
    venue_data = data[data['venue'] == selected_venue]

    # Calculate total runs scored by each player
    player_runs = (
        venue_data.groupby('batter')['batsman_runs']
        .sum()
        .reset_index()
        .sort_values(by='batsman_runs', ascending=False)
        .head(5)
        .reset_index(drop=True)  # Reset the index
    )
    player_runs.index += 1  # Start index from 1

    # Calculate total wickets taken by each bowler
    most_wickets = (
        venue_data[venue_data['is_wicket'] == 1]
        .groupby('bowler')
        .size()
        .reset_index(name='Wickets')
        .sort_values(by='Wickets', ascending=False)
        .head(5)
        .reset_index(drop=True)  # Reset the index
    )
    most_wickets.index += 1  # Start index from 1

    return player_runs, most_wickets

def highest_scores(data, selected_venue):
    # Filter data for the selected venue
    venue_data = data[data['venue'] == selected_venue]
    
    # Group by venue, match_id, inning, batting_team, and bowling_team to calculate total runs
    inning_scores = (
        venue_data.groupby(['venue', 'match_id', 'inning', 'batting_team', 'bowling_team'])['total_runs']
        .sum()
        .reset_index()
    )
    
    # Find the row with the highest score for the selected venue
    highest_scores = (
        inning_scores.loc[inning_scores.groupby('venue')['total_runs'].idxmax()]
        .rename(columns={'total_runs': 'Highest_Score'})
    )
    
    # Select the relevant columns
    highest_scores = highest_scores[['venue', 'batting_team', 'bowling_team', 'Highest_Score']]
    
    # Extract data as lists
    venues = highest_scores['venue'].tolist()
    batting_teams = highest_scores['batting_team'].tolist()
    bowling_teams = highest_scores['bowling_team'].tolist()
    highest_scores_values = highest_scores['Highest_Score'].tolist()
    
    return venues, batting_teams, bowling_teams, highest_scores_values


def lowest_scores(data, selected_venue):
    # Filter data for the selected venue
    venue_data = data[data['venue'] == selected_venue]
    
    # Group by venue, match_id, inning, batting_team, and bowling_team to calculate total runs
    inning_scores = (
        venue_data.groupby(['venue', 'match_id', 'inning', 'batting_team', 'bowling_team'])['total_runs']
        .sum()
        .reset_index()
    )
    
    # Find the row with the lowest score for the selected venue
    lowest_scores = (
        inning_scores.loc[inning_scores.groupby('venue')['total_runs'].idxmin()]
        .rename(columns={'total_runs': 'Lowest_Score'})
    )
    
    # Select the relevant columns
    lowest_scores = lowest_scores[['venue', 'batting_team', 'bowling_team', 'Lowest_Score']]
    
    # Extract data as lists
    venues = lowest_scores['venue'].tolist()
    batting_teams = lowest_scores['batting_team'].tolist()
    bowling_teams = lowest_scores['bowling_team'].tolist()
    lowest_scores_values = lowest_scores['Lowest_Score'].tolist()
    
    return venues, batting_teams, bowling_teams, lowest_scores_values 

 
def score_intervals(data, selected_venue, bins=[0, 50, 100, 150, 200, 250, 300]):
    venue_data = data[data['venue'] == selected_venue]
    inning_scores = (
        venue_data.groupby(['match_id', 'inning'])['total_runs']
        .sum()
        .reset_index()
    )
    interval_counts = pd.cut(inning_scores['total_runs'], bins=bins, right=False).value_counts().sort_index()
    interval_df = interval_counts.reset_index()
    interval_df.columns = ['Score Range', 'Frequency']
    
    # Convert Interval objects to "X to Y" format
    interval_df['Score Range'] = interval_df['Score Range'].apply(lambda x: f"{x.left} to {x.right - 1}")
    return interval_df

