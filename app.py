import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as ex
import plotly.figure_factory as ff
import helper
import preprocessing
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.graph_objects as go

data=preprocessing.preprocessing()
match_data=preprocessing.matches_data()

st.sidebar.title("IPL Data Analysis")

option = st.sidebar.radio(
    'Select an analysis type:',
    ['Overview', 'Team Performance', 'Player Performance', 'Venue Analysis']
)

if option == 'Overview':
    st.title('Yearwise Champion')
    
    # Call the helper function to get yearwise champions
    final_matches = helper.yearwise_champion(match_data)
    
    # Display the data in a table format with controlled width
    # Use st.dataframe with use_container_width to make it full width
    st.dataframe(final_matches, use_container_width=True)
    
  
    st.title('Champion Count')

# Call the helper function to get champion count
    champion_count = helper.count_of_champion(match_data)

# Define a custom color map for teams
    team_colors = {
    'Chennai Super Kings': 'yellow',   # Fixed color name
    'Deccan Chargers': 'blue',
    'Gujarat Titans': 'darkblue',
    'Kolkata Knight Riders': 'purple',
    'Mumbai Indians': 'skyblue',
    'Rajasthan Royals': 'pink',
    'Sunrisers Hyderabad': 'darkorange'
    # Add more teams and colors as needed
    }

# Create a bar chart using Plotly with custom colors
    fig = ex.bar(
    champion_count,  
    y='Count', 
    color='Winner', 
    color_discrete_map=team_colors  # Set custom color map
    )

# Update the layout of the plot
    fig.update_layout(
    title='Number of Championships Won', 
    xaxis_title='Team', 
    yaxis_title='Champion Count'
    )

# Display the plot
    st.plotly_chart(fig)


    st.title('Top 10 Batters and Average')

    top_10 = helper.top_batter(data)

# Display the result in an interactive table
    st.dataframe(top_10, use_container_width=True)
    st.title('Top 10 Blower')

    top_10_blower = helper.top_10_blower(data)
    st.dataframe(top_10_blower, use_container_width=True)


    st.title("Top 10 Players with Most 'Man of the Match' Awards Across All Seasons")

# Get the top 10 players using the helper function
    top_10 =helper.top_10_man_of_match(match_data)


# Display the top 10 players dataframe
    st.markdown("### Season-Wise Top Performance")

    season = ['2007/08', '2009', '2009/10', '2011', '2012', '2013', '2014',
          '2015', '2016', '2017', '2018', '2019', '2020/21', '2021', '2022',
          '2023', '2024']

# Dropdown to select the season
    selected_season = st.selectbox("Select Season", season)

# Call the helper functions for season-wise top 'Man of the Match' and bowlers
    man_of_match = helper.season_wise_top_man_of_match(match_data, selected_season)
    bowler_stats = helper.season_wise_top_bowler(data, selected_season)
    batter_stats=helper.season_wise_top_batter(data,selected_season)

# Display the top 5 players with most 'Man of the Match' awards
    st.markdown("#### Top 5 Players with Most 'Man of the Match' Awards")
    st.dataframe(man_of_match, use_container_width=True)

# Display the top 5 bowlers with most matches played and wickets taken
    st.markdown("#### Top 5 Bowlers with Most Matches Played and Wickets Taken")
    st.dataframe(bowler_stats, use_container_width=True)
    st.markdown("#### Top 5 Batter with Most Matches Played and Runs")
    st.dataframe(batter_stats, use_container_width=True)
    
    
    
    
    
if option == "Team Performance":
    # Title for Team Performance
    st.markdown('### Total Matches Played and Wins by Each Team')

    # Matches played and wins
    match_played = helper.played_matches(match_data)
    st.dataframe(match_played, use_container_width=True)

    # Head-to-Head Stats
    st.markdown("## Head-to-Head Statistics Between Two Teams")

    # List of teams
    teams = [
        'Chennai Super Kings', 'Deccan Chargers', 'Delhi Capitals',
        'Delhi Daredevils', 'Gujarat Lions', 'Gujarat Titans',
        'Kings XI Punjab', 'Kochi Tuskers Kerala', 'Kolkata Knight Riders',
        'Lucknow Super Giants', 'Mumbai Indians', 'Pune Warriors',
        'Punjab Kings', 'Rajasthan Royals', 'Rising Pune Supergiant',
        'Rising Pune Supergiants', 'Royal Challengers Bangalore',
        'Royal Challengers Bengaluru', 'Sunrisers Hyderabad'
    ]

    # Team Selection
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        team1 = st.selectbox("Select Team 1", teams)

    with col2:
        st.markdown("<h3 style='text-align: center;'>vs</h3>", unsafe_allow_html=True)

    with col3:
        team2 = st.selectbox("Select Team 2", teams)

    # Ensure different teams are selected
    if team1 == team2:
        st.warning("Please select two different teams.")
    else:
        # Fetch head-to-head stats
        h2h_stats = helper.team1_vs_team2(team1, team2, match_data)

        # Convert stats to DataFrame for display
        head_to_head_df = pd.DataFrame({
            "Statistic": [
                "Total Matches Played",
                f"{team1} Wins",
                f"{team1} Losses",
                f"{team2} Wins",
                f"{team2} Losses"
            ],
            "Value": [
                h2h_stats['Total Matches'],
                h2h_stats[f'{team1} Wins'],
                h2h_stats[f'{team1} Losses'],
                h2h_stats[f'{team2} Wins'],
                h2h_stats[f'{team2} Losses']
            ]
        })

        # Display the results
        st.markdown("### Head-to-Head Results")
        st.table(head_to_head_df)

    # Season Performance
    st.markdown("### Season-Wise Performance of All Teams")
    season = ['2007/08', '2009', '2009/10', '2011', '2012', '2013', '2014',
              '2015', '2016', '2017', '2018', '2019', '2020/21', '2021', '2022',
              '2023', '2024']

    selected_season = st.selectbox("Select Season", season)

    standings_df, team_1, team_2, winner = helper.season_team_performance(match_data, selected_season)
    
    # Display standings
    st.dataframe(standings_df, use_container_width=True)

    # Display final match details
    st.markdown("### Season Final Match")
    if not team_1.empty and not team_2.empty and not winner.empty:
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.markdown(f"**{team_1.iloc[0]}**")

        with col2:
            st.markdown("<h3 style='text-align: center;'>vs</h3>", unsafe_allow_html=True)

        with col3:
            st.markdown(f"**{team_2.iloc[0]}**")

        st.markdown(f"<h3 style='text-align: center;'>The {selected_season} Season Winner is **{winner.iloc[0]}**</h3>", unsafe_allow_html=True)
    else:
        st.warning("No final match details available for the selected season.")
        
    # Team Performance Analysis
    st.title("Team Match Win after toss win")
    team_performance_df = helper.calculate_team_performance(match_data)

    # Dropdown to select a team
    team_names = team_performance_df['Team'].unique()
    selected_team = st.selectbox("Select a Team", team_names)

    # Filter the data for the selected team
    team_data = team_performance_df[team_performance_df['Team'] == selected_team]

    # Check if the selected team has any data to display
    if not team_data.empty:
        # Data to be visualized
        matches_played = team_data['Matches Played'].values[0]
        toss_wins = team_data['Toss Wins'].values[0]
        match_wins_after_toss = team_data['Match Wins After Toss Win'].values[0]
        match_losses_after_toss = team_data['Match Losses After WIN'].values[0]
        win_percentage_after_toss = team_data['Win Percentage After Toss Win'].values[0]
    
        # Prepare data for plotting
        performance_data = {
            'Matches Played': matches_played,
            'Toss Wins': toss_wins,
            'Match Wins After Toss Win': match_wins_after_toss,
            'Match Losses After WIN': match_losses_after_toss,
            'Win Percentage After Toss Win': win_percentage_after_toss
        }

        # Plotting the data using matplotlib
        st.dataframe(performance_data, use_container_width=True)