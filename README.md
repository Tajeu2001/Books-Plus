# Books Plus




## Prerequisites

* Text Editor
* Python3
* Git

## Getting Started

* Install git in your computer.
* Open termimal.
* Clone the repository using the command $git clone.
* You will now have the repository in your local folder.


### Setup and Installation  
To get the project .......    
##### Cloning the repository:  
 ```bash 
git clone https://github.com/Tajeu2001/Books-Plus.git
```
##### Navigate into the folder 
 ```bash 
cd books-plus
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
pip install -r requirements.txt 
```  
##### Setup Database  
SetUp your database User,Password, Host then make migrations
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
python3.8 manage.py migrate 
```
##### Run the application  
 ```bash 
python3.8 manage.py runserver 
```  
##### Testing the application  
 ```bash 
python3.8 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

### View of the application homepage

![alt text]()

### View of the single hood page


![alt text]()

## User Story

* Users get to sign up and login
* 


## Deployment

Deploy the project to heroku.

## Built With

* Django2.2
* Python3.8
* Bootstrap
* Javascript

## Live link




## Author

* Rosemary Siantayo Tajeu

## Contact details
Email: tajeusanta7@gmail.com

### License
This is under the [MIT](LICENSE) license 