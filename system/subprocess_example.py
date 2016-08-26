# Example of how to execute a subprocess with a command
import subprocess

result = subprocess.getoutput('ps -ef | grep python')
print(result)

output = subprocess.check_output(['date', '-u'])
print(output)

# Show the exit status and output as a tuple result
exit_status_and_output = subprocess.getstatusoutput('date')
print(exit_status_and_output)

# Only show the exit status
exit_status_only = subprocess.call('date')
print(exit_status_only)
