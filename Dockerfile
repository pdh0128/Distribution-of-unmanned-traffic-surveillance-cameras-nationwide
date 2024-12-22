# 베이스 이미지로 python:3.11-slim 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 요구 사항 파일을 컨테이너에 복사
COPY requirements.txt .

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 포트 9000을 외부에 노출
EXPOSE 9000

# uvicorn으로 FastAPI 앱 실행
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]
