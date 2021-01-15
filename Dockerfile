FROM python:3.8

WORKDIR /usr/src/app

COPY config/requirements.txt ./config/
RUN pip install --no-cache-dir -r ./config/requirements.txt

COPY main.py ./
COPY __init__.py ./
COPY models/ ./models/

CMD ["python", "-u", "main.py"]
