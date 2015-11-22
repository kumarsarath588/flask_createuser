import subprocess
import crypt

"""
  This contains actions for user management user existance/create/modify/delete.
  User.py uses these actions and controls the operations.
"""

def userExistance(user):
  try:
    args = ['getent', 'passwd', user]
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
  except:
    msg = "Error occured while executing '{}'".format(' '.join(args))
    return 1


def createUser(user,passwd,homedir,shell):
  try:
    encPass = crypt.crypt(passwd,"22")
    args = ['useradd', '-p', encPass, user]
    if homedir:
      args.extend(['-d', homedir])
    if shell:
      args.extend(['-s',shell])
    msg = "Executing {}.".format(' '.join(args))
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
  except:
    msg = "Error occured while executing: {}.".format(' '.join(args))
    return 1

def modifyUser(user,passwd,homedir,shell):
  try:
    args = ['usermod']
    if passwd:
      encPass = crypt.crypt(passwd,"22")
      args.extend(['-p', encPass])
    if homedir:
      args.extend(['-d', homedir])
    if shell:
      args.extend(['-s',shell])
    args.append(user)
    msg = "Executing {}.".format(' '.join(args))
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
  except:
    msg = "Error occured while executing user modification: {}".format(args)
    return 1

def deleteUser(user):
  try:
    args = ['userdel', user]
    msg = "Executing {}.".format(' '.join(args))
    cmd = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    return cmd.returncode
  except:
    msg = "Error occured while executing user deletion: {}.".format(' '.join(args))

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
