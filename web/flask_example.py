from flask import Flask, render_template, request

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

@app.route('/jinja2/say/<thing>/<place>')
def jinja2_template2(thing, place):
    return render_template('flask3.html', thing=thing, place=place)

# http://localhost:9999/getparams/echo/?thing=bazooka&place=nkandla
@app.route('/getparams/echo/')
def get_params():
    thing_value = request.args.get('thing')
    place_value = request.args.get('place')
    return render_template('flask3.html', thing=thing_value, place=place_value)

# http://localhost:9999/dictargs/echo/?thing=bazooka&place=Braggi
@app.route('/dictargs/echo/')
def dictionary_args():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html', **kwargs)

app.run(port=9999, debug=True)