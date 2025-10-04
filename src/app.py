import subprocess #nosec
import shlex

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command_safe(cmd):
    if isinstance(cmd, str):
        args = shlex.split(cmd)
    else:
        args = cmd

    allowed_bins = {'echo', 'ls', 'date'}
    if args and args[0] not in allowed_bins:
        raise ValueError("Perintah tidak diizinkan")

    result = subprocess.run(args, capture_output=True, text=True) #nosec
    return result.stdout
