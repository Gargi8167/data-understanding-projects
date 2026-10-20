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

# | Feature Name | Type                     | Discription                      | Relevance |
# |--------------|--------------------------|----------------------------------|-----------|
# | Sales	     | Quantitative, Continuous | Product sales (units or $)       | Relevant  |
# | CompPrice	 | Quantitative, Continuous | Competitor’s product price       | Relevant  |
# | Income	     | Quantitative, Continuous | Customer’s household income      | Relevant  |
# | Advertising	 | Quantitative, Continuous | Company’s advertising budget     | Relevant  |
# | Population	 | Quantitative, Continuous | Population size of region	       | Relevant  |
# | Price	     | Quantitative, Continuous | Price of company product         | Relevant  |
# | ShelveLoc	 | Qualitative, Ordinal	    | Shelf location (Bad/Medium/Good) | Relevant  |
# | Age	         | Quantitative, Discrete	| Age of customer                  | Relevant  |
# | Education	 | Quantitative, Discrete   | Years of education               | Relevant  |
# | Urban	     | Qualitative, Binary	    | Store in urban area (Yes/No)     | Relevant  |
# | US           | Qualitative, Binary	    | Store located in US (Yes/No)     | Relevant  |