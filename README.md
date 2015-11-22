# flask_createuser


Flask web application is a web based automation platform which is written in python using flask and jinja modules.

##Prerequisites:
####Python 3.4.3
#####Flask Module

This web application has a index page with all the process and each process inturn has some inputs to be given. This application is very light weight as its for testing i will continue to add some more process along with remote execution. This currently supports local user mangement. 

##Try:

1. Clone the repository, install Python 3.4.3.
2. Create a python virtual environment (Recomended).
3. Start the application

`Python run.py`

4.  The above command start the application on port number 80.
5.	Now open your browser go to IP address of the server where you started the application like http://<IPaddress>.
6.	You can see a welcome page click on linux user management.
7.	Type username and password (remaining are optional).
8.	Press submit; Now check in the server it will have user which you have created.


`getent passwd <username>`

Note: This application should run as root or with sudo permissions.
