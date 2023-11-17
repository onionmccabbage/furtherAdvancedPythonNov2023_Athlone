# Flask solves web server problems by providing a configurable micro service web server
# might need to pip isntall Flask
# Flask is NOT a secure web server - use with Apache or tomcat etc for security
# but for an internal web server it is great

from flask import Flask

app = Flask(__name__) # this is conventional
# we declare routes for our app
@app.route('/')
def root():
    return 'hello and welcome to Flask'

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True) # debug will reload on change (use for development)
