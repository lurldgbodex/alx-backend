#!/usr/bin/env python3
'''flask babel module'''

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    '''Flask Bebel configuration'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    '''index page'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
