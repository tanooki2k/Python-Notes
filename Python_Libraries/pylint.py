"""
This file contains the definition of our Flask application

It also runs the app if the file is executed.
"""
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
