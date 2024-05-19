# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

FROM python:3.8.5-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1


# Updating docker and installing aws cli
RUN apt-get update -y && apt-get install apt-transport-https ca-certificates gnupg curl -y

# RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
# RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
# RUN apt-get update && apt-get install google-cloud-cli -y

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
         | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
         curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
         | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \ 
         apt-get update -y && \
         apt-get install google-cloud-sdk -y

# Initiate google cloud authetication by running below command - 
    # docker run -d -p 8080:8080 hate_speech_classifiaction:latest` - This will run the container.
    # docker ps -a  - To view the running container
    # Synatx to get into a running container - docker exec --it [container_name] [shell]
    # docker exec --it nervous_wright bash
    # Run the below command and follow the instructions
    # gcloud init

# Setting Work Directory
WORKDIR /app

# Copy the source code into the container.
COPY . /app

# To signify root directory of application
RUN touch /app/.project-root

# To install all dependencies
RUN pip install -r requirements.txt


# Expose the port that the application listens on.
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app:HateSpeechClassificationapp", "--reload","--host", "0.0.0.0", "--port", "8080"]
# uvicorn app:HateSpeechClassificationapp --reload --host=0.0.0.0 --port=8000
