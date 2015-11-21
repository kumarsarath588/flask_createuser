# flask_createuser


Flask web application is a web based automation platform which is written in python using flask and jinja modules.

##Prerequisites:
####Python 3.4.3
#####Flask Modules

This web application has a index page with all the process and each process inturn has some inputs to be given. This application is very light weight as its for testing i will continue to add some more process along with remote execution. This currently supports local user mangement. 

##Try:

1. Clone the repository, install Python 3.4.3.
2. Create a python virtual environment (Recomended).
3. Start the application

` Python run.py

4. Now open your browser goto IP address of the server where you started the application like http://<hostname/ip>.
5. You can see a welcome page click on linux user mangement.
6. Type username and password (remaining are optional).
7. Press sumbit, Now check in the server i will have user which you have created.

` getent passwd <username>

Note: This application should run as root or with sudo permissions.
