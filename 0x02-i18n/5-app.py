#!/usr/bin/env python3
'''flask babel module'''

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Union


app = Flask(__name__)


class Config(object):
    '''Flask Bebel configuration'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    '''get a user'''
    login_as = request.args.get('login_as')
    if login_as:
        user = users.get(int(login_as))
        return user
    return None


@app.before_request
def before_request():
    '''before request op'''
    user = get_user()
    g.user = user


@app.route('/')
def index() -> str:
    '''index page'''
    home_title = gettext('home_title')
    return render_template('5-index.html', home_title=home_title)


@babel.localeselector
def get_locale() -> str:
    '''get the best match for supported langs'''
    data = request.args.get('locale')
    if data in app.config['LANGUAGES']:
        return data
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
