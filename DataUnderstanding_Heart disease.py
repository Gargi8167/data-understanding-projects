# -*- coding: utf-8 -*-
"""


@author: gargi
"""

import pandas as pd

data = pd.read_csv('heart disease.csv')

data.head()

data.shape
data.columns 
data.info()

# ==============================================================================
#                       HEART DISEASE DATASET FEATURE DESCRIPTION
# ==============================================================================
#
# | Feature  | Description                          | Type                    | Relevance
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | age      | Age of the patient, in years.        | Quantitative, Discrete  | Potentially Relevant; age may be
# |          |                                      |                         | associated with heart-disease status.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | sex      | Sex code used by the dataset         | Qualitative, Binary     | Potentially Relevant; differences
# |          | (commonly 1 = male, 0 = female).     | (encoded 0/1)           | between categories may relate to the
# |          | Confirm using the source codebook.   |                         | target. Verify category encoding.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | cp       | Chest-pain type code; categories     | Qualitative, Nominal    | Relevant; chest-pain presentation may
# |          | are numerically coded.               | (encoded categories)    | provide useful diagnostic information.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | trestbps | Resting blood pressure, typically    | Quantitative,           | Potentially Relevant; may relate to
# |          | measured in mm Hg.                   | Continuous              | heart-disease status and cardiovascular
# |          |                                      |                         | risk factors.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | chol     | Serum cholesterol, typically         | Quantitative,           | Potentially Relevant; may relate to
# |          | measured in mg/dL.                   | Continuous              | cardiovascular risk and other indicators.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | fbs      | Fasting blood sugar indicator;       | Qualitative, Binary     | Potentially Relevant; may provide
# |          | commonly 1 if above 120 mg/dL,       | (encoded 0/1)           | additional clinical context.
# |          | otherwise 0.                         |                         |
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | restecg  | Resting electrocardiographic result, | Qualitative, Nominal    | Relevant; ECG categories may provide
# |          | encoded as categories.               | (encoded categories)    | useful clinical information.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | thalach  | Maximum heart rate achieved          | Quantitative, Discrete  | Relevant; reflects exercise response
# |          | during the test.                     |                         | and may aid clinical assessment.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | exang    | Exercise-induced angina indicator    | Qualitative, Binary     | Relevant; exercise-induced angina may
# |          | (commonly 1 = yes, 0 = no).          | (encoded 0/1)           | provide diagnostic information.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | oldpeak  | ST depression induced by exercise    | Quantitative,           | Relevant; exercise-related ST
# |          | relative to rest.                    | Continuous              | depression may provide clinical evidence.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | slope    | Slope category of the peak-exercise  | Qualitative, Ordinal    | Relevant; ST-slope categories may
# |          | ST segment, numerically coded.       | (encoded categories)    | complement other exercise-test results.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | ca       | Number of major vessels (0–3)        | Quantitative, Discrete  | Relevant; vessel count may provide
# |          | colored by fluoroscopy.              |                         | important diagnostic information.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | thal     | Thalassemia/thal test result code,   | Qualitative, Nominal    | Relevant; test category may provide
# |          | represented as numeric categories.   | (encoded categories)    | clinical information. Verify category
# |          |                                      |                         | meanings using the source codebook.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
# | target   | Heart-disease target label; commonly | Qualitative, Binary     | Target Variable; outcome to be
# |          | 1 = disease present, 0 = absent.     | (target)                | predicted/classified. Dataset contains
# |          | Confirm using source documentation.  |                         | 165 rows coded 1 and 138 coded 0.
# |----------|--------------------------------------|-------------------------|-----------------------------------------
#
# ==============================================================================
