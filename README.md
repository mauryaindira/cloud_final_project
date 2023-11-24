# cloud_final_project

Step 1: Create an flask application(Web_app.py) and running the file on web url.

Step 2: create a Requirement file (req.text)

    flask
    sqlite3
    google-cloud-pubsub


Step 3: Create a Dockerfile FROM python:3.6 WORKDIR /app COPY . . RUN pip install -r req.txt EXPOSE 80 CMD ["python", "cloud_asign1.py"]

Command: sudo docker build -t flask_app .

 # Docker file will pull the python: 3.6
 # Now will it will create directory with the 'app' name.
 # It will copy the files from root directory to docker file
 # Now it will install the requirement file 
 # It expose the app on port 80
 # CMD run python file cloud_assign1.py
Step 4: sudo docker run -p 80:80 flask_app:latest

    This command will run the image on port 80.


    
Author : Indira Maurya

Roll Number: M21AIE228