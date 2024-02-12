# Dicc with city and y coordinates for each team
from collections import defaultdict

team_city_coordinates = {
    'Man City': {'City': 'Manchester', 'Coordinates': [53.483959, -2.244644]},
    'Man United': {'City': 'Manchester', 'Coordinates': [53.483959, -2.244644]},
    'Liverpool': {'City': 'Liverpool', 'Coordinates': [53.408371, -2.991573]},
    'Chelsea': {'City': 'London', 'Coordinates': [51.509865, -0.118092]},
    'Arsenal': {'City': 'London', 'Coordinates': [51.509865, -0.118092]},
    'Fulham': {'City': 'London', 'Coordinates': [51.474144, -0.221174]},
    'Tottenham': {'City': 'London', 'Coordinates': [51.603231, -0.065684]},
    'West Ham': {'City': 'London', 'Coordinates': [51.538654, 0.016546]},
    'Leeds': {'City': 'Leeds', 'Coordinates': [53.777863, -1.580045]},
    'Leicester': {'City': 'Leicester', 'Coordinates': [52.636877, -1.139759]},
    'Brighton': {'City': 'Brighton', 'Coordinates': [50.860522, -0.080970]},
    'Wolves': {'City': 'Wolverhampton', 'Coordinates': [52.590056, -2.130421]},
    'Newcastle': {'City': 'Newcastle', 'Coordinates': [54.978252, -1.617439]},
    'Crystal Palace': {'City': 'London', 'Coordinates': [51.398254, -0.085733]},
    'Brentford': {'City': 'London', 'Coordinates': [51.488224, -0.287573]},
    'Aston Villa': {'City': 'Birmingham', 'Coordinates': [52.509132, -1.884994]},
    'Southampton': {'City': 'Southampton', 'Coordinates': [50.909698, -1.404351]},
    'Everton': {'City': 'Liverpool', 'Coordinates': [53.438847, -2.966471]},
    'Burnley': {'City': 'Burnley', 'Coordinates': [53.789958, -2.230996]},
    'Watford': {'City': 'Watford', 'Coordinates': [51.649021, -0.401511]},
    'Norwich': {'City': 'Norwich', 'Coordinates': [52.622319, 1.308989]}
}


# Grouped teams by city
city_teams = defaultdict(list)
for team, data in team_city_coordinates.items():
    city_teams[data['City']].append(team)

# Create a list
grouped_teams = [
    (city, data['Coordinates'], teams)
    for city, teams in city_teams.items()
    for team, data in team_city_coordinates.items()
    if data['City'] == city
]
