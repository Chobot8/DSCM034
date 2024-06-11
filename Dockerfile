# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest for testing
RUN pip install pytest

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run tests and then start the server
CMD ["sh", "-c", "pytest && uvicorn app:app --host 0.0.0.0 --port 5000"]
