import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from tabulate import tabulate
from transformed_data_dictionary import (
    df_stats,
    Total_goals,
    Avg_goals_per_game,
    df_consolidated,
    df_wins_rate_home,
    nombres_arbitros,
    porcentajes,
)
import dash_leaflet as dl
from dash_leaflet import Marker, Tooltip
from dash.exceptions import PreventUpdate
from cities_coordinates import team_city_coordinates, grouped_teams
import plotly.express as px

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
                                            # Interactivity: Go to the map when click over a row in the table
                                            row_selectable="single",
                                            selected_rows=[],
                                        ),
                                    ],
                                    style={"flex": "1", "margin-right": "10px"},
                                ),
                                html.Div(
                                    [
                                        html.H3("Team location"),
                                        dl.Map(
                                            id="map",
                                            center=[
                                                54.7023545,
                                                -3.2765753,
                                            ],  # united Kingdom coorden.
                                            zoom=6,
                                            children=[
                                                dl.TileLayer(),
                                                *[
                                                    Marker(
                                                        id=f"marker-{city}",
                                                        position=city_coordinates,
                                                        children=[
                                                            Tooltip(children=[html.P(", ".join(teams))]), 
                                                        ],
                                                    )
                                                    for city, city_coordinates, teams in grouped_teams
                                                ],
                                            ],
                                            style={"width": "97%", "height": "650px"},
                                        ),
                                    ],
                                    style={"flex": "1", "margin-left": "10px"},
                                ),
                                html.Div(
                                    [
                                        html.H3("Cards"),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(  # Card #1
                                                            [
                                                                html.H4(
                                                                    "Total Goals in the Season",
                                                                    style={
                                                                        "color": "white"
                                                                    },
                                                                ),
                                                                html.P(
                                                                    Total_goals,
                                                                    style={
                                                                        "font-size": "20px",
                                                                        "margin-bottom": "0",
                                                                    },
                                                                ),
                                                            ],
                                                            className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "display": "block",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-right": "10px",
                                                            },
                                                        ),
                                                        html.Div(  # Card #2
                                                            [
                                                                html.H4(
                                                                    "Goals per Game",
                                                                    style={
                                                                        "color": "white"
                                                                    },
                                                                ),
                                                                html.P(
                                                                    round(
                                                                        Avg_goals_per_game,
                                                                        2,
                                                                    ),
                                                                    style={
                                                                        "font-size": "20px",
                                                                        "margin-bottom": "0",
                                                                    },
                                                                ),
                                                            ],
                                                            className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-left": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    style={
                                                        "display": "flex"
                                                    },  # Container as flexbox
                                                ),
                                            ],
                                            style={"flex": "1", "margin-right": "10px"},
                                        ),
                                        html.Div(style={"height": "10px"}),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(  # Card #3
                                                            [
                                                                html.H4(
                                                                    "Pro Home Referee (%)",
                                                                    style={
                                                                        "color": "white"
                                                                    },
                                                                ),
                                                                html.P(
                                                                    f"{nombres_arbitros[0]}: {round(porcentajes[0], 2)}%",
                                                                    style={
                                                                        "font-size": "20px",
                                                                        "margin-bottom": "0",
                                                                    },
                                                                ),
                                                            ],
                                                            className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-right": "10px",
                                                            },
                                                        ),
                                                        html.Div(  # Card #4
                                                            [
                                                                html.H4(
                                                                    "Win Rate Local Team",
                                                                    style={
                                                                        "color": "white"
                                                                    },
                                                                ),
                                                                html.P(
                                                                    f"{round(df_wins_rate_home * 100, 2)}%",
                                                                    style={
                                                                        "font-size": "20px",
                                                                        "margin-bottom": "0",
                                                                    },
                                                                ),
                                                            ],
                                                            className="card",
                                                            style={
                                                                "background-color": "#1f77b4",
                                                                "padding": "10px",
                                                                "border-radius": "5px",
                                                                "flex": "1",
                                                                "margin-left": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    style={
                                                        "display": "flex"
                                                    },  # Container as flexbox
                                                ),
                                            ],
                                            style={"flex": "1", "margin-right": "10px"},
                                        ),
                                        html.Div(
                                            [
                                                html.H3("Histogram"),
                                                dcc.Dropdown(
                                                    id="histogram-variable-dropdown",
                                                    options=[
                                                        {"label": col, "value": col}
                                                        for col in df_consolidated.columns
                                                    ],
                                                    value="TotalGoalsByMatch",  # initial Value
                                                    style={"width": "50%"},
                                                ),
                                                dcc.Graph(id="histogram"),
                                            ],
                                            style={"flex": "1", "margin-top": "10px"},
                                        ),
                                    ],
                                    style={"flex": "1"},
                                ),
                            ],
                            style={"display": "flex"},
                        ),
                    ],
                ),
                dcc.Tab(
                    label="Team Stats",
                    children=[
                        html.Div(
                            [
                                # Pending (plots, stats by team)
                            ]
                        )
                    ],
                ),
            ]
        ),
    ]
)


# Callback: click over row table and update map
# @app.callback(
#     [
#         Output("table", "selected_rows"),
#         Output("map", "center"),
#         Output("selected-marker", "position"),
#         Output("team-name-tooltip", "children"),
#     ],
#     [Input("table", "derived_virtual_selected_rows"), Input("table", "data")],
# )
# def update_selected_row_and_map(selected_rows, data):
#     if selected_rows is None or len(selected_rows) == 0:
#         raise PreventUpdate  # No selected row

#     selected_row = selected_rows[0]
#     selected_team = data[selected_row]["Team"]

#     team_info = team_city_coordinates.get(selected_team, {})
#     coordenadas_equipo = team_info.get("Coordinates")

#     if coordenadas_equipo:
#         return [
#             selected_rows,
#             coordenadas_equipo,
#             coordenadas_equipo,
#             selected_team,
#         ]
#     else:
#         raise PreventUpdate  # No location for team


# Callback: histogram update using dropdown
@app.callback(
    Output("histogram", "figure"), [Input("histogram-variable-dropdown", "value")]
)
def update_histogram(selected_variable):
    fig = px.histogram(
        df_consolidated,
        x=selected_variable,
        nbins=10,
        histnorm="percent",
        title=f"Distribution of {selected_variable}",
        color_discrete_sequence=["#0c2142"],
    ).update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        title=dict(x=0.5),
        xaxis=dict(title=selected_variable),
        yaxis=dict(title="Percentaje over Total Games"),
        margin=dict(t=50, b=50, l=50, r=50),
        height=350,
        bargap=0.1,
    )
    return fig


# Run app
if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
