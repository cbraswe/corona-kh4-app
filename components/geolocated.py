from dash import html
import dash_leaflet as dl
import dash_bootstrap_components as dbc
import os
from shapely.geometry import Polygon

name = "Geolocated Plane Crashes"
img_coords = [
    [36.26072363015, -82.58834378005001],
    [36.79178077685, -82.58834378005001],
    [36.79178077685, -81.93113484415001],
    [36.26072363015, -81.93113484415001],
    [36.26072363015, -82.58834378005001],
]

center = Polygon(img_coords).centroid.coords
vor = [36.4370556, -82.1296000]
layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("Geolocated Plane Crashes"),
        html.P(
            "Unless otherwise indicated, geolocations are intended as a starting point for further analysis and not considered authoritative."
        ),
        html.H2("Possible DC-3 Crash Location"),
        html.P(
            'Attachment A in the DC-3 crash report provided an accurate map. Two image pixels were mapped to a geographic location, and a translation matrix was created for the remainder of the image. Due to the lack of landmarks in the original image, the accuracy of the translation is unclear. The LFR and LMM locations were possibly identified; however, one location has to be incorrect for the other to exist. Given the age of the map and construction around the airport, it seems probable that the current locations of the LMM/LOM do not reflect historics. Accuracy could improve with the identification of the Emmett "H", which is also known as Emmett MHW, EME MHW, Emmett Int. It is listed as 14.5 miles from Tri-Cities Airport.'
        ),
        html.Div(
            dl.Map(
                [
                    dl.TileLayer(
                        url="https://api.maptiler.com/maps/openstreetmap/256/{z}/{x}/{y}.jpg?key="
                        + f"{os.environ.get('MAP_TILER_KEY')}",
                        attribution="MapTiler",
                    ),
                    dl.Marker(
                        position=vor,
                        children=[dl.Tooltip(content="<b>Holston VOR<b/>")],
                        id="vor",
                    ),
                    dl.ImageOverlay(
                        opacity=0.5, url="/assets/se304_attacha.png", bounds=img_coords
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
                center=[Polygon(img_coords).centroid.x, Polygon(img_coords).centroid.y],
                zoom=10,
                style={"height": "500px", "width": "100%"},
            )
        ),
    ],
    id="nro-data",
    class_name="offset",
)
