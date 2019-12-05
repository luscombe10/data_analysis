from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = "super_secret    "
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    user_agent = "Henry"
    return render_template("main.html", name=user_agent)


@app.route("/test")
def test():
    return "<h1>Hello World</h1>"


@app.route("/user", methods=["GET", "POST"])
def user():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("user.html", form=form, name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


class NameForm(Form):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField("Submit")
    

if __name__ == "__main__":
    app.run(debug=True)