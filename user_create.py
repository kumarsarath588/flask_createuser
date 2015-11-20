import subprocess

username = 'root'
if not username.isalnum():
  print("Username {} can only contain [a-z,A-z,1-9]".format(username))

def userExistance(username):
  try:
    args = ['getent', 'passwd', username]
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
    print(cmd.returncode)
  except:
    print("Error occured while executing '{}'".format(' '.join(args)))

#userExistanceStatus=userExistance('root')
if userExistance(username) == 0:
  print("User Existed")
else:
  print("User Not exests")
