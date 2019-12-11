from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def home():
    return  render_template("home.html")
@app.route('/lo')
def login():
    return  render_template("login.html")
@app.route('/re')
def reg():
    return  render_template("reg.html")
@app.route('/stl')
def stlog():
    return  render_template("stlog.html")
@app.route('/tchl')
def tlog():
    return  render_template("teachlog.html")
@app.route('/str')
def streg():
    return  render_template("streg.html")
@app.route('/tr')
def teachlog():
    return  render_template("teachreg.html")

@app.route('/trr',methods=['POST'])
def teachreg():
    conn = mysql.connector.connect(host='localhost', db='db', user='root', password='')
    sn = str(request.form["sn"])
    c = str(request.form["c"])
    b = str(request.form["b"])
    date = str(request.form["date"])
    em = str(request.form["em"])
    pw = str(request.form["pw"])
    cur = conn.cursor()
    cur.execute( "insert into tregis values('" + sn + "','" + c + "','" + b + "','" + date + "','" + em + "','" + pw + "')")
    conn.commit()
    return render_template('suc.html')

@app.route('/reg',methods=['POST'])
def regis():
    conn=mysql.connector.connect(host='localhost',db='db',user='root',password='')
    sn=str(request.form["sn"])
    c=str(request.form["c"])
    b=str(request.form["b"])
    date=str(request.form["date"])
    em=str(request.form["em"])
    pw=str(request.form["pw"])
    cur=conn.cursor()
    cur.execute("insert into stregis values('"+sn+"','"+c+"','"+b+"','"+date+"','"+em+"','"+pw+"')")
    conn.commit()
    return render_template('suc.html')
@app.route('/login',methods=['POST'])
def log():
    conn=mysql.connector.connect(host='localhost',db='db',user='root',password='')
    un=str(request.form["em"])
    pw=str(request.form["pw"])
    cur=conn.cursor()
    cur.execute("select * from login where username='" +un+ "' and password='" +pw+ "'")
    ar=cur.fetchone()

    if(ar[2]=="admin"):
        return render_template('afterlogin.html', user=ar)
    elif (ar[2] == "student"):
        return render_template('welstud.html' , user=ar)
    elif (ar[2] == "teacher"):
        return render_template('welteach.html', user=ar)

@app.route('/trlist')
def tealist():
    conn = mysql.connector.connect(host='localhost',db='db',user='root',password='')
    cur=conn.cursor()
    cur.execute("select * from tregis")
    ar = cur.fetchall()
    return  render_template('list.html',data=ar)

@app.route('/sslist')
def sslist():
    conn = mysql.connector.connect(host='localhost',db='db',user='root',password='')
    cur=conn.connect()
    cur.execute("select * from stregis")
    ar = cur.fetchall()
    return  render_template('lists.html',data=ar)
@app.route('/upd')
def update():
    conn = mysql.connector.connect(host='localhost',db='db',user='root',password='')
    cur = conn.cursor()
    id=request.args.get('id')
    cur.execute("update teachers set status='true' where id="+id)
    conn.commit()
    cur.execute("select * from teachers where id="+id)
    ar1=cur.fetchone()
    name=str(ar1[1])
    pwd=str(ar[4])
    cur.execute("insert into login values('" +name+"','"+pwd+"','teacher')")
    conn.commit()

    cur.execute("select * from teachers")
    ar = cur.fetchall()


@app.route('/upds')
def updates():
    conn = mysql.connector.connect(host='localhost', db='db', user='root', password='')
    cur = conn.cursor()
    id = request.args.get('id')
    cur.execute("update students set status='true' where id=" + id)
    conn.commit()
    cur.execute("select * from students where id=" + id)
    ar1 = cur.fetchone()
    name = str(ar1[1])
    pwd = str(ar[4])
    cur.execute("insert into login values('" + name + "','" + pwd +
    "','student')")
    conn.commit()

    cur.execute("select * from students")
    ar = cur.fetchall()





if __name__ == '__main__':
    app.run()
