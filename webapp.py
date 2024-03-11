import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from transformed_data_dictionary import (
    df_stats,
    Total_goals,
    Avg_goals_per_game,
    df_consolidated,
    df_wins_rate_home,
    nombres_arbitros,
    porcentajes,
    original,
)

# upload data
df = df_stats

# Dash app
app = dash.Dash(__name__)


# Banner
banner = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Premier League - Season 2021-2022",
                    id="dashboard-title",
                    style={"text-align": "center", "color": "white", "flex": "1"},
                ),
                html.Img(
                    src="https://i.pinimg.com/736x/10/c5/ef/10c5efe06f251eea8dcda38bb2473136.jpg",
                    style={"height": "90px", "float": "right"},
                ),
            ],
            style={
                "display": "flex",
                "justify-content": "space-between",
                "align-items": "center",
                "background-color": "#ff7f0e",
                "padding": "10px",
            },
        ),
        html.Hr(style={"border-color": "#ff7f0e"}),
        html.P(
            "Data Science Personal Project for Fun.",
            style={"text-align": "left", "color": "white"},
        ),
    ],
    style={
        "background-color": "#1f77b4",
        "border-radius": "10px",
        "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
        "margin": "20px",
    },
)


class Card:
    def __init__(self, title, value, color):
        self.title = title
        self.value = value
        self.color = color

    def render(self):
        return html.Div(
            [
                html.H4(self.title, style={"color": "white"}),
                html.P(
                    self.value,
                    style={
                        "font-size": "20px",
                        "margin-bottom": "0",
                        "color": "white",
                        "text-align": "center",
                    },
                ),
            ],
            className="card",
            style={
                "background-color": self.color,
                "display": "block",
                "padding": "10px",
                "border-radius": "5px",
                "flex": "1",
            },
        )


total_goals_card = Card("Total Goals in the Season:", Total_goals, "#1f77b4")
goals_per_game_card = Card("Goals per Game:", round(Avg_goals_per_game, 2), "#1f77b4")
Pro_Local_Team_Referee_card = Card(
    "Pro Local Team Referee",
    f"{nombres_arbitros[0]}: {round(porcentajes[0], 2)}%",
    "#1f77b4",
)
Win_Rate_Local_Team_card = Card(
    "Win Rate Local Team:", f"{round(df_wins_rate_home * 100, 2)}%", "#1f77b4"
)

# Layout
app.layout = html.Div(
    [
        banner,
        dcc.Tabs(
            [
                dcc.Tab(
                    label="General Stats",
                    children=[
                        html.Div(
                            [
                                # First Row
                                html.Div(
                                    [
                                        # Column 1
                                        html.Div(
                                            [
                                                html.H3("Table"),
                                                dash_table.DataTable(
                                                    id="table",
                                                    columns=[
                                                        {"name": col, "id": col}
                                                        for col in df.columns
                                                    ],
                                                    data=df.to_dict("records"),
                                                    style_table={"overflowX": "auto"},
                                                    style_as_list_view=True,
                                                    style_header={
                                                        "backgroundColor": "#ff7f0e",
                                                        "color": "White",
                                                    },
                                                    style_cell={"textAlign": "center"},
                                                    style_data_conditional=[
                                                        {
                                                            "if": {"row_index": "odd"},
                                                            "backgroundColor": "#f9f9f9",
                                                        }
                                                    ],
                                                ),
                                            ],
                                            style={"flex": "1", "margin-right": "10px"},
                                        ),
                                        # Column 2
                                        html.Div(
                                            [
                                                # Column 2 - First row
                                                html.H3("Cards"),
                                                html.Div(
                                                    [
                                                        html.Div(  # Card #1
                                                            [
                                                                total_goals_card.render(),
                                                            ],
                                                            # className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "display": "block",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-left": "10px",
                                                            },
                                                        ),
                                                        html.Div(  # Card #2
                                                            [
                                                                goals_per_game_card.render(),
                                                            ],
                                                            # className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "display": "block",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-left": "10px",
                                                            },
                                                        ),
                                                        html.Div(  # Card #3
                                                            [
                                                                Pro_Local_Team_Referee_card.render()
                                                            ],
                                                            # className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "display": "block",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-left": "10px",
                                                            },
                                                        ),
                                                        html.Div(  # Card #4
                                                            [
                                                                Win_Rate_Local_Team_card.render()
                                                            ],
                                                            # className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "display": "block",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-left": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    style={
                                                        "display": "flex",
                                                    },
                                                ),
                                                # Second row - Column 2
                                                html.H3("Plot 1"),
                                                dcc.Graph(
                                                    id="team-stats-graph3",
                                                ),
                                            ],
                                            style={
                                                "flex": "1",
                                                "margin-left": "10px",
                                                "height": "200%",
                                            },
                                        ),
                                    ],
                                    style={
                                        "display": "flex",
                                        "justify-content": "space-between",  # columns formats
                                        # "align-items": "center",  # vertical allign
                                    },
                                ),
                                # Second row
                                html.Div(
                                    [
                                        # Column 1
                                        html.Div(
                                            [
                                                html.H3("Plot 2"),
                                                dcc.Graph(id="team-stats-graph4"),
                                            ],
                                            style={"flex": "1", "margin-right": "10px"},
                                        ),
                                        # Column 3
                                        html.Div(
                                            [
                                                html.H3("Box PLots"),
                                                dcc.Graph(id="boxplot"),
                                            ],
                                            style={"flex": "1"},
                                        ),
                                    ],
                                    style={
                                        "display": "flex",
                                        "justify-content": "space-between",
                                    },
                                ),
                            ],
                            style={
                                "display": "grid",
                                "grid-template-rows": "1fr 1fr",
                                "gap": "1rem",
                                "height": "100%",
                            },
                        ),
                    ],
                ),
                dcc.Tab(
                    label="Team Stats",
                    children=[  # Dropdown to select team
                        html.H3("Select Team:"),
                        dcc.Dropdown(
                            id="team-dropdown",
                            options=[
                                {"label": team, "value": team}
                                for team in df_stats["Team"]
                            ],
                            value=df_stats["Team"][0],  # Default value
                        ),
                        # Row 1 with 3 columns
                        html.Div(
                            children=[
                                # First column: Table
                                html.Div(
                                    children=[
                                        html.H3("Team Statistics"),
                                        dash_table.DataTable(
                                            id="TeamStatsContainer",
                                            columns=[
                                                {
                                                    "name": "Statistic",
                                                    "id": "Statistic",
                                                },
                                                {"name": "Value", "id": "Value"},
                                            ],
                                            data=[],  # Initially empty, data will be populated by the callback
                                            style_table={"overflowX": "auto"},
                                            style_cell={"textAlign": "left"},
                                            style_header={
                                                "backgroundColor": "#ff7f0e",
                                                "color": "White",
                                            },
                                            style_data_conditional=[
                                                {
                                                    "if": {"row_index": "odd"},
                                                    "backgroundColor": "#f9f9f9",
                                                }
                                            ],
                                        ),
                                    ],
                                    style={"flex": 1},  # adjust column withd 
                                ),
                                # Second column: first plot
                                html.Div(
                                    children=[
                                        html.H3("Team Statistics"),
                                        dcc.Graph(
                                            id="team-stats-graph"
                                        ),  
                                    ],
                                    style={"flex": 1},  
                                ),
                                # Third column: plot numb 2
                                html.Div(
                                    children=[
                                        dcc.Graph(
                                            id="team-stats-graph2"
                                        ),  
                                    ],
                                    style={"flex": 1},  
                                ),
                            ],
                            style={
                                "display": "flex",  
                                "justify-content": "space-between",  
                                "align-items": "center",  
                            },
                        ),
                        # Second row in 2nd tab
                        html.Div(),  # to add something later
                    ],
                ),
            ]
        ),
    ]
)


@app.callback(Output("TeamStatsContainer", "data"), [Input("team-dropdown", "value")])
def update_team_stats(selected_team):
    """
    Updates the team statistics based on the selected team.

    Parameters:
    - selected_team (str): The name of the team selected by the user.

    Returns:
    - list: A list of dictionaries containing the team's statistics.
    """

    if selected_team is None:
        return []

    # Get statistics for the selected team
    team_stats = df_stats[df_stats["Team"] == selected_team].iloc[0]

    stats_data = [
        {"Statistic": "Wins", "Value": team_stats["Wins"]},
        {"Statistic": "Losses", "Value": team_stats["Losses"]},
        {"Statistic": "Draws", "Value": team_stats["Draws"]},
        {"Statistic": "Goals Scored", "Value": team_stats["GoalsFor"]},
        {
            "Statistic": "Goals Scored per Game",
            "Value": round(team_stats["GoalsFor"] / int(38), 2),
        },
        {"Statistic": "Goals Conceded", "Value": team_stats["GoalsAgainst"]},
        {
            "Statistic": "Goals Conceded per Game",
            "Value": round(team_stats["GoalsAgainst"] / int(38), 2),
        },
        # ... add more statistics if needed
    ]

    return stats_data


# Callback to update team statistics graph based on selected team
@app.callback(Output("team-stats-graph", "figure"), [Input("team-dropdown", "value")])
def update_team_stats_graph(selected_team):
    """
    Updates the team statistics graph based on the selected team.

    Parameters:
    - selected_team (str): The name of the team selected by the user.

    Returns:
    - dict: An object containing the figure data for the Plotly graph.
    """

    if selected_team is None:
        return {}

    # Filter the other DataFrame based on the selected team

    perf_by_team_selected = original.query(
        "HomeTeam == @selected_team | AwayTeam == @selected_team"
    )

    def calculate_points(row):
        if row["FTR"] == "H":
            return 3 if row["HomeTeam"] == selected_team else 0
        elif row["FTR"] == "A":
            return 3 if row["AwayTeam"] == selected_team else 0
        elif row["FTR"] == "D":
            return (
                1
                if row["HomeTeam"] == selected_team or row["AwayTeam"] == selected_team
                else 0
            )
        else:
            return 0

    perf_by_team_selected["Points"] = perf_by_team_selected.apply(
        calculate_points, axis=1
    )
    perf_by_team_selected["Cumul_Points"] = perf_by_team_selected["Points"].cumsum()

    conditions = [
        (perf_by_team_selected["Points"] == 3),
        (perf_by_team_selected["Points"] == 0),
        (perf_by_team_selected["Points"] == 1),
    ]

    values = ["Won", "Lose", "Draw"]

    perf_by_team_selected["Result"] = np.select(conditions, values)

    perf_by_team_selected["Date"] = pd.to_datetime(
        perf_by_team_selected["Date"], dayfirst=True
    )

    
    wins = (
        perf_by_team_selected[perf_by_team_selected["Result"] == "Won"]
        .groupby("Date")
        .size()
        .cumsum()
    )
    losses = (
        perf_by_team_selected[perf_by_team_selected["Result"] == "Lose"]
        .groupby("Date")
        .size()
        .cumsum()
    )
    draws = (
        perf_by_team_selected[perf_by_team_selected["Result"] == "Draw"]
        .groupby("Date")
        .size()
        .cumsum()
    )

    # Plot
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=wins.index, y=wins.values, mode="lines", name="Wins"))

    fig.add_trace(
        go.Scatter(x=losses.index, y=losses.values, mode="lines", name="Losses")
    )

    fig.add_trace(go.Scatter(x=draws.index, y=draws.values, mode="lines", name="Draws"))

    # Cumula points
    fig.add_trace(
        go.Scatter(
            x=perf_by_team_selected["Date"],
            y=perf_by_team_selected["Cumul_Points"],
            mode="markers",
            name="Cumulative Points",
            yaxis="y2",
        )
    )

    fig.update_layout(
        title="Cumulative Progression of Wins, Losses, and Draws Over Time",
        xaxis_title="Date",
        yaxis_title="Cumulative Wins/Losses/Draws",
        yaxis2=dict(title="Cumulative Points", overlaying="y", side="right"),
        legend=dict(yanchor="top", y=1.02, xanchor="right", x=0.28),
    )

    return fig


# Callback2 to update team statistics graph based on selected team
@app.callback(Output("team-stats-graph2", "figure"), [Input("team-dropdown", "value")])
def update_team_stats_graph2(selected_team):
    """
    Updates the team statistics graph based on the selected team.

    Parameters:
    - selected_team (str): The name of the team selected by the user.

    Returns:
    - dict: An object containing the figure data for the Plotly graph.
    """
    if selected_team is None:
        return {}

    perf_by_team_selected = original.query(
        "HomeTeam == @selected_team | AwayTeam == @selected_team"
    )

    def calculate_points(row):
        if row["FTR"] == "H":
            return 3 if row["HomeTeam"] == selected_team else 0
        elif row["FTR"] == "A":
            return 3 if row["AwayTeam"] == selected_team else 0
        elif row["FTR"] == "D":
            return (
                1
                if row["HomeTeam"] == selected_team or row["AwayTeam"] == selected_team
                else 0
            )
        else:
            return 0

    perf_by_team_selected["Points"] = perf_by_team_selected.apply(
        calculate_points, axis=1
    )
    perf_by_team_selected["Cumul_Points"] = perf_by_team_selected["Points"].cumsum()

    conditions = [
        (perf_by_team_selected["Points"] == 3),
        (perf_by_team_selected["Points"] == 0),
        (perf_by_team_selected["Points"] == 1),
    ]

    values = ["Won", "Lose", "Draw"]

    perf_by_team_selected["Result"] = np.select(conditions, values)

    perf_by_team_selected["Date"] = pd.to_datetime(
        perf_by_team_selected["Date"], dayfirst=True
    )

    # Cumul percentage
    perf_by_team_selected["Cumul_Wins"] = (
        perf_by_team_selected["Result"].apply(lambda x: 1 if x == "Won" else 0).cumsum()
    )
    perf_by_team_selected["Cumul_Losses"] = (
        perf_by_team_selected["Result"]
        .apply(lambda x: 1 if x == "Lose" else 0)
        .cumsum()
    ) 
    perf_by_team_selected["Cumul_Draws"] = (
        perf_by_team_selected["Result"]
        .apply(lambda x: 1 if x == "Draw" else 0)
        .cumsum()
    )

    perf_by_team_selected["games"] = 1

    # Cumu perc as total fraction
    perf_by_team_selected["Cumul_Wins_Percentage"] = (
        perf_by_team_selected["Cumul_Wins"] / perf_by_team_selected["games"].cumsum()
    ) * 100
    perf_by_team_selected["Cumul_Losses_Percentage"] = (
        perf_by_team_selected["Cumul_Losses"] / perf_by_team_selected["games"].cumsum()
    ) * 100
    perf_by_team_selected["Cumul_Draws_Percentage"] = (
        perf_by_team_selected["Cumul_Draws"] / perf_by_team_selected["games"].cumsum()
    ) * 100

    fig = px.bar(
        perf_by_team_selected,
        x="Date",
        y=[
            "Cumul_Wins_Percentage",
            "Cumul_Losses_Percentage",
            "Cumul_Draws_Percentage",
        ],
        title="Porcentaje acumulado de Victorias, Derrotas y Empates",
        labels={"value": "Porcentaje acumulado", "variable": "Resultado"},
        color_discrete_map={
            "Cumul_Wins_Percentage": "green",
            "Cumul_Losses_Percentage": "red",
            "Cumul_Draws_Percentage": "yellow",
        },
        barmode="stack",
    )

    return fig


# Callback3 to update team statistics graph based on selected team
@app.callback(Output("team-stats-graph3", "figure"), [Input("team-dropdown", "value")])
def update_team_stats_graph3(selected_team):
    """
    Updates the team statistics graph based on the selected team.

    Parameters:
    - selected_team (str): The name of the team selected by the user.

    Returns:
    - dict: An object containing the figure data for the Plotly graph.
    """
    if selected_team is None:
        return {}

    df_stats["Avg_Goals_Scored"] = df_stats["GoalsFor"] / 38
    df_stats["Avg_Goals_Conceded"] = df_stats["GoalsAgainst"] / 38

    df_stats["Bubble_Size"] = (
        df_stats["Avg_Goals_Scored"] / df_stats["Avg_Goals_Conceded"]
    )

    fig = px.scatter(
        df_stats,
        x="Avg_Goals_Scored",
        y="Avg_Goals_Conceded",
        text="Team",
        size="Bubble_Size",
        size_max=60,
        color=df_stats["Team"].apply(
            lambda x: (
                "Top 5"
                if x in ["Man City", "Liverpool", "Chelsea", "Tottenham", "Arsenal"]
                else (
                    "Bottom 5"
                    if x in ["Norwich", "Watford", "Burnley", "Leeds", "Everton"]
                    else "Others"
                )
            )
        ),
    )

    fig.update_traces(
        marker=dict(line=dict(width=2, color="DarkSlateGrey")),
        selector=dict(mode="markers+text"),
    )

    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor="LightSteelBlue",
    )

    return fig


# Callback4 to update team statistics graph based on selected team
@app.callback(Output("team-stats-graph4", "figure"), [Input("team-dropdown", "value")])
def update_team_stats_graph4(selected_team):
    """
    Updates the team statistics graph based on the selected team.

    Parameters:
    - selected_team (str): The name of the team selected by the user.

    Returns:
    - dict: An object containing the figure data for the Plotly graph.
    """
    if selected_team is None:
        return {}

    # Contingency table
    contingency_table = pd.crosstab(original["HTR"], original["FTR"])

    contingency_table.reset_index(inplace=True)

    fig = px.bar(
        contingency_table,
        x="HTR",
        y=list(contingency_table.columns[1:]),
        title="Half Time result and Full Time result Relationship",
        labels={
            "halftime_result": "Half Time Result",
            "value": "Frecuencia",
            "variable": "Full Time Result",
        },
        barmode="stack",
    )

    # Mover la leyenda a la parte inferior
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor="LightSteelBlue",
    )

    return fig


# Callback para actualizar el boxplot
@app.callback(Output("boxplot", "figure"), [Input("team-dropdown", "value")])
def update_boxplot(selected_team):
    """
    Updates the boxplot figure based on the selected variable.

    Parameters:
    - selected_variable (str): The name of the variable selected by the user.

    Returns:
    - dict: An object containing the figure data for the Plotly boxplot.
    """
    if selected_team is None:
        return {}

    fig = go.Figure()

    for column in df_consolidated.columns:
        fig.add_trace(
            go.Box(
                y=df_consolidated[column],
                name=column,
                line_color="rgb(7,40,89)",
                boxpoints="outliers",
                showlegend=False,
            )
        )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Values",
        paper_bgcolor="LightSteelBlue",
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
