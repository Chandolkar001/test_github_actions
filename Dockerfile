FROM python:3.8-slim
COPY entrypoint.sh /entrypoint.sh
COPY app.py /app.py
CMD ["/bin/ls", "-l"]
