from flask import Flask, render_template, url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
#db_host = ""
#db_name = "d90p31vkkl6td1"
#db_user = "jkbvrgxdgnhcbh"
#db_port = 5432
#db_password = "0f737abe099ffc9dcc4d72375fa40bcbf1c1a5ca516ddc0040268f0e63edb50d"
#db_conn = psycopg2.connect(host = db_host, port= db_port, dbname=db_name, user=db_user, password=db_password)
#db_cursor = db_conn.cursor

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jkbvrgxdgnhcbh:0f737abe099ffc9dcc4d72375fa40bcbf1c1a5ca516ddc0040268f0e63edb50d@ec2-52-203-160-194.compute-1.amazonaws.com:5432/d90p31vkkl6td1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    fName = db.Column(db.String(30))
    lName = db.Column(db.String(30))
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
@app.route('/', methods=['POST', 'GET'])
def index():
        return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        fName = request.form['FirstName']
        lName = request.form['LastName']
        if fName == '' or lName == '':
            return render_template('index.html', message='Please fill out both fields.')
        else:
            if db.session.query(Feedback).filter(Feedback.fName == fName).count() == 0 and db.session.query(Feedback).filter(Feedback.lName == lName).count() == 0:
                data = Feedback(fName, lName)
                db.session.add(data)
                db.session.commit()
                return render_template('index.html', message='Form has been submitted.')
            return render_template('index.html', message='User is already registered.')
if __name__ == '__main__':
    app.run(debug = True)