import os
import subprocess
import sys

from dotenv import load_dotenv
import requests

load_dotenv()

url = 'https://www.mydns.jp/directip.html'
id = os.environ.get('MYDNS_ID')
password = os.environ.get('MYDNS_PASSWORD')

if id is None or password is None:
    print('not set id or password! create .env file via .env.sample')
    sys.exit(1)

proc = subprocess.run('curl ifconfig.io'.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ip = proc.stdout.decode().strip()

r = requests.post(url, params={'MID': id, 'PWD': password, 'IPV4ADDR': ip})
if not r.ok:
    print(r.text)

