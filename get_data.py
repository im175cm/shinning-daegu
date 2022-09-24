#!/usr/bin/python3.9

import pandas as pd
import requests
import datetime


def time_set():
    now = datetime.datetime.now()

    dt = datetime.timedelta(days = 180)

    start = now.strftime("%Y%m%d")
    end =  (now + dt).strftime("%Y%m%d")

    return start, end
def get_data():
    API_base = "http://www.kopis.or.kr/openApi/restful/pblprfr"

    subsggcode = {
        "동구" : 2714,
        "서구": 2717,
        "남구" :2720,
        "북구" : 2723,
        "중구" : 2711,
        "수성구" : 2726,
        "달서구": 2729,
        "달성군": 2771,
    }
    
    start, end = time_set()

    params = {
        "service" : "09c941a6cb2d4808a660fbc6640350c2",
        "stdate" : start,
        "eddate" : end,
        "cpage" : "1",
        "signgucode" : 27,
        "signgucodesub" : 2771,
        "rows" : "1000"
    }

    df_list = []

    for k, v in subsggcode.items():
        params['signgucodesub'] = v
        res = requests.get(API_base, params=params)
        try:
            df = pd.read_xml(res.content)
            df['SGG'] = k
        except ValueError:
            continue
        df_list.append(df)

    result = pd.concat(df_list, axis=0)
    result = result.reset_index(drop=True)
    return result

if __name__=="__main__":
    data = pd.read_csv('data.csv')
    df = get_data()
    data = pd.concat([data, df], axis=1)
    data = data.drop_duplicates(['mt20id'])
    print(data.shape)
    df.to_csv('data.csv', index=False)
    print("Done")