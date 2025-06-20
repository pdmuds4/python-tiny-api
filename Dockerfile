FROM python:3.12

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "application:app", "--host=0.0.0.0"]