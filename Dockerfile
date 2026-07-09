FROM python:3.11-slim

WORKDIR /app

# COPY source dest

COPY requirements.txt .

# RUN command
RUN pip install --no-cache-dir -r requirements.txt

# COPY source dest

COPY . .

# EXPOSE port
EXPOSE 8000

# CMD [ "executable" ]
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]

