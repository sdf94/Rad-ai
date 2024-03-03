FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]