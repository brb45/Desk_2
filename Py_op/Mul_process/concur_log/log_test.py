import subprocess

out = subprocess.Popen(['dir'], shell=True, stdout=subprocess.PIPE)


output= out.communicate()[0]
print(type(output))
