from app import app
from flask import render_template,request

@app.route('/user', methods = ['GET', 'POST'])
def user():
  if request.method == 'GET':
     return render_template('user/user_action.html')
  elif request.method == 'POST':
     username = request.form['username']
     password = request.form['password']
     homedir = request.form['homedir']
     shell = request.form['shell']
     return 'Successfully submited' + ' '.join([username, password, shell, homedir])
