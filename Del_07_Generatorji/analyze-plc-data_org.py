#%%
import pandas as pd
from dateutil.parser import parse as duparse
import plotly.graph_objects as go
import datetime
import os

#%%
input_file = "20200915 081812_10_2_6_26.csv"
resample = 60
base = os.path.splitext(input_file)[0]
convertedPath = f"{base}-converted.csv"

# clean csv file and convert it to clean form
if not os.path.exists(convertedPath):
    s = open(input_file).read()
    s = s.replace('"=""', "").replace('"', "")
    f = open(convertedPath, "w")
    f.write(s)
    f.close()

#%%
df_log = pd.read_csv(convertedPath, delimiter=";", low_memory=False)
# convert to datetime
df_log["Time"] = pd.to_datetime(df_log["Time"], yearfirst=True)

# convert type column to category
df_log.Type = df_log.Type.astype("category")

# do some stats:
timespan = df_log.Time.max() - df_log.Time.min()

# make clone of column Time and set column Time as index
df_log["original Time"] = df_log["Time"]
df_log = df_log.set_index("Time")

#%%

df_log_rrep = df_log[df_log.Type.str.contains("LOADNG RREP", na=False)]

comment = f"Observing time: {timespan}."
print(comment)
#%%
# reindex df

groups_rrep = (
    df_log_rrep["Type"].resample(f"{resample}T", label="right", closed="right").count()
)

df_result = pd.DataFrame(groups_rrep)

# df_result.to_excel('df_result.xlsx')
#%%
chart = go.Figure()
chart.add_trace(
    go.Bar(
        x=df_result.index, y=df_result.Type, name="# of rrep", marker=dict(color="red")
    )
)

chart.update_traces(opacity=0.7)


chart.write_html(f"{base}_resampleTo{resample}min.html")

# %%
