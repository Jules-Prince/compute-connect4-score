FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY src ./src

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "src.main:app", "--reload"]