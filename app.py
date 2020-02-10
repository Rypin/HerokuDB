from flask import Flask, render_template, url_for, request,redirect
import psycopg2

app = Flask(__name__)
app.config['POSTGRESQL_DATABASE_URI'] = 'postgres://jkbvrgxdgnhcbh:0f737abe099ffc9dcc4d72375fa40bcbf1c1a5ca516ddc0040268f0e63edb50d@ec2-52-203-160-194.compute-1.amazonaws.com:5432/d90p31vkkl6td1'
db_host = "ec2-52-203-160-194.compute-1.amazonaws.com"
db_name = "d90p31vkkl6td1"
db_user = "jkbvrgxdgnhcbh"
db_port = 5432
db_password = "0f737abe099ffc9dcc4d72375fa40bcbf1c1a5ca516ddc0040268f0e63edb50d"

db_conn = psycopg2.connect(host = db_host, port= db_port, dbname=db_name, user=db_user, password=db_password)
db_cursor = db_conn.cursor

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_fname = request.form['Fname']
        task_lname = request.form['Lname']
        task = "INSERT INTO users(firstname, lastname) VALUES ("+task_fname+", "+task_lname+")"
        try:
            db_cursor.execute(task)
            return redirect('/')
        except:
            return 'Issue inserting into Database'
    else:

        return render_template('index.html')
@app.route('/page2')
def page2():
    return 'Welcome'
if __name__ == '__main__':
    app.run(debug = True)