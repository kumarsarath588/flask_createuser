from app import app
from flask import render_template,request
from app.user.actions import createUser,userExistance,modifyUser,deleteUser,sudoPrevilege
import logging as log

@app.route('/user', methods = ['GET', 'POST'])
def user():
  if request.method == 'GET':
     return render_template('user/user_action.html')
  elif request.method == 'POST':
     username = request.form['username']
     password = request.form['password']
     homedir = request.form['homedir']
     shell = request.form['shell']
     operation = request.form['operation']
     sudo = request.form['sudo']
     if operation.lower() == 'create' and ( not username or not password ):
       msg="Username/Password is missing."
       log.error(msg)
       return render_template('error.html',msg=msg)
     elif not username:
       msg="Username is mandate for delete/modify operation."
       log.error(msg)
       return render_template('error.html',msg=msg)
     if not username.isalnum():
       msg="Username can only contain [a-z,A-z,1-9] no special characters. You passed : {}.".format(username)
       log.error(msg)
       return render_template('error.html',msg=msg)
     if operation.lower() == 'create':
       if userExistance(user=username) == 0:
         msg = "User: {} already exists".format(username)
         log.error(msg)
         return render_template('error.html',msg=msg)
       if createUser(user=username,passwd=password,homedir=homedir,shell=shell) != 0:
         msg="User '{}' Creation failed.".format(username)
         log.error(msg)
         return render_template('error.html',msg=msg)
       msg="User '{}' Created Successfully.".format(username)
       log.info(msg)
       if sudo == 'true':
         if sudoPrevilege(user=username) != 0:
           msg="User '{}' Created Successfully, but sudo previlege failed".format(username)
           log.error(msg)
           return render_template('error.html',msg=msg)
         msg="User '{}' Created Successfully, sudo previlege success".format(username)
         log.info(msg)
       return render_template('success.html',msg=msg)
     elif operation.lower() == 'modify':
       if not password and not shell and not homedir and sudo != 'true':
         msg = "Nothing to modify for user: {}".format(username)
         log.warn(msg)
         return render_template('error.html',msg=msg)
       if userExistance(user=username) != 0:
         msg = "User: {} dosen't exists".format(username)
         log.error(msg)
         return render_template('error.html',msg=msg)
       if password or shell or homedir:
         if modifyUser(user=username,passwd=password,homedir=homedir,shell=shell) != 0:
           msg="User '{}' modification failed.".format(username)
           log.error(msg)
           return render_template('error.html',msg=msg)
         msg="User '{}' modified Successfully.".format(username)
       if sudo == 'true':
         if sudoPrevilege(user=username) != 0:
           msg="User '{}' modified Successfully, sudo previlege failed".format(username)
           log.error(msg)
           return render_template('error.html',msg=msg)
         msg="User '{}' modified Successfully, sudo previlege success".format(username)
         log.info(msg)
       return render_template('success.html',msg=msg)
     elif operation.lower() == 'delete':
       if userExistance(user=username) != 0:
         msg = "User: {} dosen't exists".format(username)
         log.error(msg)
         return render_template('error.html',msg=msg)
       if deleteUser(user=username) != 0:
         msg="User '{}' deletion failed.".format(username)
         log.error(msg)
         return render_template('error.html',msg=msg)
       msg="User '{}' deleted  Successfully.".format(username)
       log.info(msg)
       return render_template('success.html',msg=msg)
