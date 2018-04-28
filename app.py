from flask import Flask, render_template, flash, request, url_for, redirect, session, g
from wtforms import Form
from dbconnect import connection
from util import query_fetch, query_mod
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
    date = request.form.get('date')

    """
    def post_get():
    post_id = request.form.get('pid')
    sql = "SELECT title, category, tags, content FROM posts WHERE pid = '{}'".format(post_id)
    if VERBOSE:
        print("post get query:" + sql)
    indicator = query_fetch(sql, DB)
    response = PostList()
    if indicator:
        response.data['pid'] = post_id
        response.data['title'] = indicator['title']
        response.data['category'] = indicator['category']
   post_tags = 'dog, 2017, happy, weekend'
        response.data['tags'] = indicator['tags']
        response.data['content'] = indicator['content']
    else:
        response = ErrorResponse()
        response.error['errorCode'] = '105'
        response.error['errorMsg'] = 'Post does not exist'
    return jsonify(response.__dict__)"""
    return render_template("index.html")


@app.route('/home/customer/')
def customer_page():
    print(session['user'])
    print(session['type'])
    # If the user logged in a session with customer account
    if g.type == 'customer':
        return render_template("chome.html")
    return redirect(url_for('home_page'))


@app.route('/home/agent/')
def agent_page():
    print(session['user'])
    print(session['type'])
    if g.type == 'agent':
        return render_template("ahome.html")
    return redirect(url_for('home_page'))


@app.route('/home/staff/')
def staff_page():
    print(session['user'])
    print(session['type'])
    if g.type == 'staff':
        return render_template("shome.html")
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
    return redirect(url_for('home_page'))


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
