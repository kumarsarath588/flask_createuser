from app import app
from flask import render_template,url_for

@app.route('/')
def index():
  print(url_for('user'))
  processes = url_for('user')
  return render_template('index.html',processes = processes)
