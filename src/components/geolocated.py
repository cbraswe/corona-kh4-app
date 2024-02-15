from dash import html
import dash_leaflet as dl
import dash_bootstrap_components as dbc
from dash import callback, Input, Output, State
import os
import rasterio
from utils import file_to_md, update_code_button

name = "Geolocated Plane Crashes"
# DC3 Notes: 18.75 nm from tri-cities airport
# aircraft was on a course of 235 degrees
# struck at 3140 ft near crest of mountain
# lmm should be 5 nm east of the end of runway 27
# lom must be 3.7 nm east of the runway 27
# emmett beacon must be 12.3 nm east of runway
dc3 = rasterio.open("assets/se304_attacha.png").bounds
dc3_bounds = [
    [dc3.bottom, dc3.left],
    [dc3.top, dc3.left],
    [dc3.top, dc3.right],
    [dc3.bottom, dc3.right],
    [dc3.bottom, dc3.left],
]  # this is inverted for use with Dash-leaflet
dc3_center = [(dc3.top + dc3.bottom) / 2, (dc3.left + dc3.right) / 2]
airport = [36.47853873, -82.3953803]
vor = [36.4370628, -82.1295676]
tricites_lfr = [36.494722, -82.334722]  # https://flyingthebeams.com/map
layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("Geolocated Plane Crashes"),
        html.P(
            "Unless otherwise indicated, geolocations are intended as a starting point for further analysis and not considered authoritative."
        ),
        html.H2("Possible DC-3 Crash Location, Annotated by 'X'"),
        html.P(
            children=[
                "In the DC-3 crash report, Attachment-A included a map with a scale and North arrow, which are typically indicative of an accurate map. To translate the image into a greogaphical location, image pixels for Holston VOR and Tri-Cities Airport were mapped to their geographic location to create a translation matrix. The approximate location of the Tri-Cities Low Frequency Range is ",
                html.A(
                    "known, but the precision of coordinates is unclear.",
                    href="https://flyingthebeams.com/map",
                ),
                " Therefore, this set of coordinates was excluded.",
            ]
        ),
        dbc.Button("", id="data-geolocation-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/geolocation/1_geolocating_dc3.ipynb"),
            id="data-geolocation-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.P(
            "The below map represents the perceived best possible solution for the map, with point markers included as reference to understand potential skew. A simplified, polygonized elevation is included for Sullivan County elevations between 3120-3160ft, since the point of impact was reportedly at 3,140ft. The elevation was originally provided with 2ft post spacing with very high accuracy, which reduced responsiveness."
        ),
        html.Div(
            dl.Map(
                [
                    dl.LayersControl(
                        [
                            dl.BaseLayer(
                                dl.TileLayer(
                                    url="https://api.maptiler.com/maps/topo-v2/{z}/{x}/{y}.png?key="
                                    + f"{os.environ.get('MAP_TILER_KEY')}",
                                    attribution="&copy; <a href='https://www.maptiler.com/copyright/'>MapTiler</a>",
                                ),
                                checked=True,
                                name="Topographic Basemap",
                            ),
                            dl.BaseLayer(
                                dl.TileLayer(
                                    url="https://api.maptiler.com/maps/openstreetmap/256/{z}/{x}/{y}.jpg?key="
                                    + f"{os.environ.get('MAP_TILER_KEY')}",
                                    attribution="&copy; <a href='https://www.maptiler.com/copyright/'>MapTiler</a>",
                                ),
                                checked=False,
                                name="Open Street Maps",
                            ),
                            dl.Overlay(
                                dl.TileLayer(
                                    url="https://api.maptiler.com/tiles/contours/{z}/{x}/{y}.pbf?key="
                                    + f"{os.environ.get('MAP_TILER_KEY')}",
                                ),
                                name="Contour Vectors (Experimental)",
                            ),
                            dl.Overlay(
                                dl.LayerGroup(
                                    dl.LayerGroup(
                                        [
                                            dl.Marker(
                                                position=vor,
                                                children=[
                                                    dl.Popup(
                                                        content="<b>Holston VOR<b/>"
                                                    )
                                                ],
                                                id="vor",
                                            ),
                                            dl.Marker(
                                                position=airport,
                                                children=[
                                                    dl.Popup(
                                                        content="<b>Tri-Cities Airport End of Runway 27<b/>"
                                                    )
                                                ],
                                                id="airport",
                                            ),
                                            dl.Marker(
                                                position=tricites_lfr,
                                                children=[
                                                    dl.Popup(
                                                        content="<b>Approximate Location of Tri-Cities LFR, fidelity UNK<b/>"
                                                    )
                                                ],
                                            ),
                                        ],
                                    )
                                ),
                                checked=True,
                                name="Mentioned Locations",
                            ),
                            dl.Overlay(
                                dl.GeoJSON(url="/assets/3120_3160_elvation.geojson"),
                                checked=True,
                                name="Polygonized Elevation (3120-3160ft)",
                            ),
                        ]
                    ),
                    dl.ImageOverlay(
                        opacity=0.5, url="/assets/se304_attacha.png", bounds=dc3_bounds
                    ),
                    dl.MeasureControl(
                        position="topleft",
                        primaryLengthUnit="miles",
                        secondaryLengthUnit="meters",
                        primaryAreaUnit="sqmiles",
                        secondaryAreaUnit="sqmeters",
                        activeColor="#214097",
                        completedColor="#972158",
                    ),
                ],
                center=dc3_center,
                zoom=10,
                style={"height": "500px", "width": "100%"},
            )
        ),
    ],
    id="geolocated-crashes",
    class_name="offset",
)


#! TODO: Find a better mechanism to handle these shared code cases. I think matching will work
@callback(
    [
        Output("data-geolocation-collapse-code", "is_open"),
        Output("data-geolocation-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-geolocation-collapse-button", "n_clicks")],
    [
        State("data-geolocation-collapse-code", "is_open"),
    ],
)
def toggle_pdf_retrieval_collapse(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)
