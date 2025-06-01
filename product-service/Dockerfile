FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN ls -l /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5002

#CMD ["python", "app.py"]


# Start the Flask app using Gunicorn (replace app with the actual Flask app module if needed)
CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:5002"]
