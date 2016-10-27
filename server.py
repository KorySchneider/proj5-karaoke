import flask, logging

# Globals
app = flask.Flask(__name__)
import CONFIG

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT, host='0.0.0.0')
