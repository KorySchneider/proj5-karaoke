import flask, logging, json
from flask import jsonify

# Globals
import CONFIG
import map_key
app = flask.Flask(__name__)
app.secret_key = CONFIG.secret_key

@app.route('/')
@app.route('/index')
def index():
    flask.session['locations'] = []
    for loc in get_poi():
        flask.session['locations'].append(loc)
    return flask.render_template('index.html')

# Ajax handlers
@app.route('/_poi')
def _poi():
    locations = get_poi()
    return jsonify(locations)

@app.route('/_map_key')
def _map_key():
    return jsonify(key=map_key.key)

# Helper functions
def get_poi():
    with open('poi.json') as poi:
        locations = json.load(poi)
    return locations


if __name__ == '__main__':
    if CONFIG.debug:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
    else:
        app.debug=False

    app.run(port=CONFIG.port, host='0.0.0.0')
