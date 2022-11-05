# from crypt import methods
from flask import *
from flask_cors import CORS

app = Flask(__name__,template_folder = 'templates')


class sessionobj:
    def __init__(self,email):
        self.email = email

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/signinusers',methods=['POST'])
def signinusers():
    print(json.loads(request.get_data()))
    return json.loads(request.get_data())['name']

@app.route('/signin')
def signin():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signuppage.html")

if __name__ == "__main__":
    app.run(debug=True)    