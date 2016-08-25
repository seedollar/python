# Shows how to use the "bottle" library

from bottle import route, run, static_file

@route('/')
def home():
    return "This is bottle's home page"

@route('/fancy')
def fancy():
    return static_file('fancy.html', root='.')

@route('/say/<thing>')
def say(thing):
    return "You said: %s!" % thing

run(host='localhost', port=9999)