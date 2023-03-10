from flask import Flask, render_template,request,redirect,url_for
import sqlite3

app =Flask(__name__)

# connection = sqlite3.connect("signup.db")
# cursor = connection.cursor()

# connection.commit()
# cursor.close()

@app.route("/", methods=["GET","POST"])
def signup():
    if(request.method == "POST"):
        if(request.form["username"]!= "" and request.form["password"]!= ""):
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            connection = sqlite3.connect("signup.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO person VALUES('"+username+"','"+email+"','"+password+"')")
            connection.commit()
            cursor.close()
        else:
            msg = "Something went wrong"
            return render_template("login.html",msg = msg)
    return render_template("signup.html")
@app.route("/login", methods=["GET","POST"])
def login():
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        connection = sqlite3.connect("signup.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM person WHERE username ='"+username+"' and password='"+password+"'")
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        if len(result)>0:
            return redirect(url_for("home"))
        else:
            return render_template("login.html")

        # msg = "Your account is created"
        
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/trending")
def trending():
    return render_template("trending.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=8051)