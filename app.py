"""
 Note1 : We are going to run this app from a virtual environment because the purpose is not to install flask
 in the overall python installation in the system and because it is the best practices option
 Thus, the follow is the steps i used to create the "virtualenv":
 1- install the module for virtualenv
   $ pip3 install virtualenv
 2- Go to the root of the directory where starts the website file, in this case mysite. Set the virtualenv project
   $ python3 -m venv virtual ---> This create a new directory "virtual" which contains a new python3 installation
 3- Activate the virtualenv
   $ source virtual/bin/activate
 4- install flask  with pip inside the virtualenv
   $ pip3 install flask
 5- To get off the venv just run:
   $ deactivate
 Note2 : Follow the next lines to start up the application manually and accesing it from outside the server. From the working directory :
 $ export FLASK_APP=script1.py
 $ flask run --host=0.0.0.0 &  # Actually, this is excecuted from the script, so is not need it
 * Serving Flask app "script1.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from validate_email import validate_email

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/height_collector' # ----> if runinng locally in ubuntutesting
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bjpnwsnntybnbt:2ce93058d0a497e4ab418f0adfdd09d48a523a9bf69f215e995b2818bd0a5a0f@ec2-107-21-224-61.compute-1.amazonaws.com:5432/d57d6u704adh38?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        is_valid = validate_email(request.form["email_name"], check_mx=True)
        if is_valid:
                if db.session.query(Data).filter(Data.email_ == email).count() == 0:
                    data=Data(email, height)
                    db.session.add(data)
                    db.session.commit()
                    average_height=db.session.query(func.avg(Data.height_)).scalar()
                    average_height=round(average_height,2)
                    count=db.session.query(Data.height_).count()
                    send_email(email, height, average_height, count)
                    return render_template("success.html")
                return render_template('index.html', text="Seems like you have entered same email before !")
        return render_template("index.html", text="Seems like you have entered a wrong email !")


if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0', port=5000) # ----> if runinng locally in ubuntutesting
    app.run()
