# -*- coding: utf-8 -*-
"""


@author: gargi
"""

import pandas as pd

data = pd.read_csv('Company_Data.csv')

data.head()

data.shape # (400, 11)
data.columns 
data.info()

# There are total 11 Columns

# =============================================================================
#                         DATASET FEATURE DESCRIPTION
# =============================================================================
#
# | Feature     | Description                                      | Data Type             | Relevance
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Sales       | Sales of the product at each store, measured     | Quantitative,         | Target Variable; used as the
# |             | in thousands of units.                           | Continuous            | outcome to understand or predict sales.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | CompPrice   | Price charged by a competitor for a comparable   | Quantitative,         | Relevant; competitor pricing may
# |             | product.                                         | Discrete              | influence demand and relative value.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Income      | Income level of the local population around      | Quantitative,         | Potentially Relevant; may represent
# |             | the store, as recorded in the dataset.           | Discrete              | local purchasing power.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Advertising | Advertising expenditure for the store or market, | Quantitative,         | Relevant; may increase awareness.
# |             | in units defined by the dataset source.          | Discrete              | Weak positive correlation with Sales
# |             |                                                  |                       | (r = 0.27); limited linear relationship.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Population  | Population size of the area served by the store. | Quantitative,         | Potentially Relevant; may approximate
# |             |                                                  | Discrete              | market size, but not likely customers alone.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Price       | Price charged by the store for the product.      | Quantitative,         | Highly Relevant; may influence demand.
# |             |                                                  | Discrete              | Moderate negative correlation with Sales
# |             |                                                  |                       | (r = -0.44).
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | ShelveLoc   | Quality of the product's shelving/display        | Qualitative,          | Highly Relevant; display quality can
# |             | location: Bad, Medium, or Good.                  | Ordinal               | affect visibility and buying decisions.
# |             |                                                  |                       | Preserve category order during encoding.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Age         | Age-related measure for the local market,        | Quantitative,         | Potentially Relevant; may relate to
# |             | as recorded in the dataset.                      | Discrete              | purchasing patterns.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Education   | Education level of the local population,         | Quantitative,         | Potentially Relevant; may capture
# |             | as recorded in the dataset.                      | Discrete              | demographic differences.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | Urban       | Indicates whether the store is in an urban area  | Qualitative,          | Potentially Relevant; urban/rural
# |             | (Yes/No).                                        | Binary                | context may affect customer traffic.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
# | US          | Indicates whether the store is in the United     | Qualitative,          | Potentially Relevant; may capture
# |             | States (Yes/No).                                 | Binary                | geographic or market differences.
# |-------------|--------------------------------------------------|-----------------------|-----------------------------
