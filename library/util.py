import subprocess
from functools import wraps

def command(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return subprocess.call(f(*args,**kwargs))

    return wrapper