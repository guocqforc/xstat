# -*- coding: utf-8 -*-

import time
from flask import Flask
from xstat import FlaskStat
import user

DEBUG = True

STAT_TITLE = 'dante.test'
STAT_HOST = '127.0.0.1'

app = Flask(__name__)
app.config.from_object(__name__)

app.register_blueprint(user.bp, url_prefix='/user')
flask_stat = FlaskStat(app)


@app.route('/allow')
def allow():
    time.sleep(1)
    return u'ok'


@app.route('/forbid')
def forbid():
    time.sleep(1)
    return u'forbid'

if __name__ == '__main__':
    app.run()
