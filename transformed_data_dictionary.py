import pandas as pd
from tabulate import tabulate
from data import result_df

# Assign the DataFrame from the imported module to df
df = result_df

# Get unique teams
teams = df['HomeTeam'].unique()

# Create a dictionary with teams and initial values
team_stats = {team: {'Points': 0, 'GoalsFor': 0, 'GoalsAgainst': 0, 'GoalDifference': 0,
                     'Wins': 0, 'Draws': 0, 'Losses': 0} for team in teams}

# Iterate over each row of the original DataFrame
for index, row in df.iterrows():
    # Check if the team was HomeTeam or AwayTeam and update statistics
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']
    home_goals = row['FTHG']
    away_goals = row['FTAG']

    # Update statistics
    team_stats[home_team]['GoalsFor'] += home_goals
    team_stats[home_team]['GoalsAgainst'] += away_goals
    team_stats[away_team]['GoalsFor'] += away_goals
    team_stats[away_team]['GoalsAgainst'] += home_goals

    # Assign points based on FTR
    if row['FTR'] == 'H':
        team_stats[home_team]['Points'] += 3
        team_stats[home_team]['Wins'] += 1
        team_stats[away_team]['Losses'] += 1
    elif row['FTR'] == 'A':
        team_stats[away_team]['Points'] += 3
        team_stats[home_team]['Losses'] += 1
        team_stats[away_team]['Wins'] += 1
    elif row['FTR'] == 'D':
        team_stats[home_team]['Points'] += 1
        team_stats[away_team]['Points'] += 1
        team_stats[home_team]['Draws'] += 1
        team_stats[away_team]['Draws'] += 1

# Calculate Goal Difference for each team
for team, stats in team_stats.items():
    stats['GoalDifference'] = stats['GoalsFor'] - stats['GoalsAgainst']

# Sort the dictionary by points from highest to lowest
sorted_team_stats = dict(sorted(team_stats.items(), key=lambda item: item[1]['Points'], reverse=True))

# Convert the sorted_team_stats to a DataFrame for better table formatting
df_stats = pd.DataFrame.from_dict(sorted_team_stats, orient='index')

# Display the sorted team statistics as a table
# print(tabulate(df_stats, headers='keys', tablefmt='pretty'))

# Reset index
df_stats.reset_index(inplace=True)  # Resetear el índice
df_stats = df_stats.rename(columns={'index': 'Team'})
Total_goals = df_stats['GoalsFor'].sum()
Avg_goals_per_game = Total_goals / (df.count()[0])

df_Total_goals_by_match = df['FTHG'] + df['FTAG']

df_consolidated = df_Total_goals_by_match.to_frame(name='TotalGoalsByMatch')
df_consolidated['RedCards'] = df['HR'] + df['AR']
df_consolidated['YellowCards'] = df['HY'] + df['AY']
df_consolidated['Corners'] = df['HC'] + df['AC']

df_consolidated.head(5)
type(df_consolidated)


df_wins_rate_home = df['FTR'].value_counts().get('H',0) / (df.count()[0])

# Referee stats
referee_win_rate = df.groupby("Referee").apply(lambda x: (x["FTR"] == "H").mean() * 100).sort_values(ascending=False)
nombres_arbitros = referee_win_rate.index
porcentajes = referee_win_rate.values
nombres_arbitros[0]
porcentajes[0]

# Calcula promedios para grupos de 5 partidos
# df_stats['Group'] = (df_stats.index // 5) + 1

# Eliminar la columna de índice original y tomar promedio
# df_stats2 = df_stats.copy()
# df_stats2.drop(columns=['Team'], inplace=True)
# average_stats_per_group = df_stats2.groupby('Group').mean()

# Muestra los promedios
# print(tabulate(average_stats_per_group, headers='keys', tablefmt='fancy_grid'))

# # Obtener los equipos del grupo 4
# teams_group_4 = df_stats[df_stats['Group'] == 4]['Team'].to_list()

# # Filtrar las filas correspondientes a los equipos del grupo 4
# matches_group_4 = df[(df['HomeTeam'].isin(teams_group_4)) | (df['AwayTeam'].isin(teams_group_4))]

# # Calcular el número total de partidos jugados por el Grupo 4
# total_matches_group_4 = len(matches_group_4)

# # Calcular estadísticas del Grupo 4 contra otros equipos
# group_4_vs_others = {'Points': 0, 'GoalsFor': 0, 'GoalsAgainst': 0, 'GoalDifference': 0, 'Wins': 0, 'Draws': 0, 'Losses': 0}

# # Iterar sobre cada fila de los partidos del Grupo 4
# for index, row in matches_group_4.iterrows():
#     home_team = row['HomeTeam']
#     away_team = row['AwayTeam']
#     home_goals = row['FTHG']
#     away_goals = row['FTAG']

#     # Actualizar estadísticas
#     group_4_vs_others['GoalsFor'] += home_goals if home_team in teams_group_4 else away_goals
#     group_4_vs_others['GoalsAgainst'] += away_goals if home_team in teams_group_4 else home_goals

#     # Asignar puntos según FTR
#     if row['FTR'] == 'H':
#         group_4_vs_others['Points'] += 3 if home_team in teams_group_4 else 0
#         group_4_vs_others['Wins'] += 1 if home_team in teams_group_4 else 0
#         group_4_vs_others['Losses'] += 1 if away_team in teams_group_4 else 0
#     elif row['FTR'] == 'A':
#         group_4_vs_others['Points'] += 3 if away_team in teams_group_4 else 0
#         group_4_vs_others['Wins'] += 1 if away_team in teams_group_4 else 0
#         group_4_vs_others['Losses'] += 1 if home_team in teams_group_4 else 0
#     elif row['FTR'] == 'D':
#         group_4_vs_others['Points'] += 1 if home_team in teams_group_4 else 0
#         group_4_vs_others['Points'] += 1 if away_team in teams_group_4 else 0
#         group_4_vs_others['Draws'] += 1 if home_team in teams_group_4 else 0
#         group_4_vs_others['Draws'] += 1 if away_team in teams_group_4 else 0

# # Calcular Diferencia de Goles
# group_4_vs_others['GoalDifference'] = group_4_vs_others['GoalsFor'] - group_4_vs_others['GoalsAgainst']

# # Calcular promedio de puntos y goles
# group_4_vs_others['Points'] /= total_matches_group_4
# group_4_vs_others['GoalsFor'] /= total_matches_group_4
# group_4_vs_others['GoalsAgainst'] /= total_matches_group_4
# group_4_vs_others['GoalDifference'] /= total_matches_group_4
# group_4_vs_others['Wins'] /= total_matches_group_4
# group_4_vs_others['Draws'] /= total_matches_group_4
# group_4_vs_others['Losses'] /= total_matches_group_4

# # Mostrar estadísticas del Grupo 4 contra otros equipos
# print("Group 4 vs Others Statistics (Averages):")
# print(tabulate([group_4_vs_others], headers='keys', tablefmt='pretty'))

