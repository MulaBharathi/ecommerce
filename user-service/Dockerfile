FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN ls -l /app

# Upgrade pip and install the dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the application port
EXPOSE 5003


# Run the Flask app with Gunicorn
CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:5003"]
