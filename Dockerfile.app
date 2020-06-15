FROM python:3.7-slim
WORKDIR webapp/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
