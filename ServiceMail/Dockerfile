FROM python:3.11

WORKDIR /servicemail

COPY . .

RUN pip install --no-cache-dir --upgrade -r /servicemail/requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]