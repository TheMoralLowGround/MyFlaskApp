from flask import (
    Flask,
    render_template,
    request,
    redirect,
    abort,
    url_for,
    session,
    flash,
)
from flask.helpers import url_for

app = Flask(__name__)

app.secret_key = "MYvfVrIdmEenp3vHvWaxvVGKjojAOZsc"


@app.errorhandler(404)
def handle_pagenotfound(error):
    return render_template("404.html"), 404


@app.route("/")
def home():
    if "username" in session:
        return f"Hi {session['username']} ! Welcome Home !!"
    return redirect(url_for("login"))


@app.route("/divide")
def divide():
    a = 10
    b = 3
    return str(a / b)


@app.route("/notifications")  # Simple routing
def notifications():
    return "This is notifications page"


@app.route("/user/<username>")  # Dynamic routing
def userpage(username):
    return render_template("user.html", username=username)


@app.route("/multiply/<int:a>/<int:b>")  # Convertors
def multiply(a, b):
    return str(a * b)


@app.route("/profile")
def profile():
    return "profile"


@app.route("/settings/")  # Trailing/Behaviour
def settings():
    return "settings"


@app.route("/search/")  # GET request
def search():
    fruits = ["apple", "banana", "orange", "pineapple"]
    query = request.args.get("query")
    selected = [f for f in fruits if query in f]
    return ", ".join(selected)


@app.route("/login/", methods=["GET", "POST"])  # POST request
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "morallowground" and password == "Password-1":
            session["username"] = "MoralLowGround"
            return "Welcome MoralLowGround"
        else:
            # abort(401)  # Unauthorized
            flash("The username or password you have entered is invalid")
            return render_template("login.html")
    return render_template("login.html")


@app.route("/logout/")
def logout():
    session.pop("username", None)
    return "You are now LoggedOut"


if __name__ == "__main__":
    app.run(debug=True)