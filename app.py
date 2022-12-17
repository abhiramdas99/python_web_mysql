
# step 1 - import library 
from flask import Flask,render_template,request

#step 2 - import database library
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']='python_web_mysql'

mysql=MySQL(app)


@app.route('/')
def index():
    cur=mysql.connection.cursor()
    data=cur.execute("select * from employee_detail")
    if data>0:
        employees=cur.fetchall()
    
    return render_template('index.html',employees=employees)


if __name__=="__main__":
    app.run(debug=True)

