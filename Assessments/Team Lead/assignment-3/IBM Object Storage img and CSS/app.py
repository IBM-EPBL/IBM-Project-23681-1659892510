from flask import Flask, render_template,url_for
import flask
import getimagesibm

app = Flask(__name__)
app = Flask(__name__,template_folder = 'templates')

@app.route("/")
def index():
    getimagesibm.main()
    imgcontent = [url_for('static', filename='Screenshot (30).png'),url_for('static', filename='Screenshot (31).png'),url_for('static', filename='Screenshot (32).png'),url_for('static', filename='Screenshot (34).png'),url_for('static', filename='Screenshot (44).png')]
    return render_template("index.html",images = imgcontent)

if __name__ == "__main__":
    app.run(debug=True)