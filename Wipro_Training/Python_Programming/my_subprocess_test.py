# subprocess module

# execute external system commands
# iterate with OS processess
# capture output, error and return codes
# control the process execution

# run the OS level commands - linux , macos , windows

import subprocess

#subprocess.run() - run command and wait
# subprocess.papen() - run process synchronuisy\
# subprocess.PIPE - capture the output
# subprocess.Compltetprocess - result
#subprocess.TimeoutExpired - Time outexecption
# subprocess.calledprocesserror - command failure




result=subprocess.run("dir" , shell = True , capture_output=True, text = True)
print(result)

result = subprocess.run("ipconfig", shell=True, capture_output=True, text = True)
print(result)

result = subprocess.run( "python--version", shell= True, capture_output=True, text = True)
print(result)