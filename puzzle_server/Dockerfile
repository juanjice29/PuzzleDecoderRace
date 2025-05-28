FROM python:3.9-slim

WORKDIR /app
COPY puzzle_server.py .

RUN pip install flask

EXPOSE 8080
CMD ["python", "puzzle_server.py"]