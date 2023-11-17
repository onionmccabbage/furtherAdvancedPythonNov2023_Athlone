# Flask solves web server problems by providing a configurable micro service web server
# might need to pip isntall Flask
# Flask is NOT a secure web server - use with Apache or tomcat etc for security
# but for an internal web server it is great

from flask import Flask
from flask import render_template # this is a templating engine

app = Flask(__name__) # this is conventional
# we declare routes for our app
@app.route('/') # '/' is always the root of a website
def root():
    return 'hello and welcome to Flask'
@app.route('/snow')
def snow():
    return 'Here is a picture of Athlone in very deep snow'
# sometimes it is useful to offer several routes to a resource
# e.g. different names for a product, old/new terms, common misspellings
@app.route('/about')
@app.route('/info')
def about():
    return 'here is info about our site'
# we can pass parameters in the URL (Represent the State REST)
@app.route('/greet')
@app.route('/greet/<fname>') # the <> indicate a URL positional argument
@app.route('/greet/<fname><sname>') # two positional REST parameters
def greet(fname=None, sname=None):
    if fname:
        if sname:
            return f'<h2>Welcome {fname} {sname}'
        else:
            return f'<h2>Welcome {fname}'
    else:
        return '<h2>Welcome</h2>'
# a menu of links
@app.route('/menu')
def menu():
    # here is some basic html
    link1 = '<a href="/">Home</a>'
    link2 = '<a href="/about">About</a>'
    link3 = '<a href="/greet">Greet</a>'
    link4 = '<a href="/snow">Snow</a>'
    return f'{link1} | {link2} | {link3} | {link4}'

# we usually try to avoid writing too much HTML within Python
# Flask offers a template engine with a microsyntax


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True) # debug will reload on change (use for development)
