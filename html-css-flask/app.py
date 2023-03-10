import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session


def register_user_to_db(username, password):
    connection = sqlite3.connect('user.db')
    cur = connection.cursor()
    cur.execute('INSERT INTO users(username,password) values (?,?)', (username, password))
    connection.commit()
    connection.close()


def check_user(username, password):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    cursor.execute('Select username,password FROM users WHERE username=? and password=?', (username, password))

    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


app = Flask(__name__)
app.secret_key = "974c4c344fd818bd1e2a1c4469f98b298d9e7e59"


@app.route("/")
def index():
    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        register_user_to_db(username, password)
        return redirect(url_for('index'))

    else:
        return render_template('register.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))
        if check_user(username, password):
            session['username'] = username

        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/home', methods=['POST', "GET"])
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return "Username or Password is wrong!"



if __name__ == '__main__':
    app.run(debug=True)
