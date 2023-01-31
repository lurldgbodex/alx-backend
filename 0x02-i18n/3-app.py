#!/usr/bin/env python3
'''flask babel module'''

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
    home_title = gettext('home_title')
    return render_template('3-index.html', home_title=home_title)


@babel.localeselector
def get_locale() -> str:
    '''get the best match for supported langs'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
