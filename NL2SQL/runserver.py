"""
This script runs the NL2SQL application using a development server.
"""

from os import environ
from NL2SQL import app

if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = '127.0.0.1'
    try:
        #PORT = int(environ.get('SERVER_PORT', '5555'))
        PORT = 5557
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
