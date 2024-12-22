import pandas as pd
pd.set_option('display.max_colwidth', None)  # None으로 설정
df = pd.read_csv('전국 무인 교통 단속 카메라 데이터.csv', encoding='euc-kr')
df = df.dropna(subset=["위도", "경도"])
df = df.sample(frac=1)
df = df[:10000]

import folium

m = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=10)
for idx, row in df.iterrows():
  folium.CircleMarker(
      location=[row['위도'], row['경도']],
      tooltip=row['설치장소'],  
      radius=4,
      color="blue",
      fill=True,
      fill_opacity=0.8,
  ).add_to(m)

m.save('index.html')


