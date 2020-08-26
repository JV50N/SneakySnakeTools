FROM python:3.9.0rc1-buster

# MAKE A DIRECTORY FOR OUR APP
WORKDIR /app

# INSTALL DEPENDENCIES
COPY requirements.txt
RUN pip install -r requirments.txt

# COPY OUR SOURCE CODE
COPY /app .

# RUN THE APP
CMD ("python", "recon.py")