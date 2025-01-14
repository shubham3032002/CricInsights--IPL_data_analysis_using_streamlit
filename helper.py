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
