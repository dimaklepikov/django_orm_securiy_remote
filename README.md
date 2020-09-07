# Bank storage-visit controller
 This is a pet project for organizing a control path for a bank guard
## Functionality:
 - Users in storage with name, enter time, suspicious-control statement
 - Active passcards of users with name, unique passcode, registration date&time
 - Page for each user with his/her list of visits, duration of every visit, suspicious-control statement  
 ## How to install:
 1) Install Python 3,5+
 ```sh
$ pip3 install python
```
 2) Install and activate Virtualenv
  ```sh
$ pip3 install virtualenv
$ virtualenv bank_controller
$ source bank_controller/bin/activate
```
3) Install requirements
 ```sh
$ pip3 install -r requirements.txt
 ```
## How to launch:
 ```sh
$ python3 path/main.py
 ```
### Launch example:
 ```sh
/usr/local/bin/python3.8 /Users/dmitriy/gdrive/projects/learning/django-orm-watching-storage/main.py
Performing system checks...

System check identified no issues (0 silenced).
September 07, 2020 - 20:45:51
Django version 1.11.29, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

 ```