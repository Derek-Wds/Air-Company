from flask import Flask, render_template, flash, request, url_for, redirect, session, g
from wtforms import Form
from dbconnect import connection
from util import query_fetch, query_mod, fetch_all
from config import DB, secret_key
from hashlib import md5
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/', methods=['GET'])
def home_page_get():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def home_page_post():
    source_airport = request.form.get('source_airport')
    source_city = request.form.get('source_city')
    destination_airport = request.form.get('destination_airport')
    destination_city = request.form.get('destination_city')
    arrival_date = request.form.get('arrival_date')
    departure_date = request.form.get('departure_date')
    flight_number = request.form.get('flight_number')

    # Query flight based on airport
    if source_airport:
        sql = "SELECT * FROM flight WHERE departure_airport = '{}' AND arrival_airport = '{}'" \
          " departure_time = '{}'".format(source_airport, destination_airport, departure_date)
        response = fetch_all(sql, DB)
        return render_template('index.html', flights=response)
    # Query flight based on city
    elif source_airport:
        sql = "SELECT * FROM flight WHERE departure_city = '{}' AND arrival_city = '{}'" \
          " departure_time = '{}'".format(source_city, destination_city, departure_date)
        response = fetch_all(sql, DB)
        return render_template('index.html', flights=response)
    # Query flight status
    elif source_airport:
        sql = "SELECT * FROM flight WHERE flight_num = '{}' AND arrival_time = '{}'" \
          " departure_time = '{}'".format(flight_number, arrival_date, departure_date)
        response = fetch_all(sql, DB)
        return render_template('index.html', flights=response)
    return render_template('index.html')


@app.route('/home/customer/')
def customer_page():
    print(session['user'])
    print(session['type'])
    # If the user logged in a session with customer account
    if g.type == 'customer':
        return render_template("customer_home.html", username = session['user'])
    return redirect(url_for('home_page'))


@app.route('/home/agent/')
def agent_page():
    print(session['user'])
    print(session['type'])
    if g.type == 'agent':
        return render_template("agent_home.html", username = session['user'])
    return redirect(url_for('home_page'))


@app.route('/home/staff/')
def staff_page():
    print(session['user'])
    print(session['type'])
    if g.type == 'staff':
        return render_template("staff_home.html", username = session['user'])
    return redirect(url_for('home_page'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(405)
def request_error(e):
    return render_template('405.html')

@app.errorhandler(500)
def server_wrong(e):
    return render_template('500.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    return render_template("login.html")


@app.route('/login-customer/', methods = ['GET', 'POST'])
def login_customer():
    try:
        if request.method == "POST":
            session.pop('user', None)
            session.pop('type', None)
            email = request.form['email']
            # Password encoded with utf-8 first then encoded with md5
            password = md5(request.form['password'].encode('utf-8')).hexdigest()
            sql = 'SELECT password FROM customer WHERE email = "{}"'.format(email)
            db_pwd = query_fetch(sql, DB)
            if password == db_pwd['password']:
                session['user'] = email
                session['type'] = 'customer'
                print(session['user'])
                print(session['type'])
                return redirect(url_for('customer_page'))
            elif db_pwd is None:
                err = "Account does not exist"
                flash(err)
            else:
                err = "Password error!"
                flash(err)
        return render_template("login1.html")

    except Exception as e:
        flash(str(e))
        return render_template("login1.html")


@app.route('/login-agent/', methods = ['GET', 'POST'])
def login_agent():
    try:
        if request.method == "POST":
            session.pop('user', None)
            session.pop('type', None)
            email = request.form['email']
            # Password encoded with utf-8 first then encoded with md5
            password = md5(request.form['password'].encode('utf-8')).hexdigest()
            sql = 'SELECT password FROM booking_agent WHERE email = "{}"'.format(email)
            db_pwd = query_fetch(sql, DB)
            if password == db_pwd['password']:
                session['user'] = email
                session['type'] = 'agent'
                print(session['user'])
                print(session['type'])
                return redirect(url_for('agent_page'))
            elif db_pwd is None:
                err = "Account does not exist"
                flash(err)
            else:
                err = "Password error!"
                flash(err)
        return render_template("login2.html")

    except Exception as e:
        flash(str(e))
        return render_template("login2.html")


@app.route('/login-staff/', methods = ['GET', 'POST'])
def login_staff():
    try:
        if request.method == "POST":
            session.pop('user', None)
            session.pop('type', None)
            username = request.form['username']
            # Password encoded with utf-8 first then encoded with md5
            password = md5(request.form['password'].encode('utf-8')).hexdigest()
            sql = 'SELECT password FROM airline_staff WHERE username = "{}"'.format(username)
            db_pwd = query_fetch(sql, DB)
            if password == db_pwd['password']:
                session['user'] = username
                session['type'] = 'staff'
                print(session['user'])
                print(session['type'])
                return redirect(url_for('staff_page'))
            elif db_pwd is None:
                err = "Account does not exist"
                flash(err)
            else:
                err = "Password error!"
                flash(err)
        return render_template("login3.html")

    except Exception as e:
        flash(str(e))
        return render_template("login3.html")


@app.route('/register/', methods = ['GET', 'POST'])
def register_page():
    return render_template("register.html")


@app.route('/register-customer/', methods = ['GET', 'POST'])
def register_customer():
    try:
        if request.method == "POST":
            email = request.form['email']
            name = request.form['name']
            pwd = request.form['password']
            confirm_pwd = request.form['confirm_password']
            if pwd != confirm_pwd:
                err = "password and confirm password doesn't match!"
                flash(err)
                return render_template("form1.html")
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
            sql_check = 'SELECT * FROM customer WHERE email = "{}"'.format(email)
            user_exist = query_fetch(sql_check, DB)
            if user_exist is not None:
                err = "User already exists!"
                flash(err)
            else:
                sql_add = 'INSERT INTO customer VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", ' \
                            '"{}", "{}")'.format(email, name, password, building_number, street, city, state, phone_number,
                                                 passport_number, passport_expiration, passport_country, date_of_birth)
                query_mod(sql_add, DB)
                session['user'] = email
                session['type'] = 'customer'
                print(session['user'])
                print(session['type'])
                return redirect(url_for('customer_page'))
        return render_template("form1.html")

    except Exception as e:
        flash(str(e))
        return render_template("form1.html")


@app.route('/register-agent/', methods = ['GET', 'POST'])
def register_agent():
    try:
        if request.method == "POST":
            email = request.form['email']
            pwd = request.form['password']
            confirm_pwd = request.form['confirm_password']
            if pwd != confirm_pwd:
                err = "password and confirm password doesn't match!"
                flash(err)
                return render_template("form2.html")
            # Password encoded with utf-8 first then encoded with md5
            password = md5(request.form['password'].encode('utf-8')).hexdigest()
            booking_agent_id = request.form['booking_agent_id']
            sql_check = 'SELECT * FROM booking_agent WHERE email = "{}"'.format(email)
            user_exist = query_fetch(sql_check, DB)
            if user_exist is not None:
                err = "User already exists!"
                flash(err)
            else:
                sql_add = 'INSERT INTO booking_agent VALUES("{}", "{}", "{}")'.format(email, password, booking_agent_id)
                query_mod(sql_add, DB)
                session['user'] = email
                session['type'] = 'agent'
                print(session['user'])
                print(session['type'])
                return redirect(url_for('agent_page'))
        return render_template("form2.html")

    except Exception as e:
        flash(str(e))
        return render_template("form2.html")


@app.route('/register-staff/', methods = ['GET', 'POST'])
def register_staff():
    try:
        if request.method == "POST":
            username = request.form['username']
            pwd = request.form['password']
            confirm_pwd = request.form['confirm_password']
            if pwd != confirm_pwd:
                err = "password and confirm password doesn't match!"
                flash(err)
                return render_template("form3.html")
            # Password encoded with utf-8 first then encoded with md5
            password = md5(request.form['password'].encode('utf-8')).hexdigest()
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            date_of_birth = request.form['date_of_birth']
            airline_name = request.form['airline_name']

            sql_check = 'SELECT * FROM airline_staff WHERE username = "{}"'.format(username)
            user_exist = query_fetch(sql_check, DB)
            if user_exist is not None:
                err = "User already exists!"
                flash(err)
            else:
                sql_add = 'INSERT INTO airline_staff VALUES("{}", "{}", "{}", "{}", "{}", "{}")'.format(
                    username, password, first_name, last_name, date_of_birth, airline_name)
                query_mod(sql_add, DB)
                session['user'] = username
                session['type'] = 'staff'
                print(session['user'])
                print(session['type'])
                return redirect(url_for('staff_page'))
        return render_template("form3.html")

    except Exception as e:
        flash(str(e))
        return render_template("form3.html")


@app.route('/logout/', methods = ['GET', 'POST'])
def logout_redirect():
    print(session['user'])
    print(session['type'])
    session.pop('user', None)
    session.pop('type', None)
    return redirect(url_for('login_page'))


@app.before_request
def before_request():
    g.user = None
    g.type = None
    if 'user' in session:
        g.user = session['user']
    if 'type' in session:
        g.type = session['type']


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
