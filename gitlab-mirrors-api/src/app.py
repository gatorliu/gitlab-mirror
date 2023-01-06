import sys
import os
from datetime import datetime
import traceback
from git import Repo

from flask import Flask, render_template, request, jsonify
import logging
from logging.handlers import TimedRotatingFileHandler


# Config
'''
import configparser
config = configparser.ConfigParser()
try:
    config.read("config/config.ini", encoding='utf-8')
except:
    config.read("config.ini")
MIRROR_SCRIPT_PATH = config.get('GLOBAL', 'MIRROR_SCRIPT_PATH')
'''

app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.info(f'hello_world()')
    return render_template('index.html', url_root=request.url_root)


@app.route('/mirror/<project>')
def mirror(project):
    ret= {'error':0}
    try:
        app.logger.info(f'mirror project: [{project}]: start')
        repo = Repo(os.path.join("repos", project))
        repo.remotes.origin.fetch(prune=True)
        repo.remotes.origin.push(mirror=True)
        
    except:
        t = traceback.format_exc()
        app.logger.error(t)
        ret= {'error':1, 'traceback':t}

    app.logger.info(f'mirror project: [{project}]: done')
    return jsonify(ret)

if __name__ == '__main__':
    app.debug = True
    handler = TimedRotatingFileHandler(
        os.path.join("logs","flask.log"), when="D", interval=1, backupCount=15, encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    app.run(debug=True, host='0.0.0.0')
    
