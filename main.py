from flask import request
from flask import make_response
from flask import Flask, render_template, url_for, session, redirect,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField("INSERT YOUR NAME?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    data = "START PAGE"
    return render_template("index.html", data=data), 200


@app.route('/login', methods=["GET", "POST"])
def login():
    info = ''
    name = None
    data = "START PAGE"
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("You changed your name!")

        session['name'] = form.name.data
        return redirect(url_for('login'))


    return render_template("login.html", data=data, form=form, name=session.get('name'),info=info), 200


@app.route('/about/')
def about():
    data = "ABOUT PAGE"
    user_agent = request.headers.get('User-Agent')
    list = [1, 2, 3]
    addres_info = url_for('about', _external=True)

    return render_template("about.html", data= data, user_agent= user_agent, list= list, addres_info= addres_info)


@app.route('/cookie/')
def cookie():
    data = "COOKIE PAGE"
    response = make_response("CARRIES COOKIE!")
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "USER:" + name + "ID:" + str(id)

@app.route('/pictures/')
def pictures():
    return render_template("pictures.html")


@app.errorhandler(404)
def error_404(data):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)

