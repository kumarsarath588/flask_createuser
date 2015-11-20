import subprocess

username = 'kumarsarath588'
if not username.isalnum():
  print("Username {} can only contain [a-z,A-z,1-9]".format(username))

def userExistance(username):
  try:
    args = ['gettent', 'passwd', username]
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
    print(cmd.returncode)
  except:
    print("Error occured while executing '{}'".format(' '.join(args)))

userExistance('root')
