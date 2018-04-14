from flask import Flask, render_template, flash, request, url_for, redirect
from wtforms import Form
from dbconnect import connection
from util import query_fetch, query_mod
from config import DB, secret_key
from hashlib import md5


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def home_page():
    return render_template("test.html")

@app.route('/home/customer/')
def customer_page():
    return render_template("chome.html")


@app.route('/home/agent/')
def agent_page():
    return render_template("ahome.html")


@app.route('/home/staff/')
def staff_page():
    return render_template("shome.html")


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
            # Password encoded with utf-8 first then encoded with md5
            password = md5(request.form['password'].encode('utf-8')).hexdigest()
            print(password)
            sql = 'SELECT password FROM customer WHERE email = "{}"'.format(email)
            print(sql)
            db_pwd = query_fetch(sql, DB)
            print(db_pwd)
            if str(password) == str(db_pwd):
                return redirect(url_for('customer_page'))
            elif db_pwd is None:
                err = "Account does not exist"
                flash(err)
            else:
                err = "Password error!"
                flash(err)
        return render_template("login.html")

    except Exception as e:
        flash(str(e))
        return render_template("login.html")


class Registration(Form):
    pass

@app.route('/register/', methods = ['GET', 'POST'])
def register_page():
    # Make input form for everything in one page due to sql not null limitation
    return render_template("register.html")


@app.route('/customer/', methods = ['GET', 'POST'])
def register_page1():
    return render_template("register.html")

"""
    try:
        if request.method == "POST":
            email = request.form['email']
            # Password encoded with utf-8 first then encoded with md5
            password = md5(request.form['password'].encode('utf-8')).hexdigest()
            building_number = request.form['building_number']
            street = request.form['street']
            city = request.form['city']
            state = request.form['state']
            phone_number = request.form['phone_number']
            passport_number = request.form['passport_number']
            passport_expiration = request.form['passport_expiration']
            passport_country = request.form['passport_country']
            date_of_birth = request.form['date_of_birth']
            print(password)
            sql_check = 'SELECT * FROM customer WHERE email = "{}"'.format(email)
            user_exist = query_fetch(sql_check, DB)
            if user_exist is not None:
                err = "User already exists!"
                flash(err)
            else:
                sql_add = 'INSERT INTO customer VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", ' \
                            '"{}", "{}")'.format(email, password, building_number, street, city, state, phone_number,
                                                 passport_number, passport_expiration, passport_country, date_of_birth)
                query_mod(sql_add, DB)
                return redirect(url_for('customer_page'))
    except Exception as e:
        flash(str(e))
        return render_template("form1.html")
"""

@app.route('/agent/', methods = ['GET', 'POST'])
def register_page2():
    return render_template("form2.html")


@app.route('/staff/', methods = ['GET', 'POST'])
def register_page3():
    return render_template("form3.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
