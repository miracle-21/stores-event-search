FROM python:3.8

# Install app dependencies
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy app code
COPY . /app/

# Start app
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
