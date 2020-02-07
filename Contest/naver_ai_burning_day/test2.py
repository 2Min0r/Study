import pandas as pd
from pandas import DataFrame as df

df1=pd.read_json('[{"created_at": "1997-07-16T19:20:30+01:00", "project": "cobalt-blue", "label_id": "c5fb001e-7c39-4807-a1f4-a5dde6ca93d1", "classes": ["dog", "cat"], "email": "a@gmail.com", "tenant": "blue-team"}]')
print(df1)