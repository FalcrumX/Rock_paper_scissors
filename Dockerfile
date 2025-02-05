FROM python:3.11
WORKDIR /app
COPY Rock_paper_scissors.py /app/RPS.py
CMD ["python", "RPS.py"]

