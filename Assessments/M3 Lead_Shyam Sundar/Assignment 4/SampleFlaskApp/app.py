# from crypt import methods
from flask import *
from dboperations import *
from newsapilocal import *

app = Flask(__name__,template_folder = 'templates')


class sessionobj:
    def __init__(self,email):
        self.email = email

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/hello')
def helloworld():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)    