from subprocess import PIPE, run

def execute(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    if result.stderr:
        print('<Error>', result.stderr)
    return result.stdout