# Email-Campaign-Manager

## Table of Contents
1. [Configuration Setup](#configuration-setup)
2. [Testing Add Subscriber API](#testing-add-subscriber-api)
3. [Testing Remove Subscriber API](#testing-remove-subscriber-api)


### Configuration Setup
1) Open Command Prompt and  enter the following command - git clone https://github.com/Mayankrai01/Email-Campaign-Manager.git
2) Open the emaildb2.sql in workbench and execute all the commands to create tables
3) Now open the code editor and browse to the newly created folder using the command - cd Email-Campaign-Manager
4) Run the following command to create a new conda virtual environment in current folder- conda create -p ./venv python=3.8 -y
5) Enter Command - conda activate venv/
6) Run the command - {pip install -r requirements.txt} to install the required libraries
7) In the config.py file, set up your MySQL database configuration:
8) Enter Command -> python campaignFunctions.py
9) Note Down the server and port and open brower and paste it in url box for testing purpose (below image is for reference)
![image](https://github.com/Mayankrai01/Email-Campaign-Manager/assets/103130321/bb456abf-23b6-4885-8f47-17e8278f3995)



### Testing Add Subscriber API
1) Edit the URL to - http://127.0.0.1:5000/subscribe
2) Set Request to POST METHOD
3) Add the data given below in body->raw->json
4) Note-Either User Email is an admin or they are the same user as Customer Email, since either the admin or the user itself can add customer in database
5) {
    User Email:m@g.com
    Password: 1234
    Customer Email:mayank.101120@gmail.com
    First Name: mayank
  }
6) Run the following command in your MYSQL workbench to check if the users are added- {select * from Subscribers;}
7) It would reflect the changes along with their details

### Testing Remove Subscriber API
1) Edit the URL to - http://127.0.0.1:5000/subscribe
2) Set Request to POST METHOD
3) Add the data given below in body->raw->json
4) Note-Either User Email is an admin or they are the same user as Customer Email, since either the admin or the user itself can remove customer from database
5) {
    User Email:m@g.com
    Password: 1234
    Customer Email:mayank.101120@gmail.com
    Reason: Provide any reason
  }
6) Run the following command in your MYSQL workbench to check if the users are added- {select * from Subscribers;}
7) It would reflect the changes along with their details
