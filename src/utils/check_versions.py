import logging
import sys
import subprocess
import shutil

def check_versions():
    """Get versions of external dependencies"""

    flag = 0

    command_path = shutil.which("amrfinder")
    if command_path:
        try:
            result = subprocess.run(['amrfinder', '--version'], capture_output=True, text=True)
            amrfinder_ver = result.stdout.strip()
            logging.info(f'amrfinder ver :\t{amrfinder_ver}')
        except subprocess.CalledProcessError as e:
            logging.warning('amrfinder version not found!')
            logging.warning(e)
    else:
        logging.fatal('FATAL: amrfinder not found')
        flag = 1
    
    command_path = shutil.which("amrfinder")
    if command_path:
        try:
            result = subprocess.run(['amrfinder', '--database_version'], capture_output=True, text=True)
            amrfinder_db_ver = result.stdout.strip().split('\n')[3].split()[-1]
            logging.info(f'amrfinder db ver :\t{amrfinder_db_ver}')
        except subprocess.CalledProcessError as e:
            logging.fatal('amrfinder db not found!')
            logging.fatal(e)
    else:
        logging.fatal('FATAL: amrfinder db not found')
        flag = 1

    command_path = shutil.which("blastn")
    if command_path:
        try:
            result = subprocess.run(['blastn', '-version'], capture_output=True, text=True)
            blast_ver = result.stdout.strip().split()[1]
            logging.info(f'blast ver :\t{blast_ver}')
        except subprocess.CalledProcessError as e:
            logging.fatal('blastn not found!')
            logging.fatal(e)
    else:
        logging.fatal('FATAL: blastn not found')
        flag = 1

    command_path = shutil.which("seqkit")
    if command_path:
        try:
            result = subprocess.run(['seqkit', 'version'], capture_output=True, text=True)
            seqkit_ver = result.stdout.strip().split()[1]
            logging.info(f'seqkit ver :\t{seqkit_ver}')
        except subprocess.CalledProcessError as e:
            logging.fatal('seqkit not found!')
            logging.fatal(e)
            flag = 1
    else:
        logging.fatal('FATAL: seqkit not found')
        flag = 1

    if (flag == 1):
        logging.fatal("FATAL: Could not find all dependencies!")
        sys.exit(1)
