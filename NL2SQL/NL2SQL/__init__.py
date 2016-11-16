"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.debug = True

import NL2SQL.views
import NL2SQL.DBTasks

