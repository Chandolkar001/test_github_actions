FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN ls
CMD ["python", "app.py"]
