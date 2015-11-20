import subprocess
import crypt

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
