__author__ = 'Brandon'
from webApp.app import app
import os

if __name__ == '__main__':
    print(os.getenv("AWS_KEY"))
    app.run(debug=True)