from dash import html, register_page
import dash_bootstrap_components as dbc
from components import corona_dsm, keypoint_fm, introduction, nro_data, plane_crashes

register_page(__name__, path="/", order=0)

# This page is strange due to my personal desire to have a long, scrolling content pane 
# However, there are many sections that will exist in this document that would decrease code readability significantly if included here
# therefore, these sections are included in the components directory
# for a component to successfully work with the below code and be part of the sidebar, it must have a layout and
component_order = [introduction, plane_crashes, nro_data, corona_dsm, keypoint_fm]

sidebar = html.Div(
    [
        html.H2("Project Structure", className="display-7"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    component.name,
                    href=f"#{component.layout.id}",
                    active="exact",
                    external_link=True,
                )
                for component in component_order
            ],
            vertical=True,
        ),
    ],
    style={
        "position": "fixed",
        "width": "16rem",
        "margin": "10rem -15rem",
        "padding": "1rem",
        "border": "2px solid #2D4A63",
        "border-radius": "20px",
    },
)

layout = dbc.Container(
    children=[
        sidebar,
        html.Div(
            children=[component.layout for component in component_order],
            style={"margin-left": "2rem"},
        ),
    ],
)
