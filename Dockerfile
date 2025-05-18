FROM python:3.13.3-alpine3.21
WORKDIR /app
COPY main.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["2", "2"]