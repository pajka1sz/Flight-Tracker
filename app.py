from dash import Dash, dcc, callback, Input, Output
from dash.html import Div, H1
import plotly.express as px
from main import export_df

app = Dash()

df = export_df()

app.layout = Div([
    H1("Flight Tracker"),

    dcc.Dropdown(
        id="aircraft-selection",
        options=[{"label": i, "value": i}
                 for i in df["icao24"].unique()]
    ),

    dcc.Graph(figure={}, id="flight-map", style={"width": "100%", "height": "100%"}),
])


@callback(
    Output(component_id="flight-map", component_property="figure"),
    Input(component_id="aircraft-selection", component_property="value")
)
def show_flight(aircraft_chosen):
    if aircraft_chosen is None:
        return {}

    aircraft_track = df[df["icao24"] == aircraft_chosen].sort_values("time")
    fig = px.line_map(aircraft_track, lat="lat", lon="lon")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
