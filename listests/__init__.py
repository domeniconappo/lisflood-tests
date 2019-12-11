import logging
import subprocess
import sys


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.propagate = False

settings = {'ECD': 'settings_full_efas_day.xml',
            'EC6': 'settings_full_efas_6hourly.xml',
            'EWD': '',
            'EW6': '',
            'GCD': '',
            'GWD': ''}


def run_command(cmd):
    logger.info(f'>>>>Executing....:\n{cmd}\n')
    p = subprocess.Popen(args=(cmd,),
                         stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.STDOUT, universal_newlines=True)
    # Poll process for new output until finished
    while True:
        nextline = p.stdout.readline()
        if nextline == '' and p.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()
    if p.returncode:
        raise subprocess.CalledProcessError(p.returncode, cmd)
