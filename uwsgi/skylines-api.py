import os
import sys
import argparse
from config import to_envvar

parser = argparse.ArgumentParser(description='Run the SkyLines API UWSGI application.')
parser.add_argument('config_file', nargs='?', metavar='config.ini',
                    help='path to the configuration INI file')
args = parser.parse_args()

if not to_envvar(args.config_file):
    parser.error('Config file "{}" not found.'.format(args.config_file))

sys.path.append(os.path.dirname(sys.argv[0]))

from skylines import create_api_app
application = create_api_app()
