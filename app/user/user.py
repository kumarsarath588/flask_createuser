from app import app
from flask import render_template,request

@app.route('/user', method = ['GET', 'POST'])
  if request.method == 'GET':
     return render.template('user/user_action.html')
  elif request.method == 'POST':
     username = request.data['username']
     password = request.data['password']
     shell = request.data['shell']
     return 'Successfully submited' + username + password + shell
