from flask import Flask, render_template, flash, request, url_for, redirect
from wtforms import Form
from dbconnect import connection

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x1b\x9d\xa8\x9b\xbbn\xa5\xfd\xd2\xa4\x16%{c\xba~\xd5\xb1\x11iy\x97=\x96'



@app.route('/')
def home_page():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    try:
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']

            if email == 'a@qq.com' and password == '1':
                return redirect(url_for('homepage'))
            else:
                err = "Account does not exist or password error!"
                flash(err)
        return render_template("login.html")

    except Exception as e:
        flash(str(e))
        return render_template("login.html")


class Registration(Form):
    pass

@app.route('/register/', methods = ['GET', 'POST'])
def register_page():
    return render_template("register.html")


@app.route('/customer/', methods = ['GET', 'POST'])
def register_page1():
    return render_template("form1.html")


@app.route('/agent/', methods = ['GET', 'POST'])
def register_page2():
    return render_template("form2.html")


@app.route('/staff/', methods = ['GET', 'POST'])
def register_page3():
    return render_template("form3.html")




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
