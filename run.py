from app import app
import os
import logging

if not os.path.exists('log'):
        os.makedirs('log')

logging.basicConfig(filename='log/app.log', level=logging.INFO)

if os.getuid() != 0:
  log.error('This applications requires elevations')
  print('This applications requires elevations')

app.debug = True
app.run(host='0.0.0.0', port=80)
