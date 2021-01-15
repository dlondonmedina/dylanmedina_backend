import sys, os 
INTERP = "/home/api_medinad/api.dylanmedina.com/env/bin/python3"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from app import app as application