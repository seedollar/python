from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('flask-home.html')

@app.route('/say/<thing>')
def say(thing):
    return "Flask response says: %s" % thing

@app.route('/jinja2/say/<thing>')
def jinja2_template(thing):
    return render_template('flask2.html', thing=thing)

app.run(port=9999, debug=True)