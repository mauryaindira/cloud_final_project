# cloud_final_project

Step 1: Create an flask application(Web_app.py), Subscriber file, and running the file on web url.

Step 2: Created HTML pages (Order and Thankyou)

Step 3: Established a Database connection with db.sqlite3

Step 4: Istall and configure a gcp pub/sub connection on local host machine. 

               Refer Doc: https://cloud.google.com/sdk/docs/install

               https://cloud.google.com/python/docs/reference/pubsub/latest

Step 5: Created the Project ID, Topic ID and subscription ID(will we used while establishing the connection with application)

Step 6: create a Requirement file (req.text)

            flask

            sqlite3

            google-cloud-pubsub


Step 7: Run the flask application and use the local host weburl(e.g : http://127.0.0.1:5000)  

Step 8: Raise the request from Weburl for the order items 

Steps 9: Successfully order submitted and confimration page appears (e.g: Thank you for your order! We will be in touch shortly to confirm your order details.)
 
Step 10: Checked the Pub and sub queue for the multiple oders simultaneously.

Step 11: checked the database for the for proper data entry.
            Using Follwing commands:

             sqlite3 <database_name.db>

             .table

             select *from <table_name>


Step 10: checked the subsciber for reciving all the messages(Run python file) :

            python <subciber_file name.py>
            

Author : Indira Maurya

Roll Number: M21AIE228