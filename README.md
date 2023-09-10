# Email-Campaign-Manager

## Table of Contents
1. [Configuration Setup](#configuration-setup)
2. [Testing Add Subscriber API](#testing-add-user-api)
3. [Testing Remove Subscriber API](#testing-delete-movies-api)


### Configuration Setup
1) Open Command Prompt and  enter the following command - git clone https://github.com/Mayankrai01/MovieDatabase.git
2) Open the MovieDatabase.sql in workbench and execute all the commands to create tables
3) Now browse to the newly created folder using the command - cd MovieDatabse
4) Run the following command to create a new conda virtual environment in current folder- conda create -p ./venv python=3.8 -y
5) Enter Command - conda activate venv/
6) Run the command - {pip install -r requirements.txt} to install the required libraries
7) In the config2.py file, set up your MySQL database configuration:
8) Enter Command -> python addListFromJson.py , this will add the movies in the imdb.json file to the database
9) Enter Command -> python userFunctions.py
10) Note Down the server and open postman and paste it in url box (below image is for reference)
![image](https://github.com/Mayankrai01/MovieDatabase/assets/103130321/4099fe2c-8708-488e-8bd0-062bb532bcd5)



### Testing Add Subscriber API
1) Edit the URL to - http://127.0.0.1:5000/adduser
2) Set Request to POST METHOD
3) Add the data given below in body->raw->json
4) {
    "name":"testuser",
    "email":"testuser@g.com",
    "isAdmin":false,
    "password":"passwordtest2"
  }
5) {
    "name":"testadmin",
    "email":"admin@g.com",
    "isAdmin":true,
    "password":"adminpass"
  }
6) Run the following command in your MYSQL workbench to check if the users are added- {select * from user;}
7) It would show the two users with their names

### Testing Remove Subscriber API
1) Edit the URL to -http://127.0.0.1:5000/movies
2) Method - DELETE
3) Add the data given below in body->raw->json
4) {
    "name":"The Big Bang Theory",
    "user_email":"admin@g.com",
    "entered_password":"adminpass",
    "popularity":"92",
    "imdb_score":8.8,
    "director":"Chuck Lore"
  }
5) See the updated movies table and the movie "Big Bang Theory" would be deleted
