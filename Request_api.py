import json
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

API_KEY = "a5b0b768-1a25-447d-a242-01a6495c1831"

request_txt = f"https://api.rasp.yandex.net/v3.0/stations_list/?apikey={API_KEY}&lang=ru_RU&format=json"
getpage= requests.get(request_txt)
getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

s = json.loads(str(getpage_soup))
s.keys()

s['countries']

with open("stations.json", "w") as writer:
    json.dump(s, writer)
    
with open("stations.json", "r") as reader:
    data = json.load(reader)
    
data['countries'][24]['regions']

codes = {}
n=0
for idx, country in enumerate(data['countries']):
    for idx2, region in enumerate(country['regions']):
        for idx3, settlement in enumerate(region['settlements']):
            for idx4, station in enumerate(settlement['stations']):
                code = station
                try:
                    code['codes'] = code['codes']['yandex_code']
                except Exception as e:
                    print(f"{type(e)}: {e} [{code['codes']}]")
                    code['codes'] = np.nan
                if n%10000 == 0:
                    print(code)
                codes.update({n:code})
                n+=1
                
codes.keys()

train_df = code_df.loc[(code_df.transport_type=='train') & (code_df.longitude != "")].drop(['direction'], 1)
print(train_df.shape)
train_df.sample(10)

train_df[train_df.title == 'Внуково']

train_df[train_df.title == 'Самара']

train_df.to_csv("train.csv")

S_START, S_END = 's9606096', 's9602271'
API_KEY = "a5b0b768-1a25-447d-a242-01a6495c1831"
request_txt = f"https://api.rasp.yandex.net/v3.0/search/?apikey={API_KEY}&format=json&from={S_START}&to={S_END}&transport_types=train"
getpage= requests.get(request_txt)
getpage_soup= BeautifulSoup(getpage.text, 'html.parser')
json.loads(str(getpage_soup))

with open("getpage_soup.json", "w") as writer:
    json.dump(s, writer)