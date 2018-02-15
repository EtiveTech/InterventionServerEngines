import sys
import logging
logging.basicConfig(filename='C:/Users/phil/Development/_logs/py_log.txt', format='%(asctime)-15s %(message)s', level=logging.DEBUG)
sys.path.insert(0, "c:/users/phil/development/city4Age/interventionsystem/www/engines")
from main import app as application