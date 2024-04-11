# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /directory_name

# Copy the current directory contents into the container at /app
COPY . /directory_name

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
