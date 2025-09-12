FROM alpine:latest
RUN apk add --no-cache python3 py3-pip
WORKDIR /app
COPY HiveBox.py .
CMD ["python3", "/app/HiveBox.py"]
