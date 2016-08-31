# Example of how to invoke a remote call using fabric.
# Execute the following command: fab -f fab_run.py -H localhost iso
from fabric.api import run

def iso():
    run('date -u')