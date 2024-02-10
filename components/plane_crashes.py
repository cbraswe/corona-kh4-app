from dash import html
from datetime import datetime
import dash_bootstrap_components as dbc

name = "Plane Crashes"
# The below format is intended to help simplify the development and addition of content
# fore ach accordion item, if it provided a date of the crash in iso-format it will be sorted by date
army_l20_1960 = dbc.AccordionItem(
    html.Div(
        children=[
            html.P(
                [
                    "According to the ",
                    html.A(
                        "Johnson City Press-Chronicle", href="/#army_l20_1960_newspaper"
                    ),
                    ", an Army L20 crashed into the top of Cove Ridge in the Holston Mountains at 00:30 EST.",
                    " A FOIA request was submitted to the Army and may be independently ",
                    html.A(
                        "downloaded and reviewed.",
                        href="/data/1960_army_l20_foia.pdf",
                        download="1960_army_l20_foia.pdf",
                    ),
                    " Within the report, there are topographic scans of the area, several pictures taken from the perspective of the crash site, and detailed radio traffic surrounding the incident.",
                ]
            ),
            html.P(
                [
                    "On page 61, the crash site is described as",
                    html.Em(
                        html.B(
                            " 'on a 2100 foot hill, ten miles from Tri City Airport on a heading of 102 degrees or 4 miles from the Tri City Omni on a heading of 270 degrees or 1 mile north of the V16-V185E Airways'"
                        )
                    ),
                    " and ",
                    html.Em(
                        html.B(
                            "' [the plane] struck the trees 154 feet below the crest of the hill in a wing level'"
                        )
                    ),
                    ". ",
                ]
            ),
        ]
    ),
    title="Dec 17, 1960, An Army L-20 (SN 54-41671)",
    id=datetime(1960, 12, 17).date().isoformat(),
)

army_l19_1961 = dbc.AccordionItem(
    html.P("Hello 2"),
    title="27 December 1959, Army L-20, SN 54-41671",
    id=datetime(1959, 12, 17).date().isoformat(),
)

layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("Holston Mountain Plane Crashes"),
        html.Br(),
        html.P(
            "There are significant barriers in the identification of historic plane crashes. The primary barrier is an overwhelming reliance on the crash record being digitized and searchable. With Holston Mountain, there are crash records maintained by several different agencies: Federal Aviation Administration (FAA), Navy, Air Force, Army, and the National Transportation Safety Bureau (NTSB). To obtain full details for the crashes, it is often required to submit a Freedom of Information Act (FOIA) request to the investigative body. Next, the quality of the data varies heavily based on crash year and investigative body. Investigating a plane crash on a mountainside is labor and cost intensive, which may affect the ability and willingness of an agency to create the best possible record."
        ),
        html.P(
            "The following plane crashes were identified, primarily by digitized newspapers:"
        ),
        dbc.Accordion(
            sorted([army_l20_1960, army_l19_1961], key=lambda x: x.id),
            start_collapsed=True,
        ),
    ],
    id="plane-crashes",
    class_name="offset",
)
