# -*- coding: utf-8 -*-
"""


@author: gargi
"""

import pandas as pd

data = pd.read_csv('mtcars.csv')

data.head()

data.shape
data.columns 
data.info()

# There are total 11 Columns
# ==============================================================================
#                         DATASET FEATURE DESCRIPTION
# ==============================================================================
#
# | Feature | Description                         | Type                    | Relevance
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | mpg     | Miles per gallon; fuel efficiency   | Quantitative, Continuous| Target Variable if predicting fuel
# |         | of the car.                         |                         | efficiency; other vehicle features
# |         |                                     |                         | may help explain or predict MPG.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | cyl     | Number of cylinders in the engine.  | Quantitative, Discrete  | Relevant; cylinder count may relate
# |         |                                     |                         | to engine size, horsepower, and MPG.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | disp    | Engine displacement, measured in    | Quantitative, Continuous| Relevant; engine size may influence
# |         | cubic inches.                       |                         | power, weight, and fuel efficiency.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | hp      | Gross horsepower of the car.        | Quantitative, Discrete  | Relevant; engine power may relate to
# |         |                                     |                         | weight, performance, and MPG.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | drat    | Rear axle ratio.                    | Quantitative, Continuous| Potentially Relevant; gearing may
# |         |                                     |                         | influence vehicle performance and
# |         |                                     |                         | fuel efficiency.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | wt      | Car weight, measured in 1,000 pounds| Quantitative, Continuous| Highly Relevant; vehicle weight may
# |         |                                     |                         | affect fuel consumption and MPG.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | qsec    | Time to travel a quarter mile,      | Quantitative, Continuous| Relevant; reflects vehicle
# |         | measured in seconds.                |                         | performance and acceleration.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | vs      | Engine configuration indicator:     | Qualitative, Binary     | Potentially Relevant; distinguishes
# |         | 0 = V-shaped, 1 = straight engine.  | (encoded 0/1)           | engine layouts that may relate to
# |         |                                     |                         | power and fuel efficiency.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | am      | Transmission indicator:             | Qualitative, Binary     | Relevant; 0 = automatic and
# |         | 0 = automatic, 1 = manual.          | (encoded 0/1)           | 1 = manual; transmission type may
# |         |                                     |                         | relate to performance and MPG.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | gear    | Number of forward gears.            | Quantitative, Discrete  | Potentially Relevant; gear count
# |         |                                     |                         | may relate to transmission type,
# |         |                                     |                         | performance, and fuel efficiency.
# |---------|-------------------------------------|-------------------------|-------------------------------------
# | carb    | Number of carburetors.              | Quantitative, Discrete  | Relevant; carburetor count reflects
# |         |                                     |                         | engine configuration and may relate
# |         |                                     |                         | to horsepower and MPG.
# ================================================================================================================

