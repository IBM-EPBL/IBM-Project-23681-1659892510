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

@app.route('/isgoodtoload',methods=['POST'])
def isgoodtoload():
    value = checkkey(json.loads(request.get_data())['id'],json.loads(request.get_data())['key'])
    return value

@app.route('/explore')
def explore():
    return render_template("Explore.html")    

@app.route('/signinusers',methods=['POST'])
def signinusers():
    value = signinusersdb(json.loads(request.get_data())['id'],json.loads(request.get_data())['password'])
    print(json.loads(request.get_data()))
    return value

@app.route('/signin')
def signin():
    return render_template("index.html")

@app.route('/signupusers',methods=['POST'])
def signupusers():
    value = signupusersdb(json.loads(request.get_data())['name'],json.loads(request.get_data())['email'],json.loads(request.get_data())['password'])
    print(json.loads(request.get_data()))
    return value

@app.route('/getsingleheadline',methods=['POST'])
def getsingleheadline():
    value = getsingleheadlinedb(json.loads(request.get_data())['id'])
    print(json.loads(request.get_data()))
    return value

@app.route('/getsinglebusinessheadline',methods=['POST'])
def getsinglebusinessheadline():
    value = getsinglebusinessheadlinedb(json.loads(request.get_data())['id'])
    print(json.loads(request.get_data()))
    return value

@app.route('/getsinglesportsheadline',methods=['POST'])
def getsinglesportsheadline():
    value = getsinglesportsheadlinedb(json.loads(request.get_data())['id'])
    print(json.loads(request.get_data()))
    return value

@app.route('/getsingleentertainmentheadline',methods=['POST'])
def getsingleentertainmentheadline():
    value = getsingleentertainmentheadlinedb(json.loads(request.get_data())['id'])
    print(json.loads(request.get_data()))
    return value

@app.route('/getsingletechheadline',methods=['POST'])
def getsingletechheadline():
    value = getsingletechheadlinedb(json.loads(request.get_data())['id'])
    print(json.loads(request.get_data()))
    return value

@app.route('/getsinglemedheadline',methods=['POST'])
def getsinglemedheadline():
    value = getsinglemedheadlinedb(json.loads(request.get_data())['id'])
    print(json.loads(request.get_data()))
    return value

@app.route('/signup')
def signup():
    return render_template("signuppage.html")

@app.route("/storeheadlinesindb")
def storeheadlinesindbapppy():
    return jsonify(storeheadlinesindb())

@app.route('/headlines')
def headlines():
    return jsonify(getheadlinesfromdb())

@app.route('/bheadlines')
def bheadlines():
    return jsonify(getbusinessheadlinesfromdb())

@app.route('/sheadlines')
def sheadlines():
    return jsonify(getsportsheadlinesfromdb())

@app.route('/eheadlines')
def eheadlines():
    return jsonify(getentertainmentheadlinesfromdb())

@app.route('/theadlines')
def theadlines():
    return jsonify(gettechheadlinesfromdb())

@app.route('/heheadlines')
def mheadlines():
    return jsonify(gethealthheadlinesfromdb())

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)    