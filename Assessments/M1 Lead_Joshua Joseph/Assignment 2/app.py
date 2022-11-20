# from crypt import methods
import email
from logging import warning
from xml.dom.expatbuilder import parseString
from flask import Flask,render_template,url_for,request,make_response
from flask_mysqldb import MySQL
from flask_session import Session


app = Flask(__name__,template_folder = 'templates')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'alchemy'

mysql = MySQL(app)

class sessionobj:
    def __init__(self,email):
        self.email = email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signuppage.html")


@app.route('/someurl/',methods=['POST'])
def dummyfunction():
    username= request.form.get('name')
    pasword = request.form.get('password')
    print(username,pasword)
    cur = mysql.connection.cursor()
    result_value = cur.execute("select * from users where email=\""+username+"\""+"and password=\""+pasword+"\"")
    print(result_value,type(result_value))
    warn = '<div class="alert alert-danger alert-dismissible fade show" role="alert" style="position:absolute;bottom:5%;right:5%;z-index:100;"><strong>User not found!!!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    succ = '<div class="alert alert-success alert-dismissible fade show" role="alert" style="position:absolute;bottom:5%;right:5%;z-index:100;"><strong>User signed in Successfully!!!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    if(result_value == 0):
        return render_template("index.html",warning = warn)
    # Session['useremail'] = sessionobj(username)
    resp = make_response(render_template("welcome.html"))
    resp.set_cookie("email",username,expires=None)
    username.replace('.','[dot]')
    return render_template("welcome.html",path="/delete/"+username)

@app.route('/addtodb/',methods=['POST'])
def dummyfunction2():
    username= request.form.get('name')
    pasword = request.form.get('password')
    email = request.form.get('email')
    roll = request.form.get('roll')
    # Session['useremail'] = sessionobj(email).__dict__
    print(username,pasword,email,roll)
    cur = mysql.connection.cursor()
    query = "insert into users (name,email,rollnumber,password)values("+'"'+username+'",'+'"'+email+'",'+'"'+roll+'",'+'"'+pasword+'")'
    print(query)
    result_value = cur.execute(query)
    mysql.connection.commit()
    cur.close()
    print(result_value,type(result_value))
    # warn = '<div class="alert alert-danger alert-dismissible fade show" role="alert" style="position:absolute;bottom:5%;right:5%;z-index:100;"><strong>User not found!!!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    # succ = '<div class="alert alert-success alert-dismissible fade show" role="alert" style="position:absolute;bottom:5%;right:5%;z-index:100;"><strong>User signed in Successfully!!!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    # if(result_value == 0):
        # return render_template("index.html",warning = warn)
    return render_template("index.html")

@app.route('/delete/<string:id>',methods=['POST'])
def dummyfunction3(id):
    cur = mysql.connection.cursor()
    id.replace('[dot]','.')
    # print(request.removeprefix("delete/"))
    query = 'delete from users where email=\"'+id+"\""
    print(query)
    result_value = cur.execute(query)
    mysql.connection.commit()
    cur.close()
    print(result_value,type(result_value))
    # warn = '<div class="alert alert-danger alert-dismissible fade show" role="alert" style="position:absolute;bottom:5%;right:5%;z-index:100;"><strong>User not found!!!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    # succ = '<div class="alert alert-success alert-dismissible fade show" role="alert" style="position:absolute;bottom:5%;right:5%;z-index:100;"><strong>User signed in Successfully!!!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    # if(result_value == 0):
        # return render_template("index.html",warning = warn)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)    