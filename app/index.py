from app import app
from flask import render_template,url_for

"""
  This is the main app index page which is routed using /
  This index renderes a html page which is dynamic, depends on processes variable,
  as you add in more elements in array, it adds more processes
"""

@app.route('/')
def index():
  processes = [ url_for('user') ]
  return render_template('index.html',processes = processes)
