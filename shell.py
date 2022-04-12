import subprocess

def execute(command):
    with subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) as proc:
        return proc.stdout.read().decode()