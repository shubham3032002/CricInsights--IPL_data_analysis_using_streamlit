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

# Adding IPL Logo and Title in Sidebar
st.markdown(
    """
    <div style="background-color: #1a1a1a; padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);">
        <h1 style="color: #ffffff; font-size: 34px; font-family: 'Arial', sans-serif; margin: 0;">Cric<span style="color: #ff6600;">Insights</span></h1>
        <p style="color: #cccccc; font-size: 16px; font-family: 'Arial', sans-serif; margin-top: 8px;">Dive into IPL analytics with a modern twist</p>
    </div>
    """,
    unsafe_allow_html=True
)




st.sidebar.markdown(
    """
    <div style="text-align: center; padding: 10px;">
        <h1 style="color: white; font-size: 24px; margin-top: 10px;">IPL Data Analysis</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.image('https://parimatchnews.com/wp-content/uploads/2020/10/2010-12.jpg')
option = st.sidebar.radio(
    'Select an analysis type:',
    ['📊 Overview', '🚩 Team Performance', '🌟 Player Performance','🏏 Batter vs ⚾ Bowler', 'Venue Analysis']
)

if option == '📊 Overview':
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
    
    
    
    
    
if option == "🚩 Team Performance":
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
        
        
if option == "🌟 Player Performance":
    st.markdown("### Player statistics")
    list_of_the_players= ['A Ashish Reddy', 'A Badoni', 'A Chandila', 'A Chopra',
       'A Choudhary', 'A Dananjaya', 'A Flintoff', 'A Kamboj', 'A Kumble',
       'A Manohar', 'A Mishra', 'A Mithun', 'A Mukund', 'A Nehra',
       'A Nel', 'A Nortje', 'A Raghuvanshi', 'A Singh', 'A Symonds',
       'A Tomar', 'A Uniyal', 'A Zampa', 'AA Bilakhia', 'AA Chavan',
       'AA Jhunjhunwala', 'AA Kazi', 'AA Kulkarni', 'AA Noffke',
       'AB Agarkar', 'AB Barath', 'AB Dinda', 'AB McDonald',
       'AB de Villiers', 'AC Blizzard', 'AC Gilchrist', 'AC Thomas',
       'AC Voges', 'AD Hales', 'AD Mascarenhas', 'AD Mathews', 'AD Nath',
       'AD Russell', 'AF Milne', 'AG Murtaza', 'AG Paunikar', 'AJ Finch',
       'AJ Hosein', 'AJ Turner', 'AJ Tye', 'AK Markram', 'AL Menaria',
       'AM Nayar', 'AM Rahane', 'AM Salvi', 'AN Ahmed', 'AN Ghosh',
       'AP Dole', 'AP Majumdar', 'AP Tare', 'AR Bawne', 'AR Patel',
       'AS Joseph', 'AS Rajpoot', 'AS Raut', 'AS Roy', 'AS Yadav',
       'AT Carey', 'AT Rayudu', 'AU Rashid', 'AUK Pathan', 'Abdul Basith',
       'Abdul Samad', 'Abdur Razzak', 'Abhishek Sharma', 'Abishek Porel',
       'Akash Deep', 'Akash Madhwal', 'Akash Singh', 'Aman Hakim Khan',
       'Anand Rajan', 'Anirudh Singh', 'Ankit Sharma', 'Ankit Soni',
       'Anmolpreet Singh', 'Anuj Rawat', 'Anureet Singh',
       'Arjun Tendulkar', 'Arshad Khan', 'Arshad Khan (2)',
       'Arshdeep Singh', 'Ashutosh Sharma', 'Atharva Taide', 'Avesh Khan',
       'Azhar Mahmood', 'Azmatullah Omarzai', 'B Akhil', 'B Chipli',
       'B Geeves', 'B Indrajith', 'B Kumar', 'B Laughlin', 'B Lee',
       'B Sai Sudharsan', 'B Stanlake', 'B Sumanth', 'BA Bhatt',
       'BA Stokes', 'BAW Mendis', 'BB McCullum', 'BB Samantray',
       'BB Sran', 'BCJ Cutting', 'BE Hendricks', 'BJ Haddin', 'BJ Hodge',
       'BJ Rohrer', 'BMAJ Mendis', 'BR Dunk', 'BR Sharath',
       'BW Hilfenhaus', 'Basil Thampi', 'Bipul Sharma', 'C Ganapathy',
       'C Green', 'C Madan', 'C Munro', 'C Nanda', 'C Sakariya',
       'C de Grandhomme', 'CA Ingram', 'CA Lynn', 'CA Pujara', 'CH Gayle',
       'CH Morris', 'CJ Anderson', 'CJ Dala', 'CJ Ferguson', 'CJ Green',
       'CJ Jordan', 'CJ McKay', 'CK Kapugedera', 'CK Langeveldt',
       'CL White', 'CM Gautam', 'CR Brathwaite', 'CR Woakes',
       'CRD Fernando', 'CV Varun', 'D Brevis', 'D Ferreira', 'D Jansen',
       'D Kalyankrishna', 'D Padikkal', 'D Pretorius', 'D Salunkhe',
       'D Wiese', 'D du Preez', 'DA Miller', 'DA Warner', 'DAJ Bracewell',
       'DB Das', 'DB Ravi Teja', 'DE Bollinger', 'DG Nalkande',
       'DH Yagnik', 'DJ Bravo', 'DJ Harris', 'DJ Hooda', 'DJ Hussey',
       'DJ Jacobs', 'DJ Malan', 'DJ Mitchell', 'DJ Muthuswami',
       'DJ Thornely', 'DJ Willey', 'DJG Sammy', 'DJM Short', 'DL Chahar',
       'DL Vettori', 'DM Bravo', 'DNT Zoysa', 'DP Conway', 'DP Nannes',
       'DP Vijaykumar', 'DPMD Jayawardene', 'DR Martyn', 'DR Sams',
       'DR Shorey', 'DR Smith', 'DS Kulkarni', 'DS Lehmann',
       'DT Christian', 'DT Patil', 'DW Steyn', 'Dhruv Jurel', 'E Lewis',
       'EJG Morgan', 'ER Dwivedi', 'F Behardien', 'F du Plessis',
       'FA Allen', 'FH Edwards', 'FY Fazal', 'Fazalhaq Farooqi',
       'G Coetzee', 'G Gambhir', 'GB Hogg', 'GC Smith', 'GC Viljoen',
       'GD McGrath', 'GD Phillips', 'GH Vihari', 'GHS Garton',
       'GJ Bailey', 'GJ Maxwell', 'GR Napier', 'GS Sandhu',
       'Gagandeep Singh', 'Gulbadin Naib', 'Gurkeerat Singh',
       'Gurnoor Brar', 'H Das', 'H Klaasen', 'H Sharma', 'HC Brook',
       'HE van der Dussen', 'HF Gurney', 'HH Gibbs', 'HH Pandya',
       'HM Amla', 'HR Shokeen', 'HV Patel', 'Harbhajan Singh',
       'Harmeet Singh', 'Harpreet Brar', 'Harpreet Singh', 'Harshit Rana',
       'I Malhotra', 'I Sharma', 'I Udana', 'IC Pandey', 'IC Porel',
       'IK Pathan', 'IR Jaggi', 'IS Sodhi', 'Imran Tahir',
       'Iqbal Abdulla', 'Ishan Kishan', 'J Arunkumar', 'J Botha',
       'J Fraser-McGurk', 'J Little', 'J Suchith', 'J Syed Mohammad',
       'J Theron', 'J Yadav', 'JA Morkel', 'JA Richardson', 'JC Archer',
       'JC Buttler', 'JD Ryder', 'JD Unadkat', 'JDP Oram', 'JDS Neesham',
       'JE Root', 'JE Taylor', 'JEC Franklin', 'JH Kallis', 'JJ Bumrah',
       'JJ Roy', 'JJ van der Wath', 'JL Denly', 'JL Pattinson',
       'JM Bairstow', 'JM Kemp', 'JM Sharma', 'JO Holder',
       'JP Behrendorff', 'JP Duminy', 'JP Faulkner',
       'JPR Scantlebury-Searles', 'JR Hazlewood', 'JR Hopes',
       'JR Philippe', 'JW Hastings', 'Jalaj S Saxena', 'Jaskaran Singh',
       'Joginder Sharma', 'K Goel', 'K Gowtham', 'K Kartikeya',
       'K Khejroliya', 'K Rabada', 'K Santokie', 'K Upadhyay', 'K Yadav',
       'KA Jamieson', 'KA Maharaj', 'KA Pollard', 'KAJ Roach',
       'KB Arun Karthik', 'KC Cariappa', 'KC Sangakkara', 'KD Karthik',
       'KH Pandya', 'KJ Abbott', 'KK Ahmed', 'KK Cooper', 'KK Nair',
       'KL Nagarkoti', 'KL Rahul', 'KM Asif', 'KM Jadhav', 'KMA Paul',
       'KMDN Kulasekara', 'KP Appanna', 'KP Pietersen', 'KR Mayers',
       'KR Sen', 'KS Bharat', 'KS Sharma', 'KS Williamson', 'KT Maphaka',
       'KV Sharma', 'KW Richardson', 'Kamran Akmal', 'Kamran Khan',
       'Karanveer Singh', 'Kartik Tyagi', 'Kuldeep Yadav',
       'Kumar Kushagra', 'L Ablish', 'L Balaji', 'L Ngidi', 'L Ronchi',
       'L Wood', 'LA Carseldine', 'LA Pomersbach', 'LB Williams',
       'LE Plunkett', 'LH Ferguson', 'LI Meriwala', 'LJ Wright',
       'LMP Simmons', 'LPC Silva', 'LR Shukla', 'LRPL Taylor',
       'LS Livingstone', 'Lalit Yadav', 'Liton Das', 'M Ashwin',
       'M Jansen', 'M Kaif', 'M Kartik', 'M Klinger', 'M Manhas',
       'M Markande', 'M Morkel', 'M Muralitharan', 'M Ntini',
       'M Pathirana', 'M Prasidh Krishna', 'M Rawat', 'M Shahrukh Khan',
       'M Siddharth', 'M Theekshana', 'M Vijay', 'M Vohra', 'M de Lange',
       'MA Agarwal', 'MA Khote', 'MA Starc', 'MA Wood', 'MB Parmar',
       'MC Henriques', 'MC Juneja', 'MD Mishra', 'MD Shanaka',
       'MDKJ Perera', 'MEK Hussey', 'MF Maharoof', 'MG Bracewell',
       'MG Johnson', 'MG Neser', 'MJ Clarke', 'MJ Guptill', 'MJ Henry',
       'MJ Lumb', 'MJ McClenaghan', 'MJ Santner', 'MJ Suthar',
       'MK Lomror', 'MK Pandey', 'MK Tiwary', 'ML Hayden', 'MM Ali',
       'MM Patel', 'MM Sharma', 'MN Samuels', 'MN van Wyk', 'MP Stoinis',
       'MP Yadav', 'MR Marsh', 'MS Bisla', 'MS Dhoni', 'MS Gony',
       'MS Wade', 'MV Boucher', 'MW Short', 'Mandeep Singh',
       'Mashrafe Mortaza', 'Mayank Dagar', 'Misbah-ul-Haq',
       'Mohammad Ashraful', 'Mohammad Asif', 'Mohammad Hafeez',
       'Mohammad Nabi', 'Mohammed Shami', 'Mohammed Siraj',
       'Mohit Rathee', 'Mohsin Khan', 'Monu Kumar', 'Mujeeb Ur Rahman',
       'Mukesh Choudhary', 'Mukesh Kumar', 'Mustafizur Rahman',
       'N Burger', 'N Jagadeesan', 'N Pooran', 'N Rana', 'N Saini',
       'N Thushara', 'N Wadhera', 'NA Saini', 'NB Singh', 'ND Doshi',
       'NJ Maddinson', 'NJ Rimmington', 'NK Patel', 'NL McCullum',
       'NLTC Perera', 'NM Coulter-Nile', 'NS Naik', 'NT Ellis', 'NV Ojha',
       'Naman Dhir', 'Navdeep Saini', 'Naveen-ul-Haq',
       'Nithish Kumar Reddy', 'Noor Ahmad', 'O Thomas', 'OA Shah',
       'OC McCoy', 'OF Smith', 'P Amarnath', 'P Awana', 'P Chopra',
       'P Dogra', 'P Dubey', 'P Kumar', 'P Negi', 'P Parameswaran',
       'P Prasanth', 'P Ray Barman', 'P Sahu', 'P Simran Singh',
       'P Suyal', 'PA Patel', 'PA Reddy', 'PBB Rajapaksa', 'PC Valthaty',
       'PD Collingwood', 'PD Salt', 'PH Solanki', 'PJ Cummins',
       'PJ Sangwan', 'PK Garg', 'PM Sarvesh Kumar', 'PN Mankad',
       'PP Chawla', 'PP Ojha', 'PP Shaw', 'PR Shah', 'PSP Handscomb',
       'PV Tambe', 'PVD Chameera', 'PWH de Silva', 'Pankaj Singh',
       'Parvez Rasool', 'Q de Kock', 'R Ashwin', 'R Bhatia', 'R Bishnoi',
       'R Dhawan', 'R Dravid', 'R Goyal', 'R McLaren', 'R Ninan',
       'R Parag', 'R Powell', 'R Rampaul', 'R Ravindra', 'R Sai Kishore',
       'R Sanjay Yadav', 'R Sathish', 'R Sharma', 'R Shepherd',
       'R Shukla', 'R Tewatia', 'R Vinay Kumar', 'RA Bawa', 'RA Jadeja',
       'RA Shaikh', 'RA Tripathi', 'RD Chahar', 'RD Gaikwad', 'RE Levi',
       'RE van der Merwe', 'RG More', 'RG Sharma', 'RJ Gleeson',
       'RJ Harris', 'RJ Peterson', 'RJ Quiney', 'RJW Topley', 'RK Bhui',
       'RK Singh', 'RM Patidar', 'RN ten Doeschate', 'RP Meredith',
       'RP Singh', 'RR Bhatkal', 'RR Bose', 'RR Pant', 'RR Powar',
       'RR Raje', 'RR Rossouw', 'RR Sarwan', 'RS Bopara', 'RS Gavaskar',
       'RS Hangargekar', 'RS Sodhi', 'RT Ponting', 'RV Gomez', 'RV Patel',
       'RV Uthappa', 'RW Price', 'Rahmanullah Gurbaz', 'Ramandeep Singh',
       'Rashid Khan', 'Rasikh Salam', 'Ravi Bishnoi', 'S Anirudha',
       'S Aravind', 'S Badree', 'S Badrinath', 'S Chanderpaul',
       'S Dhawan', 'S Dube', 'S Gopal', 'S Joseph', 'S Kaul', 'S Kaushik',
       'S Ladda', 'S Lamichhane', 'S Midhun', 'S Nadeem', 'S Narwal',
       'S Rana', 'S Randiv', 'S Sandeep Warrier', 'S Sohal',
       'S Sreesanth', 'S Sriram', 'S Tyagi', 'S Vidyut', 'SA Abbott',
       'SA Asnodkar', 'SA Yadav', 'SB Bangar', 'SB Dubey', 'SB Jakati',
       'SB Joshi', 'SB Styris', 'SB Wagh', 'SC Ganguly', 'SC Kuggeleijn',
       'SD Chitnis', 'SD Hope', 'SD Lad', 'SE Bond', 'SE Marsh',
       'SE Rutherford', 'SH Johnson', 'SJ Srivastava', 'SK Raina',
       'SK Trivedi', 'SK Warne', 'SL Malinga', 'SM Boland', 'SM Curran',
       'SM Harwood', 'SM Katich', 'SM Pollock', 'SMSM Senanayake',
       'SN Khan', 'SN Thakur', 'SO Hetmyer', 'SP Fleming', 'SP Goswami',
       'SP Jackson', 'SP Narine', 'SPD Smith', 'SR Tendulkar',
       'SR Watson', 'SS Agarwal', 'SS Cottrell', 'SS Iyer', 'SS Mundhe',
       'SS Prabhudessai', 'SS Sarkar', 'SS Shaikh', 'SS Tiwary',
       'SSB Magala', 'ST Jayasuriya', 'STR Binny', 'SV Samson',
       'SW Billings', 'SW Tait', 'SZ Mulani', 'Sachin Baby',
       'Salman Butt', 'Sameer Rizvi', 'Sandeep Sharma', 'Sanvir Singh',
       'Saurav Chauhan', 'Shahbaz Ahmed', 'Shahid Afridi',
       'Shakib Al Hasan', 'Shashank Singh', 'Shivam Mavi',
       'Shivam Sharma', 'Shivam Singh', 'Shoaib Ahmed', 'Shoaib Akhtar',
       'Shoaib Malik', 'Shubman Gill', 'Sikandar Raza', 'Simarjeet Singh',
       'Sohail Tanvir', 'Sumit Kumar', 'Sunny Gupta', 'Sunny Singh',
       'Suyash Sharma', 'Swapnil Singh', 'T Banton', 'T Henderson',
       'T Kohler-Cadmore', 'T Kohli', 'T Natarajan', 'T Shamsi',
       'T Stubbs', 'T Taibu', 'T Thushara', 'TA Boult', 'TD Paine',
       'TG Southee', 'TH David', 'TK Curran', 'TL Seifert', 'TL Suman',
       'TM Dilshan', 'TM Head', 'TM Srivastava', 'TP Sudhindra',
       'TR Birt', 'TS Mills', 'TU Deshpande', 'Tanush Kotian',
       'Tejas Baroka', 'Tilak Varma', 'U Kaul', 'UA Birla', 'UBT Chand',
       'UT Khawaja', 'UT Yadav', 'Umar Gul', 'Umran Malik', 'V Kaverappa',
       'V Kohli', 'V Pratap Singh', 'V Sehwag', 'V Shankar',
       'V Viyaskanth', 'VG Arora', 'VH Zol', 'VR Aaron', 'VR Iyer',
       'VRV Singh', 'VS Malik', 'VS Yeligati', 'VVS Laxman', 'VY Mahesh',
       'Vijaykumar Vyshak', 'Virat Singh', 'Vishnu Vinod',
       'Vivrant Sharma', 'W Jaffer', 'WA Mota', 'WD Parnell', 'WG Jacks',
       'WP Saha', 'WPUJC Vaas', 'Washington Sundar',
       'X Thalaivan Sargunam', 'Y Gnaneswara Rao', 'Y Nagar',
       'Y Prithvi Raj', 'Y Venugopal Rao', 'YA Abdulla', 'YBK Jaiswal',
       'YK Pathan', 'YS Chahal', 'YV Dhull', 'YV Takawale', 'Yash Dayal',
       'Yash Thakur', 'Yashpal Singh', 'Younis Khan', 'Yudhvir Singh',
       'Yuvraj Singh', 'Z Khan']
    
    
    search_input = st.text_input("Search for a player")

    # Filter players based on search input
    filtered_players = [player for player in list_of_the_players if search_input.lower() in player.lower()]

    # Show filtered list as a dropdown
    if filtered_players:
       selected_player = st.selectbox("Select a player", filtered_players)
    
    # Get player performance stats
       player_stat = helper.player_performance(data, selected_player)
    
    # Center-aligned player stats using HTML
       # Center-aligned player stats using HTML
       st.markdown(f"<h3 style='text-align: center;'>Player: {selected_player}</h3>", unsafe_allow_html=True)
       st.markdown(f"<h4 style='text-align: center;'>Matches Played: {player_stat['Matches_played']}</h4>", unsafe_allow_html=True)
       st.markdown(f"<h4 style='text-align: center;'>Total Runs: {player_stat['Total_runs']}</h4>", unsafe_allow_html=True)
       st.markdown(f"<h4 style='text-align: center;'>Batting Average: {player_stat['average']}</h4>", unsafe_allow_html=True)
       st.markdown(f"<h4 style='text-align: center;'>Batting Strike Rate: {player_stat['strike_rate']}</h4>", unsafe_allow_html=True)

    # Display bowling stats
       st.markdown(f"<h4 style='text-align: center;'>Total Wickets: {player_stat['Total_wickets']}</h4>", unsafe_allow_html=True)
       st.markdown(f"<h4 style='text-align: center;'>Bowling Average: {player_stat['bowling_average']}</h4>", unsafe_allow_html=True)
       st.markdown(f"<h4 style='text-align: center;'>Economy Rate: {player_stat['economy_rate']}</h4>", unsafe_allow_html=True)
    
    else:
       st.write("No players found matching your search.")
       
       

    st.subheader(f"Season-wise Performance for {selected_player}")
    player_season_perform=helper.player_performance_seasonwise(data,selected_player)
    st.dataframe(player_season_perform,use_container_width=True)
    player_stat =helper.player_performance(data, selected_player)
    
    # # Center-aligned player stats using HTML
    # st.markdown(f"<h3 style='text-align: center;'>Player: {selected_player}</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h4 style='text-align: center;'>Matches Played: {player_stat['Matches_played']}</h4>", unsafe_allow_html=True)
    # st.markdown(f"<h4 style='text-align: center;'>Total Runs: {player_stat['Total_runs']}</h4>", unsafe_allow_html=True)
    # st.markdown(f"<h4 style='text-align: center;'>Batting Average: {player_stat['average']}</h4>", unsafe_allow_html=True)
    # st.markdown(f"<h4 style='text-align: center;'>Strike Rate: {player_stat['strike_rate']}</h4>", unsafe_allow_html=True)
    
    # # Get season-wise performance stats
    season_stats =helper.player_performance_seasonwise(data, selected_player)
    
    # Plotting the season-wise performance graph using Plotly
    fig = go.Figure()

    # Add total runs as a line graph
    fig.add_trace(go.Scatter(x=season_stats['season'], y=season_stats['total_runs'], 
                             mode='lines+markers', name='Total Runs', line=dict(color='blue')))
    
    # # Add strike rate as a line graph
    # fig.add_trace(go.Scatter(x=season_stats['season'], y=season_stats['strike_rate'], 
    #                          mode='lines+markers', name='Strike Rate', line=dict(color='green')))
    
    # Add total wickets as a bar graph
    fig.add_trace(go.Bar(x=season_stats['season'], y=season_stats['total_wickets'], 
                         name='Total Wickets', marker=dict(color='red', opacity=0.6)))
    
    # #Add economy rate as a bar graph
    # fig.add_trace(go.Bar(x=season_stats['season'], y=season_stats['economy_rate'], 
    #                      name='Economy Rate', marker=dict(color='orange', opacity=0.6)))
    
    # Customize layout
    fig.update_layout(
        title=f"Season-wise Performance of {selected_player}",
        xaxis_title="Season",
        yaxis_title="Performance",
        barmode='group',  # Grouped bar chart for wickets and economy rate
        template="plotly_dark"
    )

    # Display the graph
    st.plotly_chart(fig)
    
    

#-----------------------------------------------------------------venue analysis-----------------------------------------------------
if option == "Venue Analysis":
    st.subheader('Venue Aanlysis')

    venue =data['venue'].unique()
    selected_venue = st.selectbox("Select a Venue", venue)
    
    total_matches,batting_first_succes_rate, chasing_success_rate =helper.overall_venue(data,selected_venue=selected_venue)
    
    st.subheader(f"Overall Analysis for Venue: {selected_venue}")
    st.write(f"**Total Matches Played:** {total_matches}")
    
    
    #pie chart for success  rates
    success_rates = [batting_first_succes_rate, chasing_success_rate]
    labels = ['First Batting Success Rate', 'Chasing Success Rate']
    colors = ['#FF9999', '#66B2FF']
    fig,ax=plt.subplots()
    ax.pie(success_rates,labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title(f"Success Rates at {selected_venue}")
    
    st.pyplot(fig)
    
    st.subheader(f"Top 5 batter at {selected_venue}")
    top_batter,top_baller=helper.most_runs_and_wicket_venue(data,selected_venue=selected_venue)
    
    st.dataframe(top_batter, use_container_width=True)
    st.subheader(f"Top 5 Wicket-Takers at {selected_venue}")
    st.dataframe(top_baller, use_container_width=True)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


    tabs = st.tabs(["Highest Score", "Lowest Score"])

    with tabs[0]:
       st.header(f"Highest  Score at {selected_venue}")
    # Get highest score details from the helper function
       venues_hs, batting_teams, bowling_teams, highest_scores_values = helper.highest_scores(data, selected_venue)
    
    # Display the details in centered columns
       col1, col2, col3 = st.columns([1, 2, 1])
       with col2:
        st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Batting Team</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 20px; font-weight: bold;'>{}</p>".format(batting_teams[0]), unsafe_allow_html=True)
        
        st.markdown("<h3 style='text-align: center; color: #FF5722;'>Bowling Team</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 20px; font-weight: bold;'>{}</p>".format(bowling_teams[0]), unsafe_allow_html=True)
        
        st.markdown("<h3 style='text-align: center; color: #2196F3;'>Highest Score</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 20px; font-weight: bold;'>{}</p>".format(highest_scores_values[0]), unsafe_allow_html=True)
    
        st.write(f"Highest Individual Score at {selected_venue}: {batting_teams[0]} scored {highest_scores_values[0]} runs against {bowling_teams[0]}.")

       with tabs[1]:
        st.header(f"Lowest Score at {selected_venue}")
        # Get lowest score details from the helper function
        venues_ls, batting_teams_ls, bowling_teams_ls, lowest_scores_values = helper.lowest_scores(data, selected_venue)
    
    # Display the details in centered columns
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
          st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Batting Team</h3>", unsafe_allow_html=True)
          st.markdown("<p style='text-align: center; font-size: 20px; font-weight: bold;'>{}</p>".format(batting_teams_ls[0]), unsafe_allow_html=True)
        
          st.markdown("<h3 style='text-align: center; color: #FF5722;'>Bowling Team</h3>", unsafe_allow_html=True)
          st.markdown("<p style='text-align: center; font-size: 20px; font-weight: bold;'>{}</p>".format(bowling_teams_ls[0]), unsafe_allow_html=True)
        
          st.markdown("<h3 style='text-align: center; color: #2196F3;'>Lowest Score</h3>", unsafe_allow_html=True)
          st.markdown("<p style='text-align: center; font-size: 20px; font-weight: bold;'>{}</p>".format(lowest_scores_values[0]), unsafe_allow_html=True)
    
          st.write(f"Lowest Score at {selected_venue}: {batting_teams_ls[0]} scored {lowest_scores_values[0]} runs against {bowling_teams_ls[0]}.")
 #------------------------------------------------------------------------------------------------------------------------------------------------
    st.title("🏏 IPL Venue Analysis - Score Intervals")



    if selected_venue:
    # Get score intervals
      intervals_df =helper.score_intervals(data, selected_venue)

    # Styled Subheader
    st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Score Intervals at {selected_venue}</h3>", unsafe_allow_html=True)

    # Show the intervals data
    st.table(intervals_df)

    # Visualize with Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(intervals_df['Score Range'], intervals_df['Frequency'], color='#1f77b4', edgecolor='black')
    ax.set_title(f"Score Distribution at {selected_venue}", fontsize=16, color='#333')
    ax.set_xlabel("Score Range", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Display the chart
    st.pyplot(fig)
    
    
    team_wins_venue=helper.most_won_match_on_venue(data,selected_venue)
    
    st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Matches Won by Teams at {selected_venue}</h3>", unsafe_allow_html=True)
    # Display as a table
    st.table(team_wins_venue)

    # Visualize with Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(team_wins_venue['winner'], team_wins_venue['Matches Won'], color='#1f77b4', edgecolor='black')
    ax.set_title(f"Matches Won by Teams at {selected_venue}", fontsize=16, color='#333')
    ax.set_xlabel("Matches Won", fontsize=12)
    ax.set_ylabel("Teams", fontsize=12)
    plt.tight_layout()

    # Display the chart
    st.pyplot(fig)
    
    

    # Get highest individual score details for the selected venue
    highest_score = helper.highest_individual_score_venue(data, selected_venue)
    highest_wickets = helper.highest_individual_wicket_venue(data, selected_venue)

    # Display Highest Individual Score interactively
    st.header("Show Highest Individual Score")
    with st.expander("Click to view highest individual score details"):
        st.write(f"**Batter:** {highest_score['batter']}")
        st.write(f"**Runs Scored:** {highest_score['batsman_runs']}")
        st.write(f"**Bowling Team:** {highest_score['bowling_team']}")
        st.write(f"**Season:** {highest_score['season']}")
        st.write(f"Highest Individual Score at {selected_venue}: {highest_score['batter']} scored {highest_score['batsman_runs']} runs against {highest_score['bowling_team']} in the {highest_score['season']} season.")

    # Display Best Bowling Performance interactively
    st.header("Show Best Bowling Performance")
    with st.expander("Click to view best bowling performance details"):
        st.write(f"**Bowler:** {highest_wickets['bowler']}")
        st.write(f"**Wickets Taken:** {highest_wickets['wickets']}")
        st.write(f"**Against Team:** {highest_wickets['batting_team']}")
        st.write(f"**Season:** {highest_wickets['season']}")
        st.write(f"Best Bowling Performance at {selected_venue}: {highest_wickets['bowler']} took {highest_wickets['wickets']} wickets against {highest_wickets['batting_team']} in the {highest_wickets['season']} season.")
    
    
    
####################################################batter_vs_bolwer##################################################################################################################################################################    

if option == '🏏 Batter vs ⚾ Bowler':
    st.subheader('🏏 Batter vs ⚾ Bowler')
    st.title("🏏 Batter vs Bowler Analysis")
    st.subheader("🎯 Interactive Cricket Insights")

    # Dropdowns for user input
    selected_batter = st.selectbox("Select Batter", data['batter'].unique())
    selected_bowler = st.selectbox("Select Bowler", data['bowler'].unique())
    selected_venue = st.selectbox("Select Venue (Optional)", ['All Venues'] + list(data['venue'].unique()))

    # Call the analysis function from helper module
    result = helper.batter_bowler_analysis(
        data=data,
        selected_batter=selected_batter,
        selected_bowler=selected_bowler,
        selected_venue=None if selected_venue == 'All Venues' else selected_venue
    )

    # Display analysis results in a structured format
    if result['total_runs'] > 0:
        # Display batter and bowler info
        st.markdown(f"### 🏏 Batter: **{result['batter']}**")
        st.markdown(f"### ⚾ Bowler: **{result['bowler']}**")
        if result['venue']:
            st.markdown(f"### 🏟 Venue: **{result['venue']}**")

        # Use columns to separate batter and bowler stats
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Batter's Performance")
            st.write(f"**Total Runs Scored:** {result['total_runs']} 🏆")
            st.write(f"**Balls Faced:** {result['balls_faced']} ⚾")
            st.write(f"**Strike Rate:** {result['strike_rate']} 🚀")
            st.write(f"**Fours:** {result['fours']} 🔥")
            st.write(f"**Sixes:** {result['sixes']} 💥")
            st.write(f"**Dismissals:** {result['dismissals']} ❌")
        with col2:
            st.markdown("### Bowler's Performance")
            st.write(f"**Total Wickets Taken:** {result['total_wickets']} 🎯")
            st.write(f"**Economy Rate:** {result['economy_rate']} 💸")

        # Detailed summary
        st.info(
            f"""
            **Summary**:  
            {result['batter']} scored **{result['total_runs']} runs** against {result['bowler']} 
            in **{result['balls_faced']} balls** with a **strike rate of {result['strike_rate']}**.  
            Additionally, {result['batter']} hit **{result['fours']} fours** and **{result['sixes']} sixes**.  
            The bowler dismissed the batter **{result['dismissals']} times** and had an **economy rate of {result['economy_rate']}**.
            """
        )
    else:
        st.warning(f"No data available for {result['batter']} against {result['bowler']} at {result['venue'] if result['venue'] else 'all venues'}.")

    st.markdown("---")
    st.caption("Powered by 🏏 Cricket Analytics")
