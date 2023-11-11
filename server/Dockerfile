FROM python:3.11-slim
RUN apt-get update
RUN apt-get install git gcc -y
RUN apt-get clean
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 5010
ENTRYPOINT [ "python", "app.py" ]