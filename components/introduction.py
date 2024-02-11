from dash import html
import dash_bootstrap_components as dbc

name = "Introduction"
layout = dbc.Container(
    children=[
        html.H1("Introduction"),
        html.P(
            children=[
                "On May 25, 1961, newspapers published ominious titles following a rash of plane crashes:",
                html.I(" Holston Mountain 'Jinx' to Airplanes"),
                ", ",
                html.I("Holston Mountain is Massive Tombstone of 15 Dead In 3 Years, "),
                html.I("Pilot Error is Blamed for Air Crashes in Holston Range. "),
                "Located in East Tennessee near Tri-Cities Regional Airport and Elizabethton Municipal Airport, Holston Mountain proved treacherous for pilots from 1959-1961. Even the Federal Government seemed to notice a peculiar uptick in crashes because a simple mitigation was implemented in 1962. An amendment was published in the ",
                html.A(
                    "Code of Federal Regulations (CFR)",
                    href="https://www.govinfo.gov/app/details/FR-1962-05-03",
                ),
                " to re-name the Tri City Tennessee VOR (an aircraft navigational aid) to Holston Mountain VOR. Although pedantic, the name change enabled pilots to more easily derive the terrain associated with the VOR from the name because ",
                html.I(
                    "'during marginal weather conditions [pilots] could conceivably not see Holston Mountain in time to avoid it'."
                ),
            ]
        ),
        html.Br(),
        html.P(
            children=[
                "Likely due to technical limitations and procedures at the time, the crash locations are partially unknown and poorly recorded. However, hikers and geocachers have identified wreckage from most plane crashes. However, are these points of impact, parts that far exceeded the original crash bounds, or smaller parts that experienced a severe locational drift after 50 years? The amount of clean-up and removal varied wildly between crashes, so it is unclear how to characterize recently identified wreckage. For context, one report explicitly mentioned considering the aircraft a total loss and abandoning it to nature. A different report implied the area was fervently searched and parts removed."
            ]
        ),
        html.Br(),
        html.P(
            children=[
                "In 1996, President Clinton declassified approximately 860,000 satellite images from CORONA collected between 1960 - 1972. Theoretically, these images may provide sufficient information to accurately geolocate the crash sites, create Digital Surface Models, and analyze any impacts that may be present 50 years later. However, this requires there to be sufficient collection over the crash sites, and the crash sites to have a large geographic footprint observable from satellite. In addition to these problems, the availability of accurate metadata for the images poses the largest barrier to analysis. With current satellite imagery, associated metadata typically provides parameters for computation based on the operating parameters of the satellite. CORONA imagery does not have, but at least some of this data is expected to reside in the ",
                html.A(
                    "Freedom of Information Act (FOIA) repository for the National Reconnaissance Office (NRO)",
                    href="https://www.nro.gov/foia-home/foia-declassified-major-nro-programs-and-projects/CAL-Library-Listing/",
                ),
                ". Therefore, the first portion of the project will focus on improving the usability of 2,358 PDFs. To accomplish this task, a pre-trained deep learning tool will be used to extract text from the documents. This is expected to perform poorly in many scenarios; however, the documents of interest are primarily technical manuals expected to be well-maintained. With the extracted text, some pre-processing will be preformed to remove boilerplate text, and then topic clustering and/or topic modeling will be applied. This is an attempt to ensure all relevant documents are reviewed prior to further steps, and it is combined with a manual review. ",
            ]
        ),
        html.Br(),
        html.P(
            children=[
                "Newspapers will be used to identify approximate location of crashes, which will also restrict the analyzed CORONA imagery. Notionally, the next steps will be to use a feature matching model between CORONA and some other source. Since the area is mostly mountainous, it may be possible to create features from the general topography for use in feature matching to modern processes. Otherwise, the feature matching will use a modern deep learning framework to compare CORONA imagery to semi-recently collected imagery (either satellite or aerial). The accuracy will be determined by a manual process, which will involve creating a transformation matrix for a subset of images. The accuracy will be calculated based on the pixel shift between the results from feature matching and the manual process."
            ]
        ),
    ],
    id="introduction",
    class_name="offset",
)
