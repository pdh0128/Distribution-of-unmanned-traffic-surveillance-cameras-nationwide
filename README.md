# 전국 무인 교통 단속 카메라 분포

# 1. 프로젝트 폴더 구조
```bash
 ┣ 📂__pycache__
 ┃ ┗ 📜app.cpython-311.pyc
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📜.gitignore
 ┣ 📜Dockerfile
 ┣ 📜app.py
 ┣ 📜map.py
 ┣ 📜requirements.txt
 ┗ 📜전국무인교통단속카메라데이터.csv
```

# 2. 데이터셋

[전국무인교통단속카메라표준데이터](https://www.data.go.kr/data/15028200/standard.do)


# 3. 구현 내용 요약

- 무인 교통단속 카메라의 위치를 확인할 수 있습니다.

# 4. 기술 스택

- 웹프레임워크: FastAPI
- 주요모듈 :  folium, pandas

# 5. 소감 및 향후 계획

- 데이터셋이 너무 큰 탓에 렌더링에 오랜 시간이 걸려, 데이터셋이 30000개이상 있었는데 10000개로 줄여 만들었습니다. 렌더링 시간을 줄이는 방안을 찾아 데이터를 전부 활용하고 싶습니다.

# 6. 상세 내용 보기: 

https://www.notion.so/164b22eecf018033afcefdec36518aa1
