FROM python

WORKDIR .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["python", "/app/app.py"]
