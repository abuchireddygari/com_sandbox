import pandas as pd
from datetime import datetime

num_of_rows=0
num_of_uniq_rows=0

print("creating dataframe: ",datetime.now().strftime("%H:%M:%S"))
# Source - https://www.kaggle.com/code/kerneler/starter-ghtorrent-pull-requests-cd55a31e-4/data?select=ghtorrent-2019-02-04.csv
df_raw=pd.read_csv(r"C:\\6-Temp\data\\github\\ghtorrent-2019-02-04.csv") #, usecols=["actor_login"]) # 18.4 GB on windows 10 ntfs
print("dataframe created: ",datetime.now().strftime("%H:%M:%S"))

print("calculating deep memory usage: ",datetime.now().strftime("%H:%M:%S"))
print(df_raw.memory_usage(deep=True).sum()) # 50400704515

print("calculating total number of rows: ",datetime.now().strftime("%H:%M:%S")) 
num_of_rows+=len(df_raw)
print(num_of_rows) # 94361402

print("calculating unique values: ",datetime.now().strftime("%H:%M:%S"))
num_of_uniq_rows=len(df_raw.groupby(["actor_login"]))
print(num_of_uniq_rows) # 114536
    