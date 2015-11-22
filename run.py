from app import app
import os
import logging as log
from sys import exit

"""
  Creating log directory, opening log file for logging all errors and information
  this application requires elevations either root/sudo previlege
  start the flask on 0.0.0.0 and port no 80.
"""

try:
  if not os.path.exists('log'):
        os.makedirs('log')
  log.basicConfig(filename='log/app.log', level=log.INFO)
except:
  print('Not able to open log file, exiting...')
  exit()

if os.getuid() != 0:
  log.error('This applications requires elevations')
  print('This applications requires elevations')
  exit()

app.debug = True
app.run(host='0.0.0.0', port=80)
