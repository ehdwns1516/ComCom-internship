FROM python:3.9.6

RUN pip install flask
RUN pip install -U transformers
RUN pip install requests
RUN pip install torch --no-cache-dir

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

