from app import app
import os

if os.getuid() != 0:
  print("This applications requires elevations")

app.debug = True
app.run(host='0.0.0.0', port=80)
