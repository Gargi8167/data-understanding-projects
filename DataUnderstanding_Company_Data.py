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

# ==============================================================================
#                         DATASET FEATURE DESCRIPTION
# ==============================================================================
#
# | Feature     | Description                         | Type                 | Relevance
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Sales       | Sales of the product at each store, | Quantitative,        | Target Variable; used to understand
# |             | measured in thousands of units.     | Continuous           | or predict store sales.
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | CompPrice   | Price charged by a competitor for a | Quantitative,        | Relevant; may influence demand and
# |             | comparable product.                 | Discrete             | relative value versus store Price.
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Income      | Income level of the local population| Quantitative,        | Potentially Relevant; may indicate
# |             | around the store, as recorded in    | Discrete             | purchasing power and demand.
# |             | the dataset.                        |                      |
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Advertising | Advertising expenditure for the     | Quantitative,        | Relevant; may increase customer
# |             | store or market, as defined by the  | Discrete             | awareness and influence Sales.
# |             | dataset source.                     |                      |
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Population  | Population size of the area served  | Quantitative,        | Potentially Relevant; may indicate
# |             | by the store.                       | Discrete             | market size, but not actual customers.
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Price       | Price charged by the store for the  | Quantitative,        | Highly Relevant; may influence
# |             | product.                            | Discrete             | demand and purchasing decisions.
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | ShelveLoc   | Quality of the product's shelving/  | Qualitative,         | Highly Relevant; display quality
# |             | display location: Bad, Medium, or   | Ordinal              | may affect visibility and Sales.
# |             | Good.                               |                      |
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Age         | Age-related measure for the local   | Quantitative,        | Potentially Relevant; may relate
# |             | market, as recorded in the dataset. | Discrete             | to demographic purchasing patterns.
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Education   | Education level of the local        | Quantitative,        | Potentially Relevant; may capture
# |             | population, as recorded in the      | Discrete             | demographic differences.
# |             | dataset.                            |                      |
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | Urban       | Indicates whether the store is in   | Qualitative,         | Potentially Relevant; location may
# |             | an urban area (Yes/No).             | Binary               | affect traffic and purchasing patterns.
# |-------------|-------------------------------------|----------------------|-------------------------------------
# | US          | Indicates whether the store is in   | Qualitative,         | Potentially Relevant; may capture
# |             | the United States (Yes/No).         | Binary               | geographic or market differences.
# |-------------|-------------------------------------|----------------------|-------------------------------------
#
# ==============================================================================