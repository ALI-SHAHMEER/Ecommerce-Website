
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
