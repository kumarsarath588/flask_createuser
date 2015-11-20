import subprocess
import crypt

username = 'sarath12'
password ="Pass@word1" 

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


def createUser(user,passwd,homedir,shell):
  try:
    if not user and not passwd:
      print("Error Please enter Username/Password")
      return 1
    if userExistance(user) == 0:
      print("User: {} already exists".format(user))
      return 1
    encPass = crypt.crypt(passwd,"22")
    args = ['useradd', '-p', encPass, user]
    if homedir:
      args.extend(['-d', homedir])
    if shell:
      args.extend(['-s',shell])
    print(' '.join(args))
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
    print(cmd.returncode)
  except:
    print("Error occured while executing")

createUser(user=username,passwd=password,homedir='/home/sk10934',shell='/bin/bash')

def modifyUser(user,passwd,homedir,shell):
  try:
    if not user:
      print("Error Please enter Username/Password")
      return 1
    if userExistance(user) != 0:
      print("User: {} dosen't exists".format(user))
      return 1
    args = ['usermod']
    if passwd:
      encPass = crypt.crypt(passwd,"22")
      args.extend(['-p', encPass])
    if homedir:
      args.extend(['-d', homedir])
    if shell:
      args.extend(['-s',shell])
    args.append(user)
    print(' '.join(args))
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
    print(cmd.returncode)
  except:
    print("Error occured while executing user modification")
password='pass,123'
modifyUser(user=username,passwd=password,homedir='/home/skumar',shell='/bin/ksh')

def deleteUser(user):
  try:
    if not user:
      print("Error Please enter Username/Password")
      return 1
    if userExistance(user) != 0:
      print("User: {} dosen't exists".format(user))
      return 1
    args = ['userdel', user]
    print(' '.join(args))
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
    print(cmd.returncode)
  except:
    print("Error occured while executing user deletion")
  
deleteUser(user=username)

def sudoPrevilege(user):
  found = False
  try:
    args = "{} ALL=(ALL) NOPASSWD:ALL".format(user)
    with open('/etc/sudoers') as sudoersFile:
      for line in sudoersFile:
        if str(args) in line:
          return 0
          found = True

    if not found:
      with open('/etc/sudoers', 'a') as sudoersFileAppend:
        sudoersFileAppend.write(str(args)+"\n")
        sudoersFileAppend.close()
    return 0
  except:
    msg = "Unable to add user '{}' to sudoers.".format(user)
    return 1
sudoPrevilege(user=username)
