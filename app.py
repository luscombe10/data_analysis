from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    user_agent = "Henry"
    return render_template("main.html", name=user_agent)


@app.route("/test")
def test():
    return "<h1>Hello World</h1>"


@app.route("/user")
def user():
    return render_template("user.html", name="Henry")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)