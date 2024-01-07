import pandas as pd
from data import result_df

# Assign the DataFrame from the imported module to df
df = result_df

# Get unique teams
teams = df['HomeTeam'].unique()

# Create a dictionary with teams and initial values of 0
points_per_team = {team: 0 for team in teams}

# Iterate over each row of the original DataFrame
for index, row in df.iterrows():
    # Check if the team was HomeTeam or AwayTeam and assign points based on FTR
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']

    # Assign points based on FTR
    if row['FTR'] == 'H':
        points_per_team[home_team] += 3
    elif row['FTR'] == 'A':
        points_per_team[away_team] += 3
    elif row['FTR'] == 'D':
        points_per_team[home_team] += 1
        points_per_team[away_team] += 1

# Sort the dictionary by points from highest to lowest
sorted_points_per_team = dict(sorted(points_per_team.items(), key=lambda item: item[1], reverse=True))

# Display the dictionary sorted with points per team
print("Points per team (sorted):")
for team, points in sorted_points_per_team.items():
    print(f"{team}: {points}")
