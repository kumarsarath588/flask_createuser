from app import app
from flask import render_template,url_for

@app.route('/')
def index():
  print(url_for('user'))
  #processes ="<a href='" + url_for('user') + "'>user</a>"
  processes = url_for('user')
  return render_template('index.html',processes = processes)
