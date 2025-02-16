# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /WDP

# Copy the current directory contents into the container at /app
COPY . .

#create 

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# Expose the port that the Django app runs on
EXPOSE 8000

# Run migrations and start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
